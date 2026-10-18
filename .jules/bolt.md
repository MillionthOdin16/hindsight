## 2026-05-18 - Avoid numpy.exp for scalar operations in hot paths
**Learning:** In `hindsight-api-slim/hindsight_api/engine/search/reranking.py`, an inline import of `numpy` and use of `np.exp` was found for a simple scalar sigmoid calculation during reranking. This introduces significant Python-to-C overhead and inline import penalty.
**Action:** Replace `numpy.exp` with `math.exp` (wrapped in a `try/except OverflowError` block to handle large negative logits like numpy does) for single scalar operations in hot paths to avoid overhead.
