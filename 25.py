import random
import time 

log_levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
messages = [
    "Service started",
    "Connection successful",
    "Low memory",
    "Service crashed",
    "Unauthorized access detected",
    "Retrying connection"
]
log_file = "D:\\PY\\log.txt"

while True:
    message = random.choice(messages)
    level = random.choice(log_levels)
    log_line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {level}: {message}\n"
    with open(log_file, "a") as f:
        f.write(log_line)

    time.sleep(1)