## 2026-05-18 - Avoid numpy.exp for scalar operations
**Learning:** In Python, importing and using `numpy.exp` for single scalar values in loops is significantly slower than using standard library `math.exp`. `numpy` has a high Python-to-C overhead for individual elements.
**Action:** When calculating exponentials (like sigmoid) on scalars one by one, always prefer `math.exp(x)` wrapped in a `try/except OverflowError` block.
