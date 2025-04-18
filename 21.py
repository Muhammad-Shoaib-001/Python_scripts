import smtplib
from email.message import EmailMessage

def send_email_report(filepath):
    sender = "shoaibfaisal83@gmail.com"
    password = "lwwvsobmrhzphath"  # Use App Password, NOT your actual password
    receiver = "ignites69.69@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "📊 DevOps Service Report"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Hi,\n\nPlease find attached the latest service status report.\n\nRegards,\nDevOps Bot")

    # Attach the JSON file
    with open(filepath, "rb") as f:
        data = f.read()
        msg.add_attachment(data, maintype="application", subtype="json", filename="report.json")

    # Send email via Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("📧 Report emailed successfully!")

# Call this function
send_email_report("D:\\PY\\report.json")
