import requests
import os
from twilio.rest import Client


api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("OWM_ACC_SID")
auth_token = os.environ.get("OWM_AUTH_TOKEN")


params = {
    "lat": 51.209438,
    "lon": 17.378460,
    "appid": api_key,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                        params=params)
response.raise_for_status()
weather_data = response.json()
weather_data_12h = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_data_12h:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Remember to bring an umbrella.",
        from_='+12073604858',
        to='+48884617302'
    )
