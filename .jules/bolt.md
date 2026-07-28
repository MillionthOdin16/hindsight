## 2024-05-15 - [Initial]
**Learning:** [Create initial bolt.md]
**Action:** [Create initial bolt.md]

## 2026-07-28 - Optimize scalar exponential function
**Learning:** Using `math.exp` for single scalar operations instead of `numpy.exp` in hot paths (like reranking scoring) avoids Python-to-C conversion overhead and inline imports of large libraries. `numpy.exp` can be up to 10x slower for scalars compared to `math.exp`.
**Action:** Prefer standard library `math` functions for scalars, but explicitly handle `OverflowError` as `math.exp` raises on large negative/positive inputs unlike `numpy` which silently returns 0.0 or inf.
