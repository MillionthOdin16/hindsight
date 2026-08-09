## 2025-06-06 - Tiktoken `encode_ordinary` Mock Issue
**Learning:** `fake_encoding` mock sets `encode.side_effect` but when testing `encode_ordinary` the mock doesn't handle it, causing it to return a MagicMock object, which has length 0, making the test fail.
**Action:** Need to patch `encode_ordinary` in the `fake_encoding` mock.
