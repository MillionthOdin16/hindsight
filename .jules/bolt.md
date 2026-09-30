## 2026-09-30 - Python-to-C overhead for scalar operations
**Learning:** Using numpy.exp for single scalar float operations in a tight loop is significantly slower than using standard library math.exp due to the overhead of Python-to-C type conversions and numpy's array-first design.
**Action:** Replace `numpy.exp` with `math.exp` (wrapped in try/except OverflowError) when performing single scalar exponential calculations in hot paths like reranking scoring.
