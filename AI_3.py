import requests, json

url = "http://148.251.90.210:11434/api/generate"
payload = {
    "model": "deepseek-coder:6.7b",
    "prompt": "Generate a Dockerfile, Jenkinsfile, and docker-compose.yml for a simple Flask app using Docker best practices."
}

with requests.post(url, json=payload, stream=True) as response:
    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            if 'response' in data:
                print(data['response'], end='', flush=True)
            if data.get('done', False):
                print("\n✅ Generation complete.")
