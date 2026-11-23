"""Primary-lens-only norm and weights for the reducer and rate copies.

Does not run a gulls simulation or the production rates job. Toy catalogs
and in-memory frames only.
"""
import importlib.util
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest

import pandas as pd


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def load_script(name):
    script = os.path.join(REPO_ROOT, 'scripts', name)
    spec = importlib.util.spec_from_file_location(name.replace('.py', ''), script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def event_frame():
    """One single, one primary, one companion, and one source-id mismatch.

    The source IDs differ on the single so a source filter would zero it.
    The companion is the only row with Lens_ID != Lens_primary_ID.
    """
    return pd.DataFrame({
        'Field': [1, 1, 1],
        'raw_weight': [4.0, 6.0, 3.0],
        'weight': [4.0, 6.0, 3.0],
        'Lens_ID': [10, 20, 30],
        'Lens_primary_ID': [10, 10, 30],
        'Source_ID': [1, 2, 3],
        'Source_primary_ID': [9, 2, 3],
        'ObsGroup_0_chi2_bin': [100.0, 100.0, 80.0],
        'ObsGroup_0_chi2_pl': [0.0, 0.0, 0.0],
        'ObsGroup_0_flatchi2_bin': [1.0, 1.0, 1.0],
        'ObsGroup_0_flatchi2_pl': [0.0, 0.0, 0.0],
    })


class TestPrimaryLensWeights(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_script('reduce_gulls_cb_primary_lens.py')

    def test_norm_excludes_secondary_even_before_zeroing(self):
        data = event_frame()
        rates = pd.DataFrame(
            {'nevents_per_tile': [10.0]},
            index=pd.Index([1], name='ID_src'),
        )
        rates = self.mod.accumulate_norms([data], rates)
        # 4 + 3, not 4 + 6 + 3. The companion raw_weight is not in the norm.
        self.assertAlmostEqual(float(rates.loc[1, 'norm']), 7.0)
        self.assertEqual(data['raw_weight'].tolist(), [4.0, 6.0, 3.0])
        self.assertEqual(data['Source_ID'].tolist(), [1, 2, 3])

    def test_secondary_weights_are_zero_and_do_not_enter_rates(self):
        data = event_frame()
        rates = pd.DataFrame(
            {'nevents_per_tile': [10.0]},
            index=pd.Index([1], name='ID_src'),
        )
        zeroed = self.mod.zero_secondary_lens_weights(data)
        self.assertEqual(zeroed['raw_weight'].tolist(), [4.0, 0.0, 3.0])
        self.assertEqual(zeroed['weight'].tolist(), [4.0, 0.0, 3.0])
        self.assertEqual(zeroed['Source_ID'].tolist(), [1, 2, 3])
        self.assertEqual(zeroed['Source_primary_ID'].tolist(), [9, 2, 3])

        rates = self.mod.accumulate_norms([zeroed], rates)
        self.assertAlmostEqual(float(rates.loc[1, 'norm']), 7.0)
        prepared, rates = self.mod.prepare_frames([zeroed], rates, False, 432.0)
        out = prepared[0]
        # final_weight = (10 / 7) * weight. Companion weight is 0.
        self.assertAlmostEqual(float(out.loc[0, 'final_weight']), 10.0 * 4.0 / 7.0)
        self.assertAlmostEqual(float(out.loc[2, 'final_weight']), 10.0 * 3.0 / 7.0)
        self.assertEqual(float(out.loc[1, 'final_weight']), 0.0)
        self.assertEqual(float(out.loc[1, 'norm_weight']), 0.0)
        self.assertEqual(float(out.loc[1, 'raw_weight']), 0.0)
        self.assertEqual(float(out.loc[1, 'weight']), 0.0)
        self.assertAlmostEqual(float(out.loc[0, 'norm_weight']), 4.0 / 7.0)
        self.assertEqual(out['Source_ID'].tolist(), [1, 2, 3])
        self.assertEqual(out['Source_primary_ID'].tolist(), [9, 2, 3])
        self.assertAlmostEqual(float(rates.loc[1, 'final_rate']), 10.0)

        stable = out.loc[self.mod.stable_mask(out, 1)]
        self.assertEqual(len(stable), 3)
        detrates = rates.copy()
        detrates['stable_final_weight_sum'] = 0.0
        detrates['stable_norm_weight_sum'] = 0.0
        detrates['ObsGroup_Roman_final_rate'] = 0.0
        detrates['ObsGroup_Roman_final_rate_err2'] = 0.0
        self.mod.add_field_sums(detrates, stable, 'final_weight', 'stable_final_weight_sum')
        self.mod.add_field_sums(detrates, stable, 'norm_weight', 'stable_norm_weight_sum')
        self.assertAlmostEqual(float(detrates.loc[1, 'stable_final_weight_sum']), 10.0)
        self.assertAlmostEqual(float(detrates.loc[1, 'stable_norm_weight_sum']), 1.0)
        detected = self.mod.detection_frame(out, 0, 50.0)
        self.assertEqual(len(detected), 3)
        self.mod.add_field_sums(
            detrates, detected, 'final_weight',
            'ObsGroup_Roman_final_rate', 'ObsGroup_Roman_final_rate_err2',
        )
        self.assertAlmostEqual(float(detrates.loc[1, 'ObsGroup_Roman_final_rate']), 10.0)

    def test_bad_weights_cannot_restore_a_secondary(self):
        data = event_frame()
        data['Planet_q'] = 1.0
        data['u0max'] = 1.0
        data['tE_ref'] = [1.0, 0.0, 1.0]
        data['tE_helio'] = 1.0
        rates = pd.DataFrame(
            {'nevents_per_tile': [7.0]},
            index=pd.Index([1], name='ID_src'),
        )
        zeroed = self.mod.zero_secondary_lens_weights(data, announce=False)
        rates = self.mod.accumulate_norms([zeroed], rates)
        prepared, rates = self.mod.prepare_frames([zeroed], rates, True, 365.25)
        out = prepared[0]
        self.assertEqual(float(out.loc[1, 'weight']), 0.0)
        self.assertEqual(float(out.loc[1, 'final_weight']), 0.0)
        self.assertFalse(out['final_weight'].isna().any())
        self.assertAlmostEqual(float(rates.loc[1, 'final_rate']), 7.0)

    def test_field_of_only_secondaries_has_zero_norm(self):
        data = pd.DataFrame({
            'Field': [2],
            'raw_weight': [5.0],
            'weight': [5.0],
            'Lens_ID': [8],
            'Lens_primary_ID': [3],
        })
        rates = pd.DataFrame(
            {'nevents_per_tile': [10.0]},
            index=pd.Index([2], name='ID_src'),
        )
        zeroed = self.mod.zero_secondary_lens_weights(data, announce=False)
        rates = self.mod.accumulate_norms([zeroed], rates)
        self.assertEqual(float(rates.loc[2, 'norm']), 0.0)
        prepared, rates = self.mod.prepare_frames([zeroed], rates, False, 432.0)
        out = prepared[0]
        self.assertEqual(float(out.loc[0, 'final_weight']), 0.0)
        self.assertEqual(float(out.loc[0, 'norm_weight']), 0.0)
        self.assertEqual(float(rates.loc[2, 'final_rate']), 0.0)

    def test_missing_lens_id_column_exits(self):
        data = pd.DataFrame({
            'raw_weight': [1.0],
            'weight': [1.0],
            'Lens_ID': [1],
        })
        with self.assertRaises(SystemExit):
            self.mod.primary_lens_mask(data)


class TestPrimaryLensRates(unittest.TestCase):
    def test_rate_sum_drops_companions_and_keeps_dark_sources(self):
        """Companion rows leave the sum. Dark sources and dark primaries stay.

        Compared against calc_rate.py on the same catalogs with the companion
        already removed, so the rest of the calculation is unchanged.
        """
        sources = textwrap.dedent("""\
            Dist mul mub R062
            2.0 0.0 0.0 10
            3.0 0.2 -0.1 99
            """)
        lenses_with_companion = textwrap.dedent("""\
            Dist mul mub Mass ID primary_ID Is_Binary R062
            0.5 1.0 0.0 0.5 1 1 0 10
            0.4 5.0 0.0 3.0 2 1 2 99
            0.8 -1.0 0.5 0.2 3 3 1 99
            """)
        lenses_kept = textwrap.dedent("""\
            Dist mul mub Mass
            0.5 1.0 0.0 0.5
            0.8 -1.0 0.5 0.2
            """)
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, 'sources.csv')
            lens_all = os.path.join(tmp, 'lenses.csv')
            lens_kept = os.path.join(tmp, 'lenses_kept.csv')
            for path, text in (
                (src, sources),
                (lens_all, lenses_with_companion),
                (lens_kept, lenses_kept),
            ):
                with open(path, 'w') as handle:
                    handle.write(text)
            new = subprocess.run(
                [sys.executable, os.path.join(REPO_ROOT, 'scripts', 'calc_rate_primary_lens.py'),
                 src, '0.04', lens_all, '0.04'],
                check=False, capture_output=True, text=True,
            )
            old = subprocess.run(
                [sys.executable, os.path.join(REPO_ROOT, 'scripts', 'calc_rate.py'),
                 src, '0.04', lens_kept, '0.04'],
                check=False, capture_output=True, text=True,
            )
        self.assertEqual(new.returncode, 0, new.stderr)
        self.assertEqual(old.returncode, 0, old.stderr)
        self.assertEqual(new.stdout, old.stdout)
        self.assertIn('dropped 1 lens row', new.stderr)
        tokens = new.stdout.split()
        self.assertEqual(tokens[0], '2')
        self.assertEqual(tokens[2], '2')

    def test_shell_copy_skips_missing_csvs_and_calls_primary_script(self):
        sources = textwrap.dedent("""\
            Dist mul mub R062
            2.0 0.1 0.0 99
            """)
        lenses = textwrap.dedent("""\
            Dist mul mub Mass ID primary_ID Is_Binary R062
            0.5 1.0 0.2 0.4 1 1 1 10
            0.5 4.0 0.2 2.0 2 1 2 10
            """)
        with tempfile.TemporaryDirectory() as tmp:
            src_csv = os.path.join(tmp, 'src_present.csv')
            lens_csv = os.path.join(tmp, 'lens_present.csv')
            with open(src_csv, 'w') as handle:
                handle.write(sources)
            with open(lens_csv, 'w') as handle:
                handle.write(lenses)
            src_index = os.path.join(tmp, 'fields.sources')
            lens_index = os.path.join(tmp, 'fields.lenses')
            with open(src_index, 'w') as handle:
                handle.write(
                    '1 1.0 -1.0 0.1 0.1 0.04 src_present.csv\n'
                    '2 2.0 -2.0 0.1 0.1 0.04 src_missing.csv\n'
                )
            with open(lens_index, 'w') as handle:
                handle.write(
                    '10 1.0 -1.0 0.1 0.1 0.04 lens_present.csv\n'
                    '20 2.0 -2.0 0.1 0.1 0.04 lens_missing.csv\n'
                )
            env = os.environ.copy()
            env['PYTHON'] = sys.executable
            result = subprocess.run(
                [os.path.join(REPO_ROOT, 'scripts', 'run_rates_primary_lens.sh'),
                 src_index, lens_index],
                check=False, capture_output=True, text=True, env=env,
            )
            direct = subprocess.run(
                [sys.executable,
                 os.path.join(REPO_ROOT, 'scripts', 'calc_rate_primary_lens.py'),
                 src_csv, '0.04', lens_csv, '0.04'],
                check=False, capture_output=True, text=True,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(direct.returncode, 0, direct.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(len(lines), 2)
        self.assertTrue(lines[0].startswith('ID_src '))
        self.assertIn('src_present.csv', lines[1])
        self.assertNotIn('src_missing.csv', result.stdout)
        self.assertIn('1 skipped (missing csv)', result.stderr)
        self.assertTrue(lines[1].endswith(direct.stdout.strip()))
        # nsource, source_area, nlens follow the lens filename. One companion
        # was dropped, so nlens is 1 and the dark source is still counted.
        fields = lines[1].split()
        self.assertEqual(fields[14], '1')
        self.assertEqual(fields[16], '1')


if __name__ == '__main__':
    unittest.main()
