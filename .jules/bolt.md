## 2026-07-28 - Replace numpy.exp with math.exp for scalar operations
**Learning:** Using `numpy.exp` for single scalar operations introduces Python-to-C conversion overhead. Inline imports of `numpy` inside hot paths (e.g., scoring loops) add overhead.
**Action:** Replace `numpy.exp` with `math.exp` for scalar operations in hot paths. Wrap it in a `try/except OverflowError` block because `math.exp` raises an exception for highly negative values, whereas `numpy.exp` silently handles it by returning 0.0 or inf.
