## 2026-07-28 - Optimize cross-encoder reranker sigmoid
**Learning:** Found an inline import of `numpy` inside `CrossEncoderReranker.rerank` just to calculate a single scalar sigmoid (`1 / (1 + np.exp(-x))`). For scalar operations in Python hot paths, standard library `math.exp` is much faster than `numpy.exp` due to the lack of Python-to-C conversion overhead.
**Action:** Replace `numpy.exp` with `math.exp` with overflow handling in scalar math calculations to avoid numpy overhead.
