## 2026-06-24 - Optimize dict comprehension in EntityResolver

**Learning:** Found an unnecessary intermediate dictionary creation (`[{"id": c[0], "canonical_name": c[1]} for c in cands]`) inside a nested dictionary comprehension in `entity_resolver.py` that mapped entity ID to canonical name. It was allocating a temporary list of dicts for every candidate evaluation.
**Action:** Removed the temporary dict allocation and iterated directly over `cands`, destructuring values using index access `c[0]: c[1].lower()`. This improves CPU efficiency inside the hot path.
