#!/bin/bash
# Build a gulls rates table, counting only primary lenses, and write it to a file.
#
# Primary-lens-only: calls calc_rate_primary_lens.py, which keeps a lens
# catalog row only when ID == primary_ID (singles and primaries). Companion
# rows are dropped from the rate sum. Sources are not filtered.
#
# Usage:
#   scripts/run_rates_primary_lens.sh [sources_list] [lenses_list] [output_file]
#
# With no arguments this still reads gulls_surot2d_H2023.sources and
# gulls_surot2d_H2023.lenses from the working directory. Catalog paths inside
# an index are resolved relative to that index file. A field pair whose csv
# is not on disk is skipped. Field IDs in the table are the source-list IDs
# gulls stores as Field.
#
# The table is written by this script, not by a shell redirect. The default
# path is rates/binary_src_gulls_surot2d_H2024_V2.primary_lens.rates under the
# repository root (the parent of this script's directory). Pass output_file
# to write somewhere else. An existing file at the destination is left as it
# is; this script will not overwrite it.
#
# Requires python with pandas and numpy on PATH (conda env gulls).

set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
repo=$(cd "$here/.." && pwd)
calc_rate="$here/calc_rate_primary_lens.py"
sources_list=${1:-gulls_surot2d_H2023.sources}
lenses_list=${2:-gulls_surot2d_H2023.lenses}
output=${3:-"$repo/rates/binary_src_gulls_surot2d_H2024_V2.primary_lens.rates"}
python_bin=${PYTHON:-python}

echo "run_rates_primary_lens.sh: output $output" >&2
if [[ -e "$output" ]]; then
	echo "run_rates_primary_lens.sh: refusing to overwrite $output" >&2
	exit 1
fi

if [[ ! -f "$sources_list" || ! -f "$lenses_list" ]]; then
	echo "run_rates_primary_lens.sh: index file not found: $sources_list or $lenses_list" >&2
	exit 1
fi
if [[ ! -f "$calc_rate" ]]; then
	echo "run_rates_primary_lens.sh: missing $calc_rate" >&2
	exit 1
fi
if ! command -v "$python_bin" >/dev/null 2>&1; then
	echo "run_rates_primary_lens.sh: $python_bin not found (conda activate gulls, or set PYTHON)" >&2
	exit 1
fi

output_dir=$(dirname "$output")
mkdir -p "$output_dir"
tmp=$(mktemp "$output_dir/.primary_lens_rates.XXXXXX")
trap 'rm -f "$tmp"' EXIT

{
echo "ID_src l_src b_src fa_l_src fa_b_src sa_src file_src ID_lens l_lens b_lens fa_l_lens fa_b_lens sa_lens file_lens nsource source_area nlens lens_area tau tEmean murelmean nevents_per_tile nevents_per_source nevents_per_deg2 source_density"

python3 - "$sources_list" "$lenses_list" << 'PY' | while read -r sidx sl sb sdl sdb ssa sfile lidx ll lb ldl ldb lsa lfile src_abs lens_abs; do
import os
import sys

src_path, lens_path = sys.argv[1], sys.argv[2]
# Field grid is 0.2 deg. 1e-3 deg absorbs index formatting (-0.2 vs -0.200)
# and does not reach the next pointing.
tol = 1e-3

def load(path):
    rows = []
    with open(path) as handle:
        for lineno, line in enumerate(handle, 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 7:
                sys.exit("%s:%d: expected id l b dl db solid_angle file" % (path, lineno))
            rows.append(parts[:7] + [float(parts[1]), float(parts[2])])
    return rows

sources = load(src_path)
lenses = load(lens_path)
src_dir = os.path.dirname(os.path.abspath(src_path))
lens_dir = os.path.dirname(os.path.abspath(lens_path))

def resolve(directory, name):
    if os.path.isabs(name):
        return name
    return os.path.join(directory, name)

n_skip = 0
n_match = 0
used = set()
for src in sources:
    hits = [
        i for i, lens in enumerate(lenses)
        if abs(src[7] - lens[7]) <= tol and abs(src[8] - lens[8]) <= tol
    ]
    if len(hits) != 1:
        sys.stderr.write(
            "run_rates_primary_lens.sh: field %s l=%s b=%s matched %d lens fields\n"
            % (src[0], src[1], src[2], len(hits))
        )
        sys.exit(1)
    i = hits[0]
    if i in used:
        sys.stderr.write("run_rates_primary_lens.sh: lens field %s matched more than once\n" % lenses[i][0])
        sys.exit(1)
    used.add(i)
    lens = lenses[i]
    src_file = resolve(src_dir, src[6])
    lens_file = resolve(lens_dir, lens[6])
    if not (os.path.isfile(src_file) and os.path.isfile(lens_file)):
        n_skip += 1
        continue
    n_match += 1
    sys.stdout.write(" ".join(src[:7] + lens[:7] + [src_file, lens_file]) + "\n")

sys.stderr.write(
    "run_rates_primary_lens.sh: %d field pair(s) with catalogs, %d skipped (missing csv), %d source fields, %d lens fields\n"
    % (n_match, n_skip, len(sources), len(lenses))
)
if n_match == 0:
    sys.exit(3)
PY
	rates=$("$python_bin" "$calc_rate" "$src_abs" "$ssa" "$lens_abs" "$lsa" </dev/null)
	printf '%s %s\n' "$sidx $sl $sb $sdl $sdb $ssa $sfile $lidx $ll $lb $ldl $ldb $lsa $lfile" "$rates"
done
} > "$tmp"

if [[ -e "$output" ]]; then
	echo "run_rates_primary_lens.sh: refusing to overwrite $output" >&2
	exit 1
fi
if ! ln "$tmp" "$output"; then
	if [[ -e "$output" ]]; then
		echo "run_rates_primary_lens.sh: refusing to overwrite $output" >&2
	else
		echo "run_rates_primary_lens.sh: could not create $output" >&2
	fi
	exit 1
fi
rm -f "$tmp"
trap - EXIT
echo "run_rates_primary_lens.sh: wrote $output" >&2
