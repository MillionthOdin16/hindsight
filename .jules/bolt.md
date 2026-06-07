## 2026-06-25 - Async Event Loop Blocking from CPU-heavy library
**Learning:** Initializing/using `dateparser` synchronously in an async function (`retrieve_all_fact_types_parallel`) blocks the asyncio event loop entirely because `dateparser` is heavily synchronous/CPU-bound (regex parsing/locale tables).
**Action:** When calling CPU-bound Python libraries from an async context in this codebase, always wrap them with `await asyncio.to_thread()` to prevent blocking the event loop and hurting overall server concurrency.
