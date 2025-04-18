import random 
import json
import time
import smtplib
from email.message import EmailMessage

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

def send_mail(file_path):
    sender = "shoaibfaisal83@gmail.com"
    password = "lwwvsobmrhzphath"  # Use App Password, NOT your actual password
    receiver = "ignites69.69@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Daily Report"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Hi,\n\nPlease find attached the latest service status report.\n\nRegards,\nDevOps Bot")

 
    with open(file_path, "rb") as f:
        data = f.read()
        msg.add_attachment(data,maintype="application", subtype="json",filename="report.json")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
         smtp.login(sender,password)
         smtp.send_message(msg)
    print("📧 Report emailed successfully!")

send_mail("D:\\PY\\report.json")

   

