## 2026-10-27 - Replace numpy.exp with math.exp in scalar math operations
**Learning:** Using `numpy.exp` on scalar values in a hot path causes Python-to-C conversion overhead. Using standard library `math.exp` eliminates this overhead. However, `math.exp` raises `OverflowError` for large magnitude negative values where `numpy.exp` returns `inf` or `0.0`.
**Action:** When replacing `numpy.exp` with `math.exp` in single scalar operations to prevent Python-to-C conversion overhead, wrap the calculation in a `try/except OverflowError` block.
