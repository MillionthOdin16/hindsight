## 2026-10-06 - Replace numpy.exp with math.exp in score normalization

**Learning:** In the `_sigmoid` function of `hindsight_api.engine.search.reranking`, `numpy.exp` is currently used to normalize logits. For single scalar operations, Python-to-C overhead of calling into numpy is significant compared to using the standard library `math.exp`. This overhead can be avoided by making the direct replacement since we are doing scalar list comprehensions rather than vectorizing across a numpy array.

**Action:** Replace `numpy.exp` with `math.exp` within try/except OverflowError block for all single-item calculations inside hot paths like search result reranking.
