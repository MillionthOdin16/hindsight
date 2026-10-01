## 2026-11-20 - Fast Sigmoid Activation
**Learning:** Replaced `numpy.exp` with `math.exp` inside the cross-encoder sigmoid function in `hindsight_api/engine/search/reranking.py`. This avoids heavy Python-to-C API overhead for scalar operations, speeding up evaluation by ~4x.
**Action:** Always prefer standard library `math` module over `numpy` or `torch` when processing single scalar values in hot loops.
