
## 2026-10-27 - Fast Sigmoid Calculation
**Learning:** In Python hot paths, computing scalar math operations using `numpy` (like `numpy.exp` in a list comprehension) is surprisingly slow due to Python-to-C overhead. For single values, standard library `math.exp` is much faster.
**Action:** Replace `numpy.exp` with `math.exp` for scalar operations in hot paths, wrapping in a `try/except OverflowError` to safely handle large inputs.
