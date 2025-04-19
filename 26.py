# log_monitor.py

import time

log_file = "D:\\PY\\log.txt"

print("👀 Monitoring logs for ERRORs and CRITICAL alerts...\n")

with open(log_file, "r") as f:
    # Go to the end of the file
    f.seek(0, 2)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue

        print(line.strip())

        if "ERROR" in line or "CRITICAL" in line:
            print("🚨 ALERT! Immediate attention needed!\n")
