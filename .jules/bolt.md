## 2026-03-02 - Replace numpy.exp with math.exp in hot path
**Learning:** In the cross-encoder score normalization logic, `numpy` is imported inline and `np.exp` is used for single scalar operations. This introduces a heavy import overhead during the hot path of search queries, as well as the Python-to-C conversion overhead from calling `numpy` functions on individual scalars instead of vectorized arrays.
**Action:** Replace `import numpy as np` with `math.exp` wrapped in a `try/except OverflowError` block. This avoids the heavy import and significantly speeds up scalar calculations.
