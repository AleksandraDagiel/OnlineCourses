import datetime

import requests

USERNAME = "studentaccount"
TOKEN = "udemytokentrial"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating a user
response = requests.post(url=pixela_endpoint, json=pixela_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Learning Graph",
    "unit": "min",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# Create a graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Add a pixel
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.datetime.now()

pixela_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    # "date": "20220312",
    "quantity": "100",
}

response = requests.post(url=pixel_endpoint, json=pixela_pixel_config, headers=headers)

# Update the pixel
yesterday = str((today - datetime.timedelta(days=1)).strftime("%Y%m%d"))

put_endpoint = f"{pixel_endpoint}/{yesterday}"
pixel_update_config = {
    "quantity": "20",
}
response = requests.put(url=put_endpoint, json=pixel_update_config, headers=headers)


# Delete a pixel
response = requests.delete(url=put_endpoint, headers=headers)
print(response.text)
