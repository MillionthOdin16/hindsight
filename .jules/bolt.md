## 2026-06-16 - Combine Count Queries via Window Function in `list_operations`
**Learning:** `list_operations` is a common query in the API. It originally uses two queries: a `SELECT COUNT(*) WHERE ...` followed by a `SELECT ... WHERE ... ORDER BY ... LIMIT ... OFFSET ...`.
In Postgres, this dual query approach introduces two roundtrips and doubles the execution overhead. Utilizing a window function (`COUNT(*) OVER()`) allows you to do the pagination and fetch the total row count in one go. However, if the `OFFSET` is greater than or equal to the total rows, the window function approach yields empty results and thus misses the count entirely.
We can fallback to a separate count query in this edge case, keeping the "happy path" (which covers page 1 logic, e.g. OFFSET=0) fully optimized.

**Action:** Update `list_operations` in `hindsight_api/engine/memory_engine.py` to use `COUNT(*) OVER() as full_count`, extracting the total count from the first result object if present. If `operations` is empty, fallback to the current explicit `SELECT COUNT(*)` query to satisfy the API contract when `offset >= total`.
