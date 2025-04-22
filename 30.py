import argparse
import docker 
import logging

import docker.errors

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
client = docker.from_env()

parser = argparse.ArgumentParser(description="Docker Command Manager CLI")
subparser = parser.add_subparsers(dest="command", help="Available commands")

subparser.add_parser("list", help="List running containers")

start_parser = subparser.add_parser("start", help="Start a container")
start_parser.add_argument("image", help="Docker image name")
start_parser.add_argument("--name", help="Container name", default=None)
start_parser.add_argument("--port", help="Port mapping like 8080:80", default=None)

stop_parser = subparser.add_parser("stop", help="Stop a container")
stop_parser.add_argument("name", help="Container name")

remove_parser = subparser.add_parser("remove", help="Remove a Container")
remove_parser.add_argument("name", help="Container name")

status_parser = subparser.add_parser("status" , help="Status of Container")
status_parser.add_argument("name", help="Container name")

args = parser.parse_args()

if args.command == "list":
    containers = client.containers.list()
    if containers:
        for c in containers:
            logging.info(f"{c.name} ({c.image.tags[0]}) - {c.status}")
    else:
        logging.info("No Containers Running")

elif args.command == "start":
    ports = None
    if args.port:
        host_port, container_port = args.port.split(":")
        ports = {f"{container_port}/tcp": int(host_port)}
    
    try:
        container = client.containers.run(
            args.image,
            name=args.name,
            ports=ports,
            detach=True
        )
        logging.info(f"Started container {container.name}")
    except docker.errors.APIError as e:
        logging.error(f"Failed to start container: {str(e)}")
elif args.command == "stop":
    try:
        containers = client.containers.get(args.name)
        containers.stop()
        logging.info(f"Stopped container {args.name}")
    except docker.errors.NotFound:
        logging.warning(f"Container {args.name} not found.")

elif args.command == "remove":
    try:
        container = client.containers.get(args.name)
        container.remove(force=True)
        logging.info(f"Removed container {args.name}")
    except docker.errors.NotFound:
        logging.warning(f"Container {args.name} not found.")
elif args.command == "status":
    try:
        container = client.containers.get(args.name)
        logging.info(f"{args.name} status: {container.status}")
    except docker.errors.NotFound:
        logging.warning(f"Container {args.name} not found.")

else:
    parser.print_help()