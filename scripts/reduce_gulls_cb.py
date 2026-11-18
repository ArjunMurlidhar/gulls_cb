"""Reweight a circumbinary gulls run and write detection and stable-system catalogs.

This is a one-pass copy of scripts/reduce_gulls.py. The .out header it expects
is the one written by writeHeader in src/info.cpp: Field, SubRun, raw_weight,
weight, and, for each observatory group i,

    ObsGroup_<i>_chi2_bin
    ObsGroup_<i>_chi2_pl
    ObsGroup_<i>_flatchi2_bin
    ObsGroup_<i>_flatchi2_pl

Each .out file is read once. A field's norm is the sum of raw_weight over every
event in that field. Files that cannot be parsed are skipped, and so are files
whose names end with _discarded.out. Discarded files do not enter the norm,
the weights, or any HDF5 table.

final_weight = (nevents_per_tile / norm) * weight
norm_weight  = raw_weight / norm

norm_weight is not multiplied by nevents_per_tile. nevents_per_tile comes from
the rates file at $GULLS_BASE_DIR + RATES_FILE, indexed by Field.

Detections do not use an N>3sigma cut. With --ffp-det-cuts CUT, observatory
group i contributes a row to its .det table when chi2_bin or chi2_pl is greater
than CUT. both_above_cut is true only when both are greater than CUT.

Stable P-type systems are the events whose light curves were generated. They
are written to one table, "stable", in {RUN_NAME}.stable.hdf5. A row is included
when flatchi2_bin or flatchi2_pl is non-zero for any observatory group.
"""

import argparse
import os
import re
import sys

import numpy as np
import pandas as pd


CB_COLUMNS = ('chi2_bin', 'chi2_pl', 'flatchi2_bin', 'flatchi2_pl')
FLAT_COLUMNS = ('flatchi2_bin', 'flatchi2_pl')
IDENTIFIER = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')
# Present in some catalogs and absent in others. Missing ones are not indexed.
OPTIONAL_INDEX_KEYS = {
    'Planet_mass', 't0lens1', 'u0lens1', 'tcroin', 'ucroin', 'LCOutput',
    'Lens_Dist', 'Source_Dist', 'Lens_pop', 'Source_pop',
}


def parse_args():
    parser = argparse.ArgumentParser(
        description='Reweight a circumbinary gulls simulation and write detection and stable-system catalogs')
    parser.add_argument('paramfile',
                        help='The parameter file for the simulation')
    parser.add_argument('--covfac', default=None,
                        help='Covering factor file')
    parser.add_argument('--ffp-bad-weights', action='store_true',
                        help='Recalculate the weights for free-floating planet simulations. If an argument is given, it is the number of days over which t0 could have been drawn.')
    parser.add_argument('--t0range', action='store', default=432.0, type=float,
                        help='The range of days over which t0 could be drawn (minus any gaps). Only used if a bad weights option is applied.')
    parser.add_argument('--in-raw', action='store_true',
                        help='The output files are in the raw subdirectory of FINAL_DIR')
    parser.add_argument('--move-files', action='store_true',
                        help='Move the output files to their homes')
    parser.add_argument('--limit', action='store', type=int,
                        help='Limit the number of files to read (option for testing)')
    parser.add_argument('--ffp-det-cuts', action='store', type=float, default=None,
                        help='Optional chi-square cutoff. For each observatory group, a row is a detection when chi2_bin or chi2_pl is greater than this cutoff. Does not apply an N>3sigma cut.')
    parser.add_argument('--split-masses', action='store_true',
                        help='Run contains many different masses, split them by unique masses')
    parser.add_argument('--recut', action='store_true',
                        help='Do not reprocess from scratch. Load the old "out" hdf5 file and apply the cuts again.')
    parser.add_argument('-k', '--add-key', action='append',
                        help='Add keys to be added to the hdf5store index over the default (use --print-keys to print the current set without running further)')
    parser.add_argument('--print-keys', action='store_true',
                        help='Print the current set of keys to be indexed in the hdf5store without running further')
    parser.add_argument('--save-csv', action='store_true',
                        help='Save the HDF5 files as CSV files too')
    return parser.parse_args()


