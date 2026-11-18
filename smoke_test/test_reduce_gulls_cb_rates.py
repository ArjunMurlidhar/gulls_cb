"""Unit checks for NaN nevents_per_tile handling in reduce_gulls_cb."""
import importlib.util
import os
import sys
import tempfile
import unittest

import pandas as pd


def load_reduce_gulls_cb():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    script = os.path.join(repo_root, 'scripts', 'reduce_gulls_cb.py')
    spec = importlib.util.spec_from_file_location('reduce_gulls_cb', script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class TestRatesNanDrop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_reduce_gulls_cb()

    def test_load_rates_catalog_drops_nan_rows(self):
        contents = (
            'ID_src l_src b_src nevents_per_tile\n'
            '1 0.1 0.2 10.0\n'
            '2 0.3 0.4 nan\n'
            '3 0.5 0.6 5.0\n'
        )
        with tempfile.NamedTemporaryFile(mode='w', suffix='.rates', delete=False) as handle:
            handle.write(contents)
            path = handle.name
        try:
            rates, dropped = self.mod.load_rates_catalog(path)
        finally:
            os.unlink(path)
        self.assertEqual(dropped, [2])
        self.assertEqual(sorted(int(x) for x in rates.index), [1, 3])
        self.assertFalse(rates['nevents_per_tile'].isna().any())

    def test_filter_dropped_field_events(self):
        frames = [
            pd.DataFrame({'Field': [1, 2, 2], 'raw_weight': [1.0, 2.0, 3.0]}),
        ]
        kept = self.mod.filter_dropped_field_events(frames, [2])
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0]['Field'].tolist(), [1])

    def test_fields_missing_excludes_dropped_only_after_filter(self):
        rates_index = pd.Index([1, 3], name='ID_src')
        rates = pd.DataFrame({'nevents_per_tile': [10.0, 5.0]}, index=rates_index)
        frames = [pd.DataFrame({'Field': [1, 3], 'raw_weight': [1.0, 1.0]})]
        missing = self.mod.fields_missing_from_rates(frames, rates)
        self.assertEqual(missing, [])
        frames_bad = [pd.DataFrame({'Field': [99], 'raw_weight': [1.0]})]
        missing = self.mod.fields_missing_from_rates(frames_bad, rates)
        self.assertEqual(missing, [99])


if __name__ == '__main__':
    unittest.main()