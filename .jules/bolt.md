## 2026-06-20 - Optimizing Token Counting
**Learning:** `tiktoken`'s `encode` method checks for special tokens even when `disallowed_special=()` is passed. Using `encode_ordinary` completely bypasses this check, offering a significant speedup for plain token counting where special tokens should be ignored.
**Action:** When counting tokens purely for length/budgeting without needing special token handling, always use `encode_ordinary` instead of `encode` with `disallowed_special=()`.
