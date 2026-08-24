## 2026-07-27 - Inline import of numpy for scalar operations
**Learning:** Using `import numpy as np` inline and `np.exp` for single scalar operations introduces significant overhead due to Python-to-C context switching and import overhead, especially in hot paths like reranking scoring loops.
**Action:** Replace `np.exp` with `math.exp` for scalar values, but ensure it is wrapped in a `try/except OverflowError` block because `math.exp` throws an exception on overflow (large positive inputs) while numpy handles it gracefully.
