## 2026-07-25 - Avoid numpy.exp for scalar operations
**Learning:** Using numpy.exp for single scalar operations introduces significant Python-to-C conversion overhead and often involves inline imports which are slow.
**Action:** Use the standard library math.exp for scalar operations instead. Make sure to wrap it in a `try/except OverflowError` block since math.exp raises an exception for large inputs unlike numpy.exp which returns 0.0 or inf.
