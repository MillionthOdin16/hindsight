## 2026-08-01 - Avoid numpy for single scalar operations
**Learning:** In Python hot paths like reranking `_sigmoid`, using `numpy.exp` for single scalar operations introduces significant Python-to-C conversion overhead.
**Action:** Use `math.exp` with a `try/except OverflowError` block (to handle large inputs where numpy just returns inf/0.0) instead of `numpy.exp` for single scalars to get ~10x speedup.
