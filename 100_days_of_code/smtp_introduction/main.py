import smtplib
import datetime as dt
import random

my_email = "testing.acc.udemy@gmail.com"
password = "yololo123"

now = dt.datetime.now()
day_of_week = now.weekday()
with open("quotes.txt") as quotes:
    list_of_quotes = quotes.readlines()
motivation_quote = random.choice(list_of_quotes)

if day_of_week == 5:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="naoki.kircia@gmail.com",
                            msg=f"Subject: Motivation Quote \n\n {motivation_quote}")