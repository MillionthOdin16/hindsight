import re
import sys

with open('.github/workflows/test.yml', 'r') as f:
    content = f.read()

content = content.replace("HINDSIGHT_API_SKIP_LLM_VERIFICATION: true", "HINDSIGHT_API_SKIP_LLM_VERIFICATION: 'true'")

with open('.github/workflows/test.yml', 'w') as f:
    f.write(content)
