"""Protect the legacy proxy-offline 1024 fallback and reject wrong-width vectors."""
import ast
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'hindsight_api/engine/embeddings.py'
class FallbackGuardTest(unittest.TestCase):
    def test_offline_fallback_requires_actual_width_validation(self):
        src=SOURCE.read_text(); t=ast.parse(src)
        cls=next(n for n in t.body if isinstance(n,ast.ClassDef) and n.name=='LiteLLMEmbeddings')
        methods={n.name:n for n in cls.body if isinstance(n,(ast.AsyncFunctionDef,ast.FunctionDef))}
        self.assertIn('initialize',methods)
        self.assertIn('_check_declared_dimension',methods)
        init=ast.get_source_segment(src,methods['initialize'])
        guard=ast.get_source_segment(src,methods['_check_declared_dimension'])
        self.assertIn('self._legacy_fallback_used = True',init)
        self.assertIn('self._dimension = 1024',init)
        self.assertIn('if actual != expected:',guard)
        self.assertIn('self._dimension_verified = True',guard)
        self.assertLess(guard.index('if actual != expected:'),guard.index('self._dimension_verified = True'))

if __name__ == '__main__':unittest.main()
