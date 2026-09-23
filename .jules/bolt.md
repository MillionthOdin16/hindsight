## 2026-09-23 - Python-to-C Overhead in Hot Paths
**Learning:** For scalar operations in hot paths like reranking score normalization, using `numpy.exp` introduces significant Python-to-C overhead. A simple `math.exp` is much faster for single floats.
**Action:** Replace `numpy.exp` with `math.exp` wrapped in a `try/except OverflowError` block for scalar operations to avoid this overhead without losing overflow protection.
