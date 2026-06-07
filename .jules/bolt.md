## 2026-06-03 - [Performance] Optimize Search Retrieval and Reranking Functions
**Learning:** Python regex compilation inside frequently called functions (like `tokenize_query`) incurs noticeable overhead. Loops performing data transformations in Python benefit from moving invariant definitions (constants, local variable caching instead of dot-lookup) out of loops.
**Action:** When a regex is static, extract `re.compile()` calls to module level. In performance-critical tight loops, hoist invariants and cache property lookups locally to reduce CPU time.
