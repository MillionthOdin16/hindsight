import re
import sys

with open('.github/workflows/test.yml', 'r') as f:
    content = f.read()

content = content.replace("PROJECT_ID=$(jq -r '.project_id' /tmp/gcp-credentials.json)", "PROJECT_ID='dummy'")
content = content.replace("PROJECT_ID=$(jq -r '.project_id' gcp-credentials.json)", "PROJECT_ID='dummy'")

with open('.github/workflows/test.yml', 'w') as f:
    f.write(content)
