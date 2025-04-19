import time
import random
from datetime import datetime
import smtplib
from email.message import EmailMessage

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

def log_message(log_msg , level="INFO"):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    formatted_log = f"[{timestamp}] [{level}] {log_msg}"
    with open(log_file , "a", encoding="UTF-8") as f:
     f.write(formatted_log + "\n")
     print(formatted_log )


def check_logs():
        levels = random.choice(log_levels)
        message = random.choice(messages)
        return levels , message
log_message("🧭 Starting log monitor...\n")

for i in range(10):
    level, log = check_logs()
    log_message(log,level)
    if level in ["ERROR", "CRITICAL"]:
        print("🚨 Alert: Action required!\n")
    time.sleep(1)

print("✅ Logs saved successfully.")

def send_email(file_path):
    sender = "shoaibfaisal83@gmail.com"
    password = "lwwvsobmrhzphath"  # Use App Password, NOT your actual password
    receiver = "ignites69.69@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Daily Report"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Hi,\n\nPlease find attached the latest service status report.\n\nRegards,\nDevOps Bot")

    with open(log_file,'rb') as f:
        data = f.read()
        msg.add_attachment(data , maintype = "application" ,subtype = "txt",filename = "log.txt")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)
        print("📧 Report emailed successfully!")

send_email("D:\\PY\\log.txt")
    


