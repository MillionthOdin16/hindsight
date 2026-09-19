## 2026-07-02 - Python-to-C overhead in tight loops
**Learning:** For scalar operations in hot paths like `_sigmoid(x)`, `math.exp` is significantly faster than `numpy.exp` due to the overhead of converting Python scalars to C and back in NumPy.
**Action:** Replace `numpy.exp` with `math.exp` (wrapped in a try-except for OverflowError) for single scalar operations.
