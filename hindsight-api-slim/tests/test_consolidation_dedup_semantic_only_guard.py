"""Protect semantic-only observation dedup against unwanted BM25 work."""
import ast
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'hindsight_api/engine/consolidation/consolidator.py'


class DedupSearchArmsTest(unittest.TestCase):
    def test_observation_dedup_disables_unused_bm25_arm(self):
        tree = ast.parse(SOURCE.read_text())
        funcs = [n for n in ast.walk(tree) if isinstance(n, ast.AsyncFunctionDef) and n.name == '_dedup_adjudicate']
        self.assertEqual(len(funcs), 1)
        calls = [n for n in ast.walk(funcs[0]) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'recall_unified']
        self.assertEqual(len(calls), 1)
        kws = {k.arg: k.value for k in calls[0].keywords}
        self.assertIn('enable_text_search', kws)
        self.assertIsInstance(kws['enable_text_search'], ast.Constant)
        self.assertIs(kws['enable_text_search'].value, False)
        self.assertIn('enable_graph', kws)
        self.assertIs(kws['enable_graph'].value, False)
        source = ast.get_source_segment(SOURCE.read_text(), funcs[0])
        self.assertIn('grouped["observation"].semantic', source)

if __name__ == '__main__':
    unittest.main()
