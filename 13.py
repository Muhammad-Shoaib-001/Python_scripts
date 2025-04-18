import random
import time
services = ['nginx','mysql','redis']
max_attempts = 3
for service in services:
   print(f"\n🔍 Checking service: {service}")
   attempt = 1
   while attempt <= max_attempts :
     print(f"  🔄 Attempt {attempt}...")
     is_up = random.choice([True,False])
     if is_up :
            print(f"  ✅ {service} is UP on attempt {attempt}")
            break
     else:
            print(f"  ❌ {service} is still DOWN. Retrying...")
     time.sleep(1)
     attempt += 1
   if not is_up :
    print(f"  🚨 {service} failed to respond after {max_attempts} attempts.")