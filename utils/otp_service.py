import random
import smtplib
from email.mime.text import MIMEText

EMAIL = "jignashgeda@gmail.com"
PASSWORD = "scltaopsokqjkmja"


def generate_otp():

    return str(random.randint(100000, 999999))


def send_otp(user_email, otp):

    message = f"""
Your Complaint System Verification Code

OTP: {otp}

Enter this code in the application to verify your email.
"""

    msg = MIMEText(message)

    msg["Subject"] = "Complaint System Email Verification"
    msg["From"] = "Complaintees Verification <jignashgeda@gmail.com>"
    msg["To"] = user_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(EMAIL, PASSWORD)

        server.send_message(msg)