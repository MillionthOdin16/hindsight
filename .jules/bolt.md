## 2026-07-27 - [Replace numpy.exp with math.exp]
**Learning:** Using numpy.exp for scalar operations in a loop introduces significant overhead due to Python-to-C conversion and object instantiation compared to the standard library's math.exp.
**Action:** Replace `np.exp` with `math.exp` inside `hindsight_api/engine/search/reranking.py` for scalar values and ensure a `try...except OverflowError` block is used to gracefully handle large negative numbers as 0.0 (mirroring `np.exp` behavior), as `math.exp` raises an error instead of returning 0.0 or inf.
