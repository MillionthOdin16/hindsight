## 2026-08-11 - Python Scalar Math Optimization
**Learning:** Using `numpy.exp` for single scalar operations inside a loop introduces massive Python-to-C conversion overhead, taking ~4x longer than `math.exp` (or ~15x slower with inline imports).
**Action:** Always prefer standard library `math` module (e.g. `math.exp`) over `numpy` when computing scalar values one by one in hot loops like reranking. Wrap `math.exp` in a `try/except OverflowError` block because it raises an exception on large inputs, unlike `numpy.exp` which safely handles infinity.
