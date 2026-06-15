import smtplib
import os
from email.mime.text import MIMEText

sender = os.environ["MAIL_USER"]
password = os.environ["MAIL_PASS"]
receiver = os.environ["MAIL_TO"]

msg = MIMEText("这是一封自动发送的邮件内容", "plain", "utf-8")
msg["Subject"] = "自动邮件提醒"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.163.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, [receiver], msg.as_string())

print("邮件发送成功")