def read_paramfile(path):
    try:
        table = pd.read_csv(path, sep='=', header=None, names=['param', 'value'])
    except Exception as exc:
        sys.exit(f'Could not read parameter file {path}: {exc}')
    table = table.dropna(subset=['param'])
    paramfile = {str(key).strip(): str(value).strip() for key, value in table.values}
    if 'OBS_GROUP_NAMES' not in paramfile or not paramfile['OBS_GROUP_NAMES']:
        sys.exit('Parameter file has no OBS_GROUP_NAMES')
    names = [name.strip() for name in paramfile['OBS_GROUP_NAMES'].split(',') if name.strip()]
    if not names:
        sys.exit('Parameter file has no OBS_GROUP_NAMES')
    paramfile['OBS_GROUP_NAMES'] = names
    for key in ('RUN_NAME', 'FINAL_DIR', 'RATES_FILE'):
        if key not in paramfile:
            sys.exit(f'Parameter file has no {key}')
    return paramfile


def group_column(group_index, suffix):
    return f'ObsGroup_{group_index}_{suffix}'


def group_columns(n_groups):
    columns = []
    for group_index in range(n_groups):
        for suffix in CB_COLUMNS:
            columns.append(group_column(group_index, suffix))
    return columns


def index_keys_for(paramfile, extra_keys):
    keys = [
        'Field', 'Planet_mass', 't0lens1', 'u0lens1', 'tcroin', 'ucroin',
        'LCOutput', 'Lens_Dist', 'Source_Dist', 'Lens_pop', 'Source_pop',
    ]
    if extra_keys:
        keys.extend(extra_keys)
    keys.extend(group_columns(len(paramfile['OBS_GROUP_NAMES'])))
    return list(dict.fromkeys(keys))


def normalize_field_index(rates):
    if not pd.api.types.is_numeric_dtype(rates.index):
        sys.exit('Rates file ID_src is not numeric')
    values = pd.to_numeric(rates.index, errors='coerce').to_numpy(dtype=float)
    if not np.all(np.isfinite(values)) or not np.all(values == np.rint(values)):
        sys.exit('Rates file ID_src values are not whole numbers')
    rates = rates.copy()
    rates.index = np.rint(values).astype(int)
    rates.index.name = 'ID_src'
    if rates.index.has_duplicates:
        sys.exit('Rates file has duplicate ID_src values')
    return rates


def load_rates_catalog(path):
    if not os.path.isfile(path):
        sys.exit(f'Rates file not found: {path}')
    rates = pd.read_csv(
        path,
        sep=r'\s+',
        usecols=['ID_src', 'l_src', 'b_src', 'nevents_per_tile'],
    ).set_index('ID_src')
    rates = normalize_field_index(rates)
    rates['nevents_per_tile'] = pd.to_numeric(rates['nevents_per_tile'], errors='coerce')
    nan_mask = rates['nevents_per_tile'].isna()
    dropped_ids = []
    if nan_mask.any():
        dropped_ids = sorted(int(field) for field in rates.index[nan_mask])
        print(
            f'Dropping {int(nan_mask.sum())} rates row(s) with NaN nevents_per_tile: '
            f'ID_src {dropped_ids}'
        )
        rates = rates.loc[~nan_mask]
    return rates, dropped_ids


def filter_dropped_field_events(frames, dropped_ids):
    if not dropped_ids:
        return frames
    dropped = set(int(field) for field in dropped_ids)
    kept = []
    for data in frames:
        mask = ~data['Field'].isin(dropped)
        n_drop = int((~mask).sum())
        if n_drop:
            fields = sorted(int(field) for field in data.loc[~mask, 'Field'].unique())
            print(f'Skipping {n_drop} event(s) with Field in dropped rates IDs: {fields}')
        data = data.loc[mask]
        if len(data) == 0:
            continue
        kept.append(data)
    return kept


def load_saved_rates(path):
    if not os.path.isfile(path):
        sys.exit(f'Saved rates file not found: {path}')
    rates = pd.read_csv(path).set_index('ID_src')
    return normalize_field_index(rates)


