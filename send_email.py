import smtplib, ssl
import os

def send_email(user_email, subject, user_message):
    host = "smtp.gmail.com"
    port = 465
    username = "atharvachaphe7@gmail.com"
    # password = os.getenv("GMAIL_PASSWORD")
    password = "rrwiypxbjadgjhbf"
    context = ssl.create_default_context()

    # Message to Atharva (you)
    message_to_me = f"""\
Subject: New Portfolio Message from {user_email}

From: {user_email}
Subject: {subject}

Message:
{user_message}
"""

    # Message to User (auto reply)
    message_to_user = f"""\
Subject: Thanks for contacting me, {user_email}

Hi {user_email},

Thank you for reaching out to me through my portfolio website. I appreciate your interest!

I've received your message:
"{user_message}"

I'll get back to you as soon as possible. In the meantime, feel free to connect with me on LinkedIn:
https://www.linkedin.com/in/atharva-chaphe

Best regards,  
Atharva Chaphe  
Full Stack Developer | Data Science Enthusiast  
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # Send email to yourself
        server.sendmail(username, username, message_to_me)
        # Send confirmation email to user
        server.sendmail(username, user_email, message_to_user)
