## 2026-07-27 - Replacing np.exp with math.exp in Python Hot Paths
**Learning:** For scalar values in tight loops, math.exp is ~9x faster than np.exp because it avoids Python-to-C type conversions and numpy overhead. However, math.exp raises OverflowError on large negative inputs, whereas np.exp returns 0.0 or inf without throwing an exception.
**Action:** When replacing np.exp with math.exp for scalar values, ensure the math.exp call is wrapped in a try/except OverflowError block, returning 0.0 (or appropriate boundary value) to mimic numpy's behavior safely.
