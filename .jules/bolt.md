## 2026-06-15 - Replace numpy.exp with math.exp for scalar operations
**Learning:** For performance optimizations in Python hot paths, using `numpy.exp` for single scalar operations introduces Python-to-C conversion overhead. Using `math.exp` is significantly faster but differs in behavior for large inputs (it raises `OverflowError` instead of returning 0.0 or inf).
**Action:** Replace `numpy.exp` with `math.exp` wrapped in a `try/except OverflowError` block (handling `inf` or `0.0` depending on the sign of the input) when operating on single scalar values.
