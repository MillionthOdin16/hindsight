## 2026-06-15 - Python math vs numpy for scalars
**Learning:** For single scalar operations in hot paths, using standard library `math.exp` is significantly faster (~5x) than `numpy.exp`, which carries extra overhead. Also, an inline import of numpy within a loop adds unnecessary overhead compared to importing it at the module level.
**Action:** Replace `numpy.exp` with `math.exp` with a `try/except OverflowError` block for scalar operations where performance is critical. Remove inline imports.
