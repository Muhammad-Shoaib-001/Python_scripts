import requests

OLLAMA_URL = "http://148.251.90.210:11434"

prompt = """
You are a DevOps AI assistant.
Generate a Dockerfile for a Python Flask app that runs on port 5000.
"""

response = requests.post(
    f"{OLLAMA_URL}/api/generate",
    json={"model": "starcoder2:15b", "prompt": prompt},
    stream=True
)

for line in response.iter_lines():
    if line:
        try:
            data = line.decode("utf-8")
            # Each line is a JSON object with a partial response
            if '"response"' in data:
                # Extract the text between "response":"..."
                part = data.split('"response":"')[1].split('"')[0]
                print(part, end='', flush=True)
        except Exception:
            pass

print("\n---\nDone.")
