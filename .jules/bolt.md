## 2026-09-16 - Math over Numpy for scalar sigmoid

**Learning:** `np.exp` in Python list comprehensions introduces significant overhead because of implicit C extension boundary crossing and generic type dispatch on single scalar float values.

**Action:** Replace `np.exp` with `math.exp` wrapped in a `try...except OverflowError` block (returning 0.0 for x<0, 1.0 for x>=0 to match np.exp behavior for large/small numbers) in hot loops for list comprehensions where single scalar operations are performed.