def attach_covering_factors(rates, covfac_path):
    if covfac_path is None:
        rates['covfac'] = 1.0
        return rates
    # Hasn't been tested yet. Same as reduce_gulls.py: the file is read and joined.
    cftmp = pd.read_csv(covfac_path, sep=r'\s+', names=['ID', 'covfac']).set_index('ID')
    return rates.join(cftmp)


def read_out_file(path, n_groups, bad_weights):
    try:
        data = pd.read_csv(path, sep=r'\s+')
    except Exception as exc:
        print(f'Skipping {path} due to read error: {exc}')
        return None
    if data.shape[0] < 1:
        print(f'Skipping {path} with no data')
        return None

    required = ['Field', 'raw_weight', 'weight', *group_columns(n_groups)]
    if bad_weights:
        required.extend(['Planet_q', 'u0max', 'tE_ref', 'tE_helio'])
    missing = [column for column in required if column not in data.columns]
    if missing:
        print(f'Skipping {path}; missing columns: {", ".join(missing)}')
        return None

    data['Field'] = pd.to_numeric(data['Field'], errors='coerce')
    data['raw_weight'] = pd.to_numeric(data['raw_weight'], errors='coerce')
    data['weight'] = pd.to_numeric(data['weight'], errors='coerce')
    field_values = data['Field'].to_numpy(dtype=float)
    field_ok = (
        not data['Field'].isna().any()
        and np.all(np.isfinite(field_values))
        and np.all(field_values == np.rint(field_values))
    )
    if not field_ok:
        print(f'Skipping {path}; Field values are not whole numbers')
        return None
    if data['raw_weight'].isna().any() or data['weight'].isna().any():
        print(f'Skipping {path}; raw_weight or weight is not numeric')
        return None
    data['Field'] = data['Field'].astype(int)

    for column in group_columns(n_groups):
        data[column] = pd.to_numeric(data[column], errors='coerce')
    if bad_weights:
        for column in ('Planet_q', 'u0max', 'tE_ref', 'tE_helio'):
            data[column] = pd.to_numeric(data[column], errors='coerce')
        if data[['Planet_q', 'u0max', 'tE_ref', 'tE_helio']].isna().any().any():
            print(f'Skipping {path}; weight inputs are not numeric')
            return None
    return data


def fields_missing_from_rates(frames, rates):
    seen = set()
    for data in frames:
        seen.update(int(field) for field in data['Field'].unique())
    return sorted(seen.difference(int(field) for field in rates.index))


def accumulate_norms(frames, rates):
    rates['norm'] = 0.0
    for data in frames:
        grouped = data.groupby(data['Field'].astype(int))['raw_weight'].sum()
        for field, total in grouped.items():
            field = int(field)
            rates.loc[field, 'norm'] = rates.loc[field, 'norm'] + float(total)
    return rates


def apply_bad_weights(data, t0range):
    # Same correction as reduce_gulls.py.
    data['weight'] = (
        data['raw_weight']
        * np.sqrt(data['Planet_q'])
        * data['u0max']
        * (t0range / 365.25)
        / (data['tE_ref'] / data['tE_helio'])
    )
    return data


def apply_weights(data, rates):
    """Attach final_weight and norm_weight using the field norm already stored on rates."""
    fields = data['Field'].astype(int)
    norm = fields.map(rates['norm']).astype(float)
    nevents = fields.map(rates['nevents_per_tile']).astype(float)
    norm_values = norm.to_numpy(dtype=float)
    nevents_values = nevents.to_numpy(dtype=float)
    raw = data['raw_weight'].to_numpy(dtype=float)
    weight = data['weight'].to_numpy(dtype=float)
    positive = norm_values > 0

    norm_weight = np.zeros(len(data), dtype=float)
    final_weight = np.zeros(len(data), dtype=float)
    # norm_weight is raw_weight / norm. Do not scale it by nevents_per_tile.
    norm_weight[positive] = raw[positive] / norm_values[positive]
    final_weight[positive] = (nevents_values[positive] / norm_values[positive]) * weight[positive]
    data['final_weight'] = final_weight
    data['norm_weight'] = norm_weight

    if not positive.all():
        bad_fields = sorted({int(field) for field in data['Field'].to_numpy()[~positive]})
        print(f'Warning: norm is 0 for fields {bad_fields}; those weights are 0')
    return data


