## 2026-07-11 - Replace `np.exp` with `math.exp` in single scalar operations
**Learning:** Python-to-C conversion overhead makes numpy functions significantly slower than standard math functions for single scalar operations. `math.exp` is ~10x faster than `numpy.exp` when acting on a single float.
**Action:** Always prefer `math` library functions (like `math.exp`) over `numpy` equivalents when operating on single scalar values in Python hot paths.
