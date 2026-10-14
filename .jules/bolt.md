## 2026-05-18 - Avoid numpy.exp for simple scalar operations
**Learning:** In hot paths like scoring functions, `numpy.exp` has significant overhead for simple scalar inputs due to Python-to-C API conversions and internal dispatch checks.
**Action:** Use Python's built-in `math.exp` instead for simple scalar operations to improve performance. Use `try/except OverflowError` as `math.exp` throws an error on overflow/underflow whereas `numpy.exp` handles it.
