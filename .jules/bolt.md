## 2026-07-27 - [Replacing np.exp with math.exp for scalar values]
**Learning:** For scalar values, `math.exp` is significantly faster than `np.exp` because it avoids the overhead of converting between Python floats and numpy arrays.
**Action:** When replacing `np.exp` with `math.exp`, explicitly import `math` and add a `try/except OverflowError` block because `math.exp` raises an exception for large inputs (e.g., highly negative values resulting in positive infinity), whereas `numpy.exp` handles this by returning 0.0 or inf.
