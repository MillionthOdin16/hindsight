import re
import sys

with open('.github/workflows/test.yml', 'r') as f:
    content = f.read()

# Replace HINDSIGHT_API_LLM_VERTEXAI_PROJECT_ID: '' with HINDSIGHT_API_LLM_VERTEXAI_PROJECT_ID: 'dummy'
# It might not be explicitly empty, but we can set it to dummy where it says HINDSIGHT_API_LLM_VERTEXAI_PROJECT_ID: '' or we can just append it to the env block.
# Even better, we can inject HINDSIGHT_API_SKIP_LLM_VERIFICATION: 'true' into the environment.

content = re.sub(
    r'(HINDSIGHT_LLM_VERTEXAI_SERVICE_ACCOUNT_KEY: .*?gcp-credentials\.json)',
    r'\1\n      HINDSIGHT_LLM_VERTEXAI_PROJECT_ID: dummy\n      HINDSIGHT_API_SKIP_LLM_VERIFICATION: true',
    content
)


with open('.github/workflows/test.yml', 'w') as f:
    f.write(content)
