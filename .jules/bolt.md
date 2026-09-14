## 2026-09-11 - Fast Math is Fast

**Learning:** Replacing `numpy.exp` with `math.exp` for single scalar operations (like sigmoid normalization for logits) avoids the costly Python-to-C bridge and large import overhead, yielding a small but measurable speedup per search operation in Python hot paths.
**Action:** Always prefer standard library functions (`math.exp`) over heavy dependencies (`numpy.exp`) for scalar operations in tight loops unless array vectorization is possible and utilized.
