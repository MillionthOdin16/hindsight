## 2026-10-15 - [Python Scalar Math Optimization]
**Learning:** For single scalar operations like `exp`, Python's built-in `math.exp` is significantly faster (~5.5x) than `numpy.exp` due to the overhead of Python-to-C conversion for NumPy arrays.
**Action:** When performing scalar mathematical operations in a loop or hot path, prefer `math` over `numpy` if vectorized operations over arrays are not being used. Add `try/except OverflowError` block to match NumPy's behaviour of returning 0.0 for large negative exponents.
