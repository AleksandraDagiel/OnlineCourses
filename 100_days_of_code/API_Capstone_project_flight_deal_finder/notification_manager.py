import smtplib
from twilio.rest import Client

TWILIO_SID = "ACca0fe99049e758fdcd84e0e0f55fa948"
TWILIO_AUTH_TOKEN = "93049eb4d1c279d5756793c80fb6dd99"
TWILIO_VIRTUAL_NUMBER = "+12073604858"
TWILIO_VERIFIED_NUMBER = "+48884617302"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "testing.acc.udemy@gmail.com"
MY_PASSWORD = "yololo123"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )