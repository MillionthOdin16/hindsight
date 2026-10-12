## 2026-05-19 - Use math.exp for scalar sigmoid
**Learning:** In a hot path (like reranking), using `numpy.exp` for single scalar operations introduces a significant Python-to-C conversion overhead. Using `math.exp` (wrapped in try/except for OverflowError handling, unlike numpy which silently handles it) is much faster for scalars.
**Action:** Replace inline imports of numpy for single scalar operations with math functions, especially in loops or mapping operations. Handle `OverflowError` appropriately.
