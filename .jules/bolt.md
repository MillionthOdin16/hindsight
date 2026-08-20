## 2026-08-20 - Scalar Exp Ops are slower with NumPy
**Learning:** For scalar ops like single float exponentiation (in hot loops/paths like reranking), `numpy.exp` incurs significant Python-to-C translation overhead compared to `math.exp`.
**Action:** Replace `numpy.exp` with `math.exp` wrapped in a `try/except OverflowError` in single-value mathematical routines where possible.
