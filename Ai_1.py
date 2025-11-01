import requests

OLLAMA_URL = "http://148.251.90.210:11434"

prompt = """
You are a DevOps assistant.
Analyze a Node.js + React project.
Generate:
1. Dockerfile (multi-stage)
2. Jenkinsfile (build, test, deploy)
3. Helm chart (values.yaml + deployment.yaml)
"""

res = requests.post(f"{OLLAMA_URL}/api/generate",json={
    "model": "starcoder2:15b",
    "prompt": prompt
})

for line in res.iter_lines():
    if line:
        print(line.decode())