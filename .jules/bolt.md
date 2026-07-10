## 2026-05-14 - Replace inline numpy with math in hot paths
**Learning:** Using numpy for scalar operations in a loop (like `np.exp`) introduces significant Python-to-C overhead compared to the standard library `math` module. Inline imports in hot paths further degrade performance.
**Action:** For single scalar operations, prefer standard library functions (e.g., `math.exp`) over heavy dependencies like numpy.