def add_field_sums(rates, data, value_column, sum_column, square_column=None):
    fields = data['Field'].astype(int)
    totals = data.groupby(fields)[value_column].sum()
    for field, total in totals.items():
        field = int(field)
        rates.loc[field, sum_column] = float(rates.loc[field, sum_column]) + float(total)
    if square_column is not None:
        squares = data[value_column].pow(2).groupby(fields).sum()
        for field, total in squares.items():
            field = int(field)
            rates.loc[field, square_column] = float(rates.loc[field, square_column]) + float(total)


def hdf5_rename(data):
    rename = {}
    for column in data.columns:
        if column.find('/') != -1 or column.find('[') != -1 or column.find(']') != -1 or column.find('.') != -1:
            rename[column] = column.replace('/', '_').replace('[', '').replace(']', '').replace('.', '')
    if rename:
        data = data.rename(columns=rename)
    return data


def data_columns_for(data, keys):
    columns = []
    missing = []
    for key in keys:
        if key not in data.columns:
            missing.append(key)
            continue
        if not pd.api.types.is_numeric_dtype(data[key]):
            continue
        if IDENTIFIER.match(key) is None:
            continue
        columns.append(key)
    return columns, missing


def numeric_nonzero(series):
    values = pd.to_numeric(series, errors='coerce')
    return values.notna() & (values != 0)


def stable_mask(data, n_groups):
    """True when any observatory group has a non-zero flat chi-square."""
    mask = pd.Series(False, index=data.index)
    for group_index in range(n_groups):
        for suffix in FLAT_COLUMNS:
            column = group_column(group_index, suffix)
            if column not in data.columns:
                continue
            mask = mask | numeric_nonzero(data[column])
    return mask


def detection_frame(data, group_index, cutoff):
    """Rows with chi2_bin or chi2_pl greater than cutoff, plus both_above_cut.

    No N>3sigma column is consulted.
    """
    bin_column = group_column(group_index, 'chi2_bin')
    pl_column = group_column(group_index, 'chi2_pl')
    if bin_column not in data.columns or pl_column not in data.columns:
        return None
    bin_values = pd.to_numeric(data[bin_column], errors='coerce')
    pl_values = pd.to_numeric(data[pl_column], errors='coerce')
    either = (bin_values > cutoff) | (pl_values > cutoff)
    if not bool(either.any()):
        return None
    detected = data.loc[either].copy()
    detected['both_above_cut'] = (
        (bin_values.loc[either].to_numpy(dtype=float) > cutoff)
        & (pl_values.loc[either].to_numpy(dtype=float) > cutoff)
    )
    return detected


def ensure_norm_weight(data, rates):
    if 'norm_weight' in data.columns:
        return data
    if 'raw_weight' not in data.columns or 'norm' not in rates.columns:
        print('Warning: norm_weight is missing and cannot be recomputed')
        data = data.copy()
        data['norm_weight'] = np.nan
        return data
    print('Recomputing norm_weight from raw_weight and the saved field norm')
    data = data.copy()
    fields = data['Field'].astype(int)
    norm_values = fields.map(rates['norm']).astype(float).to_numpy(dtype=float)
    raw = pd.to_numeric(data['raw_weight'], errors='coerce').to_numpy(dtype=float)
    norm_weight = np.zeros(len(data), dtype=float)
    positive = np.isfinite(norm_values) & (norm_values > 0) & np.isfinite(raw)
    norm_weight[positive] = raw[positive] / norm_values[positive]
    data['norm_weight'] = norm_weight
    return data


def iter_stored_frames(store):
    if 'out' not in store:
        print('Stored catalog has no "out" table')
        return
    for chunk in store.select('out', chunksize=100000):
        yield chunk


def append_frame(store, key, data, data_columns):
    if data is None or len(data) == 0:
        return
    store.append(key, data, index=False, data_columns=data_columns, format='table')


