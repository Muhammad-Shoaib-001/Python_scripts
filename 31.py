import docker 
import argparse
import logging
from colorama import init, Fore,Style
import os

init(autoreset=True)

os.makedirs("logs",exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("D:\PY\docker_cli.log"),
        logging.StreamHandler()
    ]
)
client = docker.from_env()

# Argument Parser
parser = argparse.ArgumentParser(description="🚀 Docker Container Manager CLI")
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# List
subparsers.add_parser("list", help="List running containers")

# Start
start_parser = subparsers.add_parser("start", help="Start a container")
start_parser.add_argument("image", help="Docker image")
start_parser.add_argument("--name", help="Container name", default=None)
start_parser.add_argument("--port", help="Port mapping like 8080:80", default=None)

# Stop
stop_parser = subparsers.add_parser("stop", help="Stop a container")
stop_parser.add_argument("name", help="Container name")

# Remove
remove_parser = subparsers.add_parser("remove", help="Remove a container")
remove_parser.add_argument("name", help="Container name")

# Status
status_parser = subparsers.add_parser("status", help="Container status")
status_parser.add_argument("name", help="Container name")

args = parser.parse_args()

def info(msg):
    print(Fore.CYAN + msg)
    logging.info(msg)

def success(msg):
    print(Fore.GREEN + msg)
    logging.info(msg)

def warn(msg):
    print(Fore.YELLOW + msg)
    logging.warning(msg)

def error(msg):
    print(Fore.RED + msg)
    logging.error(msg)

# Handle commands
try:
    if args.command == "list":
        containers = client.containers.list()
        if containers:
            for c in containers:
                info(f"{c.name} ({c.image.tags[0]}) - {c.status}")
        else:
            warn("No containers running.")

    elif args.command == "start":
        ports = None
        if args.port:
            host, container = args.port.split(":")
            ports = {f"{container}/tcp": int(host)}
        container = client.containers.run(args.image, name=args.name, ports=ports, detach=True)
        success(f"Started container {container.name}")

    elif args.command == "stop":
        container = client.containers.get(args.name)
        container.stop()
        success(f"Stopped {args.name}")

    elif args.command == "remove":
        container = client.containers.get(args.name)
        container.remove(force=True)
        success(f"Removed {args.name}")

    elif args.command == "status":
        container = client.containers.get(args.name)
        info(f"{args.name} status: {container.status}")

    else:
        parser.print_help()

except docker.errors.NotFound:
    error(f"Container '{args.name}' not found.")
except docker.errors.APIError as e:
    error(f"Docker API error: {e}")
except Exception as e:
    error(f"Unexpected error: {e}")
