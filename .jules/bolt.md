## 2026-10-24 - Math.exp vs Numpy.exp

**Learning:** Numpy.exp carries an extremely high C-call overhead when used to process scalars in tight loops (such as mapping over items). In `hindsight_api/engine/search/reranking.py`, the `_sigmoid` function was using `np.exp` inside a list comprehension, which can be up to 5 times slower than `math.exp`. Note that `math.exp` may raise `OverflowError`, while `np.exp` returns 0.0 or inf instead, so wrapping `math.exp` with a try-except block is crucial.
**Action:** Always prefer standard library functions like `math.exp` in Python hot loops when operating on scalars instead of numpy.
