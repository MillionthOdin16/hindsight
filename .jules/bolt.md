## 2026-09-17 - Python Hot Path Optimization
**Learning:** Using `numpy.exp` for scalar operations in a loop (like `_sigmoid` calculating score logits) introduces unnecessary Python-to-C overhead.
**Action:** Replace `numpy.exp` with `math.exp` for scalar operations in Python hot paths. Wrap it in a `try/except OverflowError` block since `math.exp` raises an exception for large negative inputs, whereas `numpy.exp` handles it by returning 0.0.
