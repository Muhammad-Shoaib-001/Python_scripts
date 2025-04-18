import random 
import json
import time

services = ["nginx", "mysql", "redis", "kafka", "grafana"]

max_attempt = 3
retry_time = 1
results = {}
file = "D:\\PY\\report.json"

def check_service(service):
    attempt = 1
    while attempt <= max_attempt:
        print(f"🔄 Checking {service} (attempt {attempt})...")
        is_up = random.choice([True, False])
        if is_up:
            print(f"✅ {service} is UP")
            return "Up"
        else:
            print(f"❌ {service} is DOWN, retrying...")
            time.sleep(retry_time)
            attempt += 1

    print(f"🚨 {service} failed after {max_attempt} attempts")
    return "Down"
for service in services:
   status = check_service(service)
   results[service] = status
   
summary = {
   "checked" : len(services),
   "up" : list(results.values()).count("Up"),
   "Down" : list(results.values()).count("Down")
}
report = {
   "summary" : summary,
   "results" : results
}
with open(file, "w" ) as f:
   json.dump(report,f,indent=4)
print("\n📦 Report saved to report.json")


   

