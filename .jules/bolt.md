## 2026-07-29 - Python-to-C Overhead with numpy
**Learning:** For scalar operations in hot paths, using standard library functions like `math.exp` avoids the Python-to-C conversion overhead associated with `numpy.exp`. However, `math.exp` raises an `OverflowError` for large inputs, so it must be wrapped in a `try/except` block to replicate `numpy`'s behavior (returning 0.0 or inf).
**Action:** Always prefer standard library functions over heavy dependencies for single scalar operations.
