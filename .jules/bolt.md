
## 2026-03-04 - Vectorizing Nested Numpy Loops
**Learning:** In backend processing that operates heavily on dense matrices (like memory embeddings), writing a nested loop with `np.dot` over rows iteratively defeats the advantage of numpy's low-level optimizations and limits scalability for moderate batch sizes.
**Action:** Always favor bulk numpy operations (like full matrix-matrix dot products for pairwise comparisons `np.dot(M, M.T)`) over iteration. This typically delivers O(1) performance drops in execution time without changing API boundaries.