def finish_error_columns(detrates, group_names):
    for name in group_names:
        err2 = f'ObsGroup_{name}_final_rate_err2'
        err = f'ObsGroup_{name}_final_rate_err'
        detrates[err] = np.sqrt(detrates[err2].astype(float))
        detrates = detrates.drop(columns=[err2])
    return detrates


def save_csv_tables(store, path_for_key):
    for key in store.keys():
        name = key.strip('/')
        frame = store.select(name)
        destination = path_for_key(name)
        print(f'Saving {destination}')
        frame.to_csv(destination, sep=' ')


def output_directories(paramfile, in_raw):
    run_name = paramfile['RUN_NAME']
    run_dir = os.path.abspath(os.path.join(paramfile['FINAL_DIR'], run_name))
    if not os.path.isdir(run_dir):
        sys.exit(f'{run_dir} does not exist')
    for subdir in ('analysis', 'raw', 'lc', 'fm', 'logs'):
        os.makedirs(os.path.join(run_dir, subdir), exist_ok=True)
    outroot = os.path.join(run_dir, 'analysis', run_name)
    if in_raw:
        outfiledir = os.path.join(run_dir, 'raw')
    else:
        outfiledir = run_dir
    if not os.path.isdir(outfiledir):
        sys.exit(f'{outfiledir} does not exist')
    return outroot, outfiledir


def collect_out_files(outfiledir, n_groups, bad_weights, limit):
    frames = []
    n_skip = 0
    with os.scandir(outfiledir) as entries:
        for entry in entries:
            if not entry.is_file() or not entry.name.endswith('.out'):
                continue
            if entry.name.endswith('_discarded.out'):
                print(f'Skipping {entry.name}; discarded output is excluded')
                n_skip += 1
                continue
            data = read_out_file(entry.path, n_groups, bad_weights)
            if data is None:
                n_skip += 1
                continue
            fields = sorted(int(field) for field in data['Field'].unique())
            print(f'Read {entry.name} ({len(data)} events, fields {fields})')
            frames.append(data)
            if limit is not None and len(frames) >= limit:
                break
    print(f'Read {len(frames)} files, skipped {n_skip}')
    return frames


def prepare_frames(frames, rates, bad_weights, t0range):
    rates['final_rate'] = 0.0
    rates['final_rate_err2'] = 0.0
    prepared = []
    for data in frames:
        if bad_weights:
            data = apply_bad_weights(data, t0range)
        data = apply_weights(data, rates)
        add_field_sums(rates, data, 'final_weight', 'final_rate', 'final_rate_err2')
        prepared.append(hdf5_rename(data))
    rates['final_rate_err'] = np.sqrt(rates['final_rate_err2'].astype(float))
    rates = rates.drop(columns=['final_rate_err2'])
    return prepared, rates


def write_products(frames, outstore, detstore, stablestore, detrates, group_names, cutoff, data_columns, write_out):
    n_groups = len(group_names)
    warned_missing = set()
    for data in frames:
        columns, missing = data_columns_for(data, data_columns)
        for key in missing:
            if key in OPTIONAL_INDEX_KEYS or key in warned_missing:
                continue
            warned_missing.add(key)
            print(f'Index key not in the catalog: {key}')
        if write_out:
            append_frame(outstore, 'out', data, columns)

        stable = data.loc[stable_mask(data, n_groups)]
        if len(stable):
            append_frame(stablestore, 'stable', stable, columns)
            add_field_sums(detrates, stable, 'final_weight', 'stable_final_weight_sum')
            add_field_sums(detrates, stable, 'norm_weight', 'stable_norm_weight_sum')

        if cutoff is None:
            continue
        for group_index, name in enumerate(group_names):
            detected = detection_frame(data, group_index, cutoff)
            if detected is None:
                bin_column = group_column(group_index, 'chi2_bin')
                if bin_column not in data.columns and group_index not in warned_missing:
                    warned_missing.add(group_index)
                    print(f'No {bin_column} column; skipping detections for {name}')
                continue
            append_frame(detstore, name, detected, columns)
            rate_column = f'ObsGroup_{name}_final_rate'
            err_column = f'ObsGroup_{name}_final_rate_err2'
            add_field_sums(detrates, detected, 'final_weight', rate_column, err_column)
    return detrates


