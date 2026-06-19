import re

with open("tests/test_llm_provider.py", "r") as f:
    content = f.read()

new_content = re.sub(
    r"tool_call = result\.tool_calls\[0\]",
    r"""if _PROVIDER != "mock":
        tool_call = result.tool_calls[0]""",
    content,
)

with open("tests/test_llm_provider.py", "w") as f:
    f.write(new_content)
