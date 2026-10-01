## 2026-05-18 - Avoid numpy for scalar math operations
**Learning:** For Python scalar operations in hot paths, standard library methods (`math.exp`) are significantly faster than NumPy equivalents (`numpy.exp`) by avoiding Python-to-C conversion overhead, though they require explicit `OverflowError` handling.
**Action:** When working on scalar hot paths, prefer `math` over `numpy` and ensure edge cases (e.g., overflows yielding 0.0 or inf) are safely caught.
