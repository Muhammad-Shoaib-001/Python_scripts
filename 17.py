import random
import time
from datetime import datetime

# Terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Log file
LOG_FILE =  'D:\\PY\\log.txt'

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")

def check_service(service_name):
    log_message(f"Checking service: {service_name}")
    max_attempts = 3
    attempt = 1

    while attempt <= max_attempts:
        print(f"{YELLOW}🔄 Attempt {attempt} for {service_name}...{RESET}")
        log_message(f"Attempt {attempt} for {service_name}")
        
        is_up = random.choice([True, False])

        if is_up:
            print(f"{GREEN}✅ {service_name} is UP on attempt {attempt}{RESET}")
            log_message(f"{service_name} is UP on attempt {attempt}")
            return True
        else:
            print(f"{RED}❌ {service_name} is still DOWN. Retrying...{RESET}")
            log_message(f"{service_name} is still DOWN.")
            time.sleep(1)

        attempt += 1

    print(f"{RED}🚨 {service_name} failed after {max_attempts} attempts.{RESET}")
    log_message(f"{service_name} failed after {max_attempts} attempts.")
    return False

# List of services
services = ["nginx", "mysql", "redis", "kafka", "prometheus"]

success_count = 0
fail_count = 0

for service in services:
    status = check_service(service)
    if status:
        success_count += 1
    else:
        fail_count += 1

# Summary
print("\n====================")
print(f"{GREEN}✅ Services UP: {success_count}{RESET}")
print(f"{RED}❌ Services DOWN: {fail_count}{RESET}")
print("====================")

if fail_count == 0:
    print(f"{GREEN}🚀 All good. Proceeding with deployment.{RESET}")
    log_message("All services are UP. Proceeding with deployment.")
else:
    print(f"{RED}⛔ Deployment stopped. Check logs.{RESET}")
    log_message("Some services failed. Deployment stopped.")
