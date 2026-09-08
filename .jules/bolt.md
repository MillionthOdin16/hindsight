## 2026-07-27 - Replace np.exp with math.exp in scalar loops
**Learning:** Using `numpy.exp()` for single scalar values inside a loop has significant overhead due to Python-to-C type conversion. The built-in `math.exp()` is about ~10x faster for single scalar values.
**Action:** When performing scalar mathematical operations in a Python hot path, use the standard library `math` module instead of `numpy`. Be sure to catch `OverflowError` as `math.exp` raises it for large negative numbers, unlike `numpy.exp` which returns `0.0`.
