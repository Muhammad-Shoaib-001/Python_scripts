import docker

# Connect to Docker
client = docker.from_env()

# Check if Docker is accessible
try:
    client.ping()
    print("✅ Docker is running!")
except Exception as e:
    print(f"❌ Docker is not accessible: {e}")
    exit(1)

# List running containers
containers = client.containers.list()
print("\n🔍 Running Containers:")
if containers:
    for container in containers:
        print(f"- {container.name} ({container.status})")
else:
    print("No containers running.")

# Check if nginx is running, else start it
nginx_running = any("nginx" in c.image.tags[0] for c in containers if c.image.tags)
if not nginx_running:
    print("\n🚀 Starting nginx container...")
    client.containers.run("nginx", name="nginx_demo", ports={"80/tcp": 8085}, detach=True)
    print("✅ Nginx started on port 8080")
else:
    print("\n✅ Nginx is already running.")
