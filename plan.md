1. **Optimize Tiktoken Encoding**
   - The `_SafeEncoding` class in `hindsight_api/engine/token_encoding.py` currently uses `self._encoding.encode(text, **kwargs)` with `kwargs.setdefault("disallowed_special", ())` to avoid throwing errors on special tokens.
   - However, `encode_ordinary` is designed specifically for this use case and bypasses all regex checks for special tokens, making it ~20% faster than `encode` with `disallowed_special=()`. It is equivalent in tokenizing plain text including special token strings.
   - I will modify `_SafeEncoding.encode` to use `encode_ordinary` when `kwargs` has no other arguments (which is true in `count_tokens` and throughout the app), falling back to `encode` if kwargs are provided.
2. **Review other token counting overhead**
   - Ensure `count_tokens` in `token_encoding.py` and `count_cl100k_tokens` in `reflect/tokenization.py` are properly optimized.
3. **Pre-commit Checks**
   - Ensure proper testing, verification, review, and reflection are done by calling the pre commit instructions tool.
4. **Submit PR**
   - Create a PR with title `⚡ Bolt: [performance improvement]` and the expected sections.
