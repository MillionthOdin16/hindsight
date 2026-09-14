## 2026-09-14 - Replace numpy.exp with math.exp for scalar sigmoid in reranking
**Learning:** Using `numpy.exp` for scalar operations in Python hot paths (like reranking scoring loops) introduces significant overhead due to Python-to-C conversion.
**Action:** Always prefer `math.exp` over `numpy.exp` for single scalar operations. When switching to `math.exp`, ensure to catch `OverflowError` for large negative exponents which `numpy` handles silently by returning `0.0` or `inf`.
