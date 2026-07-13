## 2026-07-13 - [Python Hot Paths Optimization]
**Learning:** Using `numpy.exp` for scalar operations in a hot loop incurs a significant Python-to-C conversion overhead.
**Action:** Replace `numpy.exp` with `math.exp` for single scalar operations. Make sure to wrap `math.exp` in a `try/except OverflowError` block because it raises an exception for large inputs (e.g., highly negative values resulting in positive infinity), whereas `numpy.exp` handles this by returning 0.0 or inf.
