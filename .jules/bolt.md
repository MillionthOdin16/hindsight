## 2026-10-27 - Fast scalar exponential
**Learning:** Using `numpy.exp` for single scalar values in hot loops (like score normalization) is significantly slower (by ~6x) than `math.exp` due to Python-to-C API overhead and type coercion.
**Action:** Replace `numpy.exp` with `math.exp` with an `OverflowError` handler for single scalar operations where performance is critical.
