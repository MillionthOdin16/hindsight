## 2026-08-21 - [Fast Math in Reranking]
**Learning:** Using `numpy.exp` for scalar operations introduces overhead due to Python-to-C conversion. Replacing it with `math.exp` is faster for scalar calculations like calculating sigmoid functions on individual scores during neural reranking normalization.
**Action:** Replace `numpy.exp` with `math.exp` wrapped in a `try/except OverflowError` block when operating on scalar scores in the cross-encoder reranker hot path.
