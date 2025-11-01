import os, json, requests

def scan_project(path):
    """Scan files to detect language and framework."""
    info = {}

    if os.path.exists(os.path.join(path, "requirements.txt")):
        info["language"] = "python"
        with open(os.path.join(path, "requirements.txt")) as f:
            deps = [line.strip() for line in f if line.strip()]
        info["dependencies"] = deps
        if any("flask" in d.lower() for d in deps):
            info["framework"] = "flask"

    elif os.path.exists(os.path.join(path, "package.json")):
        info["language"] = "javascript"
        with open(os.path.join(path, "package.json")) as f:
            package = json.load(f)
        info["dependencies"] = list(package.get("dependencies", {}).keys())
        if "react" in info["dependencies"]:
            info["framework"] = "react"

    return info

def generate_docker_jenkins(info):
    """Send prompt to DeepSeek model running on Ollama."""
    prompt = (
        f"Project info: {json.dumps(info)}\n"
        "Generate only a Dockerfile and Jenkinsfile for this project. "
        "No explanations, just two fenced code blocks."
    )

    payload = {"model": "deepseek-coder:6.7b", "prompt": prompt, "stream": True}
    url = "http://148.251.90.210:11434/api/generate"

    print("🧠 Generating output from model...\n")
    with requests.post(url, json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                chunk = json.loads(line)
                if "response" in chunk:
                    print(chunk["response"], end="", flush=True)
                if chunk.get("done"):
                    break

# Example usage:
path = "D:\\Next-js -app"
project_info = scan_project(path)
print("Detected project info:", project_info)
generate_docker_jenkins(project_info)
