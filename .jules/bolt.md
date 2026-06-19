## 2026-06-19 - Fast math vs numpy for scalars
**Learning:** Using `np.exp` for scalar values inside hot loops (like `_sigmoid` over retrieved candidates) adds significant dispatch/boxing overhead compared to standard `math.exp` (approx 5-6x slower). However, `math.exp` can throw `OverflowError` on large negative inputs where `np.exp` safely returns `inf`.
**Action:** When migrating scalar math from `numpy` to `math` for performance, always wrap operations like `math.exp` in a `try...except OverflowError` block to maintain safety and fallback to appropriate boundary values (e.g., 0.0).
