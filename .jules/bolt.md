## 2026-07-27 - [Replace numpy.exp with math.exp for sigmoid]
**Learning:** In Python hot paths (like score normalization in `hindsight_api/engine/search/reranking.py`), using `numpy.exp` for single scalar operations incurs significant Python-to-C conversion overhead. Using `math.exp` is much faster but requires explicit `try/except OverflowError` handling since `math.exp` throws on large negative values where `numpy.exp` handles it gracefully.
**Action:** Always prefer `math.exp` over `numpy.exp` for scalar operations in hot loops, and wrap it in a `try/except OverflowError` block.