def main():
    args = parse_args()
    # Accepted so the original command line still parses. Neither action is used.
    _ = (args.move_files, args.split_masses)

    paramfile = read_paramfile(args.paramfile)
    group_names = paramfile['OBS_GROUP_NAMES']
    print('Parameter file:')
    print(paramfile)

    index_keys = index_keys_for(paramfile, args.add_key)
    if args.print_keys:
        print('index_keys:')
        print(index_keys)
        return

    print('Processing', paramfile['RUN_NAME'])
    if args.ffp_det_cuts is None:
        print('No chi-square cutoff given; detection tables will be empty')
    else:
        print(
            f'Detection cut: ObsGroup_<i>_chi2_bin > {args.ffp_det_cuts} '
            f'OR ObsGroup_<i>_chi2_pl > {args.ffp_det_cuts}'
        )
        print('No N>3sigma cut is applied')

    outroot, outfiledir = output_directories(paramfile, args.in_raw)
    print(f'Looking for .out files in {outfiledir}')

    if args.recut:
        rates = load_saved_rates(outroot + '.det.rates')
        frames = None
    else:
        base = os.getenv('GULLS_BASE_DIR')
        if not base:
            sys.exit('GULLS_BASE_DIR is not set')
        rates_path = os.path.abspath(os.path.join(base, paramfile['RATES_FILE']))
        rates, dropped_field_ids = load_rates_catalog(rates_path)
        rates = attach_covering_factors(rates, args.covfac)
        frames = collect_out_files(outfiledir, len(group_names), args.ffp_bad_weights, args.limit)
        frames = filter_dropped_field_events(frames, dropped_field_ids)
        missing = fields_missing_from_rates(frames, rates)
        if missing:
            sys.exit(f'Fields {missing} are not in the rates file {rates_path}')
        rates = accumulate_norms(frames, rates)
        frames, rates = prepare_frames(frames, rates, args.ffp_bad_weights, args.t0range)

    print(rates)

    detrates = rates.copy()
    for name in group_names:
        detrates[f'ObsGroup_{name}_final_rate'] = 0.0
        detrates[f'ObsGroup_{name}_final_rate_err2'] = 0.0
    detrates['stable_final_weight_sum'] = 0.0
    detrates['stable_norm_weight_sum'] = 0.0

    out_path = outroot + '.out.hdf5'
    if args.recut and not os.path.isfile(out_path):
        sys.exit(f'Stored catalog not found: {out_path}')

    out_mode = 'r' if args.recut else 'w'
    with pd.HDFStore(out_path, out_mode) as outstore, \
            pd.HDFStore(outroot + '.det.hdf5', 'w') as detstore, \
            pd.HDFStore(outroot + '.stable.hdf5', 'w') as stablestore:
        if args.recut:
            print(f'--recut option used, starting from {out_path}')
            source = (
                ensure_norm_weight(chunk, rates)
                for chunk in iter_stored_frames(outstore)
            )
            write_out = False
        else:
            source = frames
            write_out = True

        detrates = write_products(
            source, outstore, detstore, stablestore, detrates,
            group_names, args.ffp_det_cuts, index_keys, write_out,
        )
        detrates = finish_error_columns(detrates, group_names)
        detrates.to_csv(outroot + '.det.rates')

        if 'out' in outstore:
            print('\n'.join(outstore.select('out', start=0, stop=1).columns.tolist()))
        if args.save_csv:
            if 'out' in outstore:
                save_csv_tables(outstore, lambda name: outroot + '.out.csv')
            if 'stable' in stablestore:
                save_csv_tables(stablestore, lambda name: outroot + '.stable.csv')
            if len(detstore.keys()):
                save_csv_tables(
                    detstore,
                    lambda name: outroot + f'.det.{name}.csv',
                )

    if 'norm' in rates.columns:
        print(rates[rates['norm'] > 0])
    print(detrates.columns.tolist())
    print('detrates (>0):')
    first_rate = f"ObsGroup_{group_names[0]}_final_rate"
    print(detrates[detrates[first_rate] > 0])
    print('detrates:')
    print(detrates)


if __name__ == '__main__':
    main()
