import time
import random

def deployment(dep_name):
    print(f"\n🔍 Checking service: {dep_name}")
    max_attempts = 3
    attempt = 1

    while attempt <= max_attempts:
        print(f"  🔄 Attempt {attempt}...")

        is_up = random.choice([True, False])

        if is_up:
            print(f"  ✅ {dep_name} is UP on attempt {attempt}")
            return True
        else:
            print(f"  ❌ {dep_name} is still DOWN. Retrying...")
            time.sleep(1)

        attempt += 1

    print(f"  🚨 {dep_name} failed to respond after {max_attempts} attempts.")
    return False

services = ["nginx", "mysql", "redis"]

all_up = True

for service in services:
    status = deployment(service)
    if not status:
            all_up = False

# Final deployment decision
if all_up:
    print("\n🚀 All services are UP! Proceeding with deployment.")
else:
    print("\n⛔ Deployment aborted. Some services are still DOWN.")
   

