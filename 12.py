import random
import time

service = "nginx"

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print(f"🔄 Attempt {attempt} to check {service}...")

    is_up = random.choice([True, False])
    if is_up:
        print(f"✅ {service} is UP on attempt {attempt}")
        break
    else:
        print(f"❌ {service} is still DOWN. Retrying...")
        time.sleep(1)

    attempt += 1

if not is_up:
    print(f"🚨 {service} failed to respond after {max_attempts} attempts.")
