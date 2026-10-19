## 2026-10-19 - Python to C overhead with numpy
**Learning:** Using `numpy.exp` for scalar operations in a loop incurs significant Python-to-C overhead. In Python hot paths, replacing `numpy.exp` with `math.exp` (wrapped in a try-except to handle `OverflowError`) yields nearly a 10x performance improvement for scalar inputs.
**Action:** Avoid heavy numpy array functions like `np.exp` when computing math on individual scalar variables. Instead, use standard library `math` module functions like `math.exp` and handle exceptions where appropriate.
