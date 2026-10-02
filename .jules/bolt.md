## 2026-10-02 - Avoid numpy.exp for single scalar operations
**Learning:** Using `numpy.exp` inside list comprehensions or loops for scalar values (like in the reranker sigmoid function) incurs a significant Python-to-C overhead. A benchmark showed `math.exp` is ~7x faster for scalar values (0.16s vs 1.17s for 1M calls).
**Action:** Replace `numpy.exp` with standard `math.exp` (wrapped in try/except OverflowError) for single scalar operations in hot paths.
