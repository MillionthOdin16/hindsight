## 2026-05-18 - Avoid numpy.exp for scalar operations
**Learning:** Using `numpy.exp` for single scalar values incurs significant overhead due to Python-to-C conversion.
**Action:** Use `math.exp` with a `try/except OverflowError` block instead for scalar operations in hot paths.
