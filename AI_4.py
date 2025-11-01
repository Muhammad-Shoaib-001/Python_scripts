import requests, json, re, sys

URL = "http://148.251.90.210:11434/api/generate"
PAYLOAD = {
    "model": "deepseek-coder:6.7b",
    "prompt": (
        "You are a code generator. OUTPUT ONLY TWO FILES and NOTHING ELSE.\n\n"
        "1) Dockerfile (no comments)\n"
        "2) Jenkinsfile (Declarative Jenkinsfile, no comments)\n\n"
        "Format EXACTLY as two fenced code blocks with these language tags:\n"
        "```dockerfile\n"
        "<Dockerfile contents>\n"
        "```\n\n"
        "```groovy\n"
        "<Jenkinsfile contents>\n"
        "```\n\n"
        "Do not print any extra text, explanations, headings, or markdown besides those two fenced blocks."
    ),
    "stream": True,
    "options": {"temperature": 0.0, "num_predict": 1024}
}

def extract_blocks(text):
    blocks = re.findall(
        r"```(?:dockerfile|Dockerfile)\s*([\s\S]*?)```|```(?:groovy|Groovy)\s*([\s\S]*?)```",
        text,
    )
    contents = [(a or b).strip() for a, b in blocks if (a or b).strip()]
    return contents

print("🚀 Streaming response from model...\n")

response_text = ""
with requests.post(URL, json=PAYLOAD, stream=True) as resp:
    for line in resp.iter_lines():
        if not line:
            continue
        try:
            chunk = json.loads(line.decode("utf-8"))
        except Exception:
            continue

        if "response" in chunk:
            sys.stdout.write(chunk["response"])  # ✅ Print token immediately
            sys.stdout.flush()
            response_text += chunk["response"]

        if chunk.get("done"):
            print("\n✅ Generation complete.\n")
            break

# (optional) extract the fenced blocks after streaming completes
blocks = extract_blocks(response_text)
if len(blocks) >= 1:
    dockerfile = blocks[0]
else:
    dockerfile = ""

if len(blocks) >= 2:
    jenkinsfile = blocks[1]
else:
    jenkinsfile = ""
