## 2026-09-21 - [Backend] Replaced numpy.exp with math.exp in hot path
**Learning:** In python hot paths, using `numpy.exp` on scalar values incurs a high Python-to-C overhead which slows down the operation compared to the standard library `math.exp`.
**Action:** Always prefer standard library functions like `math.exp` over `numpy` for scalar operations.
