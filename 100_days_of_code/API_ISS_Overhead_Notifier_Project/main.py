import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.2102428
MY_LONG = 17.38294699262042
MY_EMAIL = "testing.acc.udemy@gmail.com"
PASSWORD = "yololo123"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT + 5) >= iss_latitude >= (MY_LAT - 5) and (MY_LONG + 5) >= iss_longitude >= (MY_LONG - 5):
        return True


def is_night():
    time.sleep(60)
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True


while True:
    # BONUS: run the code every 60 seconds.
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg=f"Subject: Look Up ! \n\n ISS is close.")





