## 2026-08-31 - Replace numpy.exp with math.exp for scalar operations
**Learning:** In Python hot paths, using `numpy.exp` for single scalar operations incurs significant Python-to-C conversion and inline import overhead.
**Action:** Always prefer standard library `math.exp` for scalar operations and wrap it in a `try/except OverflowError` block to handle large inputs gracefully (unlike `numpy.exp` which returns 0.0 or inf implicitly).
