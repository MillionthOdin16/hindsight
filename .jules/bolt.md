## 2026-06-25 - Batching Postgres Operations with `executemany`
**Learning:** Looping over `await conn.execute(...)` calls to insert multiple database records is a common N+1 query anti-pattern leading to numerous network round trips and slower execution.
**Action:** When inserting multiple rows dynamically from an iterative list or dictionary, try grouping parameters and utilizing `await conn.executemany(query, parameters)` to significantly reduce database communication overhead.
