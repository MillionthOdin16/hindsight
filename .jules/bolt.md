## 2026-08-11 - Replace numpy.exp with math.exp
**Learning:** In python hot paths, using `math.exp` is much faster for single scalar operations than `numpy.exp` because it prevents Python-to-C conversion overhead. `numpy.exp` handles overflow by returning inf, while `math.exp` raises an `OverflowError`. This can be caught and handled with `try/except OverflowError` to return 0.0.
**Action:** Use `math.exp` and `try/except OverflowError` block instead of `numpy.exp` when optimizing scalar operations in python.
