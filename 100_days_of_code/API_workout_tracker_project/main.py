import requests

API_KEY = "1cd8219f2de0179a9833f0ce1e642bdf"
APP_ID = "a81deb91"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
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
print(response.text, result)