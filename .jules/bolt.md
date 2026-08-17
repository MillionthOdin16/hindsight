## 2026-05-15 - [Python Scalar Math Optimization]
**Learning:** For scalar mathematical operations like sigmoid inside python hot loops or list comprehensions, standard library `math.exp` is significantly faster than `numpy.exp` due to avoiding python-to-C and array conversion overhead.
**Action:** Replace `numpy.exp` with `math.exp` in `_sigmoid` in `hindsight_api/engine/search/reranking.py`. Ensure to catch `OverflowError` for large magnitude negative values, or return 0.0 or 1.0 depending on the sign of x. Remove `import numpy as np` from the local scope.
