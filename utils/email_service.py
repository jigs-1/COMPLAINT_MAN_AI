import smtplib
from email.mime.text import MIMEText

EMAIL = "jignashgeda@gmail.com"
PASSWORD = "scltaopsokqjkmja"


def send_email(to_email, subject, summary, category, priority, complaint, user_email):

    message = f"""
Complaint Management System Notification

A new complaint has been submitted.

---------------------------------------

Complaint Summary:
{summary}

Category:
{category}

Priority:
{priority}

---------------------------------------

Full Complaint:
{complaint}

---------------------------------------

Submitted By:
{user_email}

Please investigate and resolve the issue as soon as possible.

Complaint Management System
"""

    msg = MIMEText(message)

    msg["Subject"] = subject
    msg["From"] = "Complaintees Complaint System <jignashgeda@gmail.com>"
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(EMAIL, PASSWORD)

        server.send_message(msg)