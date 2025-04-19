import docker 
import logging

import docker.errors

logging.basicConfig(
    level=logging.INFO,  # capital INFO, not info
    format="%(asctime)s [%(levelname)s] - %(message)s",  # fix the typo (%message)s
    handlers=[logging.StreamHandler()]  # fix "handler" -> "handlers"
)

client = docker.from_env()

client.ping()
try:
    logging.info("Docker is up")
except Exception as e:
   logging.info("Docker is Down")
   exit(1)

containers = client.containers.list()
logging.info(" Running Containers: ")
if containers:
    for container in containers:
         logging.info(f"- {container.name} ({container.status})")
else:
    logging.info("No container Running")

nginx = any("nginx" in c.image.tags[0] for c in containers if c.image.tags)
logging.info("Nginx is already running")
if not nginx:
    client.containers.run("nginx" , name = "nginx-demo", ports={"80/tcp": 8085}, detach=True)
    logging.info("Starting nginx container...")
    logging.info("nginx container is up")
else:
    logging.info("nginx is already running")

def stop_container(container_name):
    try:
        container = client.containers.get(container_name)
        container.stop()
        logging.info(f"Stopped container: {container.name}")
    except docker.errors.NotFound:
        logging.warning(f"Container {container_name} not found.")

def remove_container(container_name):
    try:
        container = client.containers.get(container_name)
        container.remove()
        logging.info(f"Stopped container: {container.name} Removed")
    except docker.errors.NotFound:
        logging.warning(f"Container {container_name} not found.")

stop_container("nginx-demo")
remove_container("nginx-demo")




      