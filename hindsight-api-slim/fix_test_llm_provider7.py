import re

with open("tests/test_llm_provider.py", "r") as f:
    content = f.read()

new_content = re.sub(
    r'if _PROVIDER != "mock":\s+tool_call = result\.tool_calls\[0\]\s+assert tool_call\.name == "get_weather", f"Expected \'get_weather\', got \'\{tool_call\.name\}\'"\s+import json\s+args = json\.loads\(tool_call\.arguments\)\s+assert "location" in args, "Tool call missing required argument \'location\'"\s+assert "paris" in args\["location"\].lower\(\), f"Expected location to contain \'Paris\', got \{args\[\'location\'\]\}"',
    r'''if _PROVIDER != "mock":
        tool_call = result.tool_calls[0]
        assert tool_call.function.name == "get_weather", f"Expected 'get_weather', got '{tool_call.function.name}'"
        import json
        args = json.loads(tool_call.function.arguments)
        assert "location" in args, "Tool call missing required argument 'location'"
        assert "paris" in args["location"].lower(), f"Expected location to contain 'Paris', got {args['location']}"''',
    content,
)

with open("tests/test_llm_provider.py", "w") as f:
    f.write(new_content)
