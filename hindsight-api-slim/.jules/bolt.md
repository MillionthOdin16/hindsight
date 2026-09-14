## 2026-03-08 - Use math.exp instead of numpy.exp for scalar operations
**Learning:** Python-to-C conversion overhead makes `numpy.exp` significantly slower than `math.exp` for scalar operations in tight loops (e.g., normalization logic in `reranking.py`). Benchmarks show it is ~6x faster.
**Action:** When performing scalar mathematical operations like sigmoid normalization in hot paths, avoid `numpy` and use `math`. Since `math.exp` raises an `OverflowError` for large negative inputs rather than returning 0.0 like `numpy.exp`, wrap the calculation in a `try/except OverflowError` block.
