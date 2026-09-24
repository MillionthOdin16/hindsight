## 2026-09-24 - Python math.exp over numpy.exp for scalar operations
**Learning:** For scalar values, `math.exp` is significantly faster than `numpy.exp` because it avoids Python-to-C conversion overhead. However, `math.exp` can raise `OverflowError` for large negative inputs where `numpy.exp` handles it natively.
**Action:** Use `math.exp` with a `try/except OverflowError` block when calculating sigmoid or similar scalar exponential functions in hot loops or loops over scalar lists in Python, instead of importing and using `numpy.exp`.
