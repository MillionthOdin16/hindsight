## 2026-03-24 - Python Hot Path Optimizations
**Learning:** For single scalar operations in hot paths (like calculating a sigmoid over individual scores), using `math.exp` instead of `numpy.exp` avoids significant Python-to-C API overhead and is noticeably faster (e.g. ~6.5x speedup), but requires handling `OverflowError` appropriately.
**Action:** Replace inline `import numpy as np` and `np.exp` with standard `math.exp` with try/except blocks on single-value computations in performance-critical sections like reranking algorithms.
