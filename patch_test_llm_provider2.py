import sys

def patch_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if "if not os.getenv('HINDSIGHT_API_LLM_PROVIDER'): return" in line:
            lines[i] = "    if not _PROVIDER: return\n"
            break

    with open(file_path, "w") as f:
        f.writelines(lines)

patch_file("hindsight-api-slim/tests/test_llm_provider.py")
