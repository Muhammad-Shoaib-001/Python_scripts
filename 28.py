import docker 
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler()]
)

client = docker.from_env()

try:
    client.ping()
    logging.info("Docker is Up")
except Exception as e:
    logging.info("Docker is not up")
    exit(1)

containers = client.containers.list()
logging.info(" Running Containers: ")
if containers:
    for container in containers:
         logging.info(f"- {container.name} ({container.status})")
else:
    logging.info("No Container Running")

nginx = any("nginx" in c.image.tags[0] for c in containers if c.image.tags)
if not nginx:
    client.containers.run("nginx" , name = "nginx-demo", ports={"80/tcp": 8085}, detach=True)
    logging.info("Starting nginx container...")
    logging.info("nginx container is up")

else:
    logging.info("nginx is already running")
