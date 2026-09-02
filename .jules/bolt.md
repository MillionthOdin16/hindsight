## 2026-09-02 - Replace numpy.exp with math.exp in scalar hot loops
**Learning:** Using `numpy.exp` for single scalar operations incurs significant Python-to-C conversion overhead. In performance-critical hot paths like the CrossEncoderReranker's `_sigmoid` function, this can be extremely slow.
**Action:** Replace `numpy.exp` with `math.exp` for scalar operations, wrapped in a `try/except OverflowError` block since `math.exp` throws an exception for large inputs while `numpy.exp` handles it.
