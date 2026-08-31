## 2026-08-02 - Replace numpy.exp with math.exp in scalar hot paths
**Learning:** For single scalar operations in hot paths (like score normalization loops in search reranking), using `numpy.exp` introduces significant Python-to-C dispatch overhead, making it ~6.5x slower than the standard library `math.exp`.
**Action:** Replace `numpy.exp` with `math.exp` for scalar computations in critical paths, and wrap the operation in a `try/except OverflowError` block to safely handle highly negative inputs (where math.exp raises an exception instead of evaluating to 0.0 like numpy). Make sure to import `math` explicitly if it is not already available.

## 2026-08-02 - Code generation commands
**Learning:** We need to update OpenAPI, schemas, clients, and docs if we modify any backend code, such as `hindsight-api-slim/hindsight_api/engine/search/reranking.py`.
**Action:** The CI checks failed due to out-of-sync generated files. We need to run `./scripts/generate-openapi.sh`, `./scripts/generate-bank-template-schema.sh`, `./scripts/generate-clients.sh`, `./scripts/generate-docs-skill.sh`, and `./scripts/hooks/lint.sh`.
