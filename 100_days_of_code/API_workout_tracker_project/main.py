import requests
import datetime as dt
import os

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
AUTH_BEARER = os.environ.get("AUTH_BEARER")

HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

TOKEN = {
    "Authorization": f"Bearer {AUTH_BEARER}",
}

user_input = input("Tell me which exercise you did: ")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
parameters = {
    "query": user_input,
    "gender": "female",
    "weight_kg": 56,
    "height_cm": 163,
    "age": 29,
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=HEADERS)
result = response.json()

today = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    exercise_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=exercise_params, headers=TOKEN)
    print(response.text)
