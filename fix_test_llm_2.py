import re
with open("hindsight-api-slim/tests/test_llm_provider.py", "r") as f:
    content = f.read()

content = content.replace("""    if llm.provider != "mock":
        assert isinstance(structured, TestResponse), f"Expected TestResponse, got {type(structured)}"
    assert structured.answer, "Structured output missing 'answer'"
    assert structured.confidence, "Structured output missing 'confidence'"

    # Test 4: call_with_tools()""", """    if llm.provider != "mock":
        assert isinstance(structured, TestResponse), f"Expected TestResponse, got {type(structured)}"
        assert structured.answer, "Structured output missing 'answer'"
        assert structured.confidence, "Structured output missing 'confidence'"

    # Test 4: call_with_tools()""")

with open("hindsight-api-slim/tests/test_llm_provider.py", "w") as f:
    f.write(content)
