import random
import time

# Define a function
def check_service(service_name):
    print(f"\n🔍 Checking service: {service_name}")
    max_attempts = 3
    attempt = 1

    while attempt <= max_attempts:
        print(f"  🔄 Attempt {attempt}...")

        is_up = random.choice([True, False])

        if is_up:
            print(f"  ✅ {service_name} is UP on attempt {attempt}")
            return True
        else:
            print(f"  ❌ {service_name} is still DOWN. Retrying...")
            time.sleep(1)

        attempt += 1

    print(f"  🚨 {service_name} failed to respond after {max_attempts} attempts.")
    return False


# List of services to check
services = ["nginx", "mysql", "redis"]

# Loop through and call the function
for service in services:
    check_service(service)
