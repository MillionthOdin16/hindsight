import sys

def patch_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if 'if not vertexai_project_id and not getattr(self, "_skip_llm_verification", False) and getattr(self, "provider", "") != "mock":' in line:
            lines[i] = '            if not vertexai_project_id and not getattr(self, "_skip_llm_verification", False):\n'
            break

    with open(file_path, "w") as f:
        f.writelines(lines)

patch_file("hindsight-api-slim/hindsight_api/engine/llm_wrapper.py")
