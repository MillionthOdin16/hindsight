## 2026-07-28 - Replace numpy.exp with math.exp in cross-encoder sigmoid

**Learning:** In `hindsight-api-slim/hindsight_api/engine/search/reranking.py`, the `_sigmoid` function uses `numpy.exp` to calculate the exponential. For single scalar operations, `math.exp` is significantly faster than `numpy.exp` because it avoids the overhead of converting Python floats to C types and back. However, `math.exp` can raise an `OverflowError` for large inputs (e.g., highly negative values resulting in positive infinity), whereas `numpy.exp` handles this by returning 0.0 or inf.

**Action:** Replace `numpy.exp` with `math.exp` in the `_sigmoid` function. Wrap the call in a `try/except OverflowError` block. If an `OverflowError` is raised, return `0.0` (since `1 / (1 + inf) == 0.0`). Ensure `math` is imported and `numpy` is safely removed from the local scope.
