import time
import random
from datetime import datetime

log_file = 'D:\\PY\\log.txt'
def log_message(message):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(log_file,"a", encoding="utf-8") as log :
        log.write(f"[{timestamp}] {message}\n")

def check_services(service_name):
    log_message(f"\n🔍 Checking service: {service_name}")
    max_attempt = 3
    attempts = 1
    while attempts <= max_attempt :
        log_message(f"  🔄 Attempt {attempts}...")
        is_up = random.choice([True,False])
        if is_up:
           log_message(f"  ✅ {service_name} is UP on attempt {attempts}")
           return True
        else:
           log_message(f"  ❌ {service_name} is still DOWN. Retrying...")
           time.sleep(1)
           attempts += 1
    log_message(f"  🚨 {service_name} failed to respond after {max_attempt} attempts.")
    return False

services = ["nginx", "mysql", "redis"]

all_up = True

for service in services :
    status = check_services(service)
    if not status :
        all_up = False
if all_up:
    log_message("\n🚀 All services are UP! Proceeding with deployment.")
    print("\n🚀 All services are UP! Proceeding with deployment.")
else:
    log_message("\n⛔ Deployment aborted. Some services are still DOWN.")
    print("\n⛔ Deployment aborted. Some services are still DOWN.")

        