import smtplib

my_email = "testing.acc.udemy@gmail.com"
password = "yololo123"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="naoki.kircia@gmail.com", msg="Hello")
connection.close()
