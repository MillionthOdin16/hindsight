## 2026-06-15 - Optimizing scalar operations in Python
**Learning:** For scalar operations (like single values in a loop), `math.exp` is significantly faster than `numpy.exp` due to the overhead of converting Python floats to C types and back. `numpy.exp` is optimized for array operations, not single scalar evaluations.
**Action:** Replace `numpy.exp` with `math.exp` (wrapped in a try/except OverflowError block) in loops or list comprehensions where single scalar values are processed, such as in `hindsight_api/engine/search/reranking.py`.
