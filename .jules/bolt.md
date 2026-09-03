## 2026-07-28 - Optimize sigmoid function with math.exp
**Learning:** Replaced numpy's exp with standard library math.exp in `hindsight_api/engine/search/reranking.py` since math.exp is faster for scalar calculations due to the lack of Python-to-C overhead.
**Action:** Use math.exp wrapped in a try/except OverflowError block for scalar exponential calculations instead of numpy.exp.
