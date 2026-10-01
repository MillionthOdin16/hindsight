## 2026-03-09 - Avoid Modifying Tests for CI Fixes Without Verification
**Learning:** Adding default values to `BaseModel` output formats in mock LLM tests bypasses test validation entirely. Modifying test logic to suppress CI failures when mock data changes is a severe anti-pattern that hides underlying system issues (e.g., mock providers not implementing valid structured output responses).
**Action:** Revert invalid test suite changes. Ensure `import math` is present at the module level when switching scalar operations from `numpy.exp` to `math.exp`.
