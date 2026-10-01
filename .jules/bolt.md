## 2026-07-20 - Scalar Exp Optimization
**Learning:** For scalar values in Python, the standard library `math.exp()` is significantly faster (~7x) than `numpy.exp()`, but `math.exp` raises an `OverflowError` for large negative inputs instead of safely returning `0.0` or `inf` like numpy does.
**Action:** When replacing `numpy.exp` with `math.exp` to optimize scalar operations, always wrap the math operation in a `try/except OverflowError` block.
