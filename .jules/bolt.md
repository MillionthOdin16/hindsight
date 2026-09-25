## 2026-03-02 - Python to C++ math overhead
**Learning:** In highly called internal Python functions, using `math.exp` instead of `numpy.exp` on scalar values can significantly improve performance (10x faster) by avoiding the overhead of converting between Python scalar types and numpy C++ arrays for a single value.
**Action:** Replace `numpy.exp` with `math.exp` for scalar operations in performance-sensitive areas, but wrap it in a `try/except OverflowError` since `math.exp` raises errors on large values while `numpy` returns limits (0.0 or inf).
