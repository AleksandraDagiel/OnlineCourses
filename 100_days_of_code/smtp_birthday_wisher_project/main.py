import pandas
import random
import smtplib
import datetime

my_email = "testing.acc.udemy@gmail.com"
password = "yololo123"


# My way
# today = datetime.datetime.now()
# today_day = today.day
# today_month = today.month
# data = pandas.read_csv("birthdays.csv")
# birthday_dict = data.to_dict("records")
#
#
# for person in birthday_dict:
#     bday_day = person["day"]
#     bday_month = person["month"]
#
#     if today_day == bday_day and today_month == bday_month:
#         random_letter = random.randint(1, 3)
#
#         with open(f"./letter_templates/letter_{random_letter}.txt", "r") as letter:
#             letter = letter.read()
#             personalised_letter = letter.replace("[NAME]", person["name"])
#
#         with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(from_addr=my_email, to_addrs=person["email"],
#                                 msg=f"Subject: Happy Birthday \n\n {personalised_letter}")
#

# Course solution

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[Name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday \n\n {contents}")
