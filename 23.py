import random
import time

log_levels = ["INFO","DEBUG", "WARNING", "ERROR","CRITICAL"]

messages = [
    "Service started",
    "Connection successful",
    "Low memory",
    "Service crashed",
    "Unauthorized access detected",
    "Retrying connection"
]
def gen_log_metrics():
    level = random.choice(log_levels)
    message = random.choice(messages)
    return f"{level}:{message}"
print("🧭 Starting log monitor...")

for i in range(10):
   log_entry = gen_log_metrics()
   print(log_entry)

   if "ERROR" in log_entry or "CRITICAL" in log_entry:
        print("🚨 Alert: Action required!")
        time.sleep(1) 