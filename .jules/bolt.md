## 2026-08-30 - Scalar Math Optimization
**Learning:** In Python hot paths, using `numpy.exp` for single scalar operations introduces significant Python-to-C conversion overhead. Inline imports also add overhead.
**Action:** Use standard library `math.exp` instead for scalar operations, and handle `OverflowError` explicitly since `math.exp` doesn't automatically return 0.0/inf like numpy.
