## 2026-08-27 - Inline Imports in Reranking Path
**Learning:** The inline import of `numpy` inside the `_sigmoid` function in `hindsight-api-slim/hindsight_api/engine/search/reranking.py` causes significant performance overhead since `_sigmoid` is called in a loop for every candidate document during reranking. Python-to-C conversion for single scalars with numpy also adds unnecessary overhead.
**Action:** Replace inline numpy functions in tight loops with `math` module equivalents (e.g., `math.exp`), handling `OverflowError` for large inputs. Avoid inline imports inside loops where possible.
