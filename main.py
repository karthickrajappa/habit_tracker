import requests
from datetime import datetime
USERNAME = "kenkaneki"
TOKEN = "!HTeXp7P+w6CNO"
GRAPH_ID = "test1"
PIXELA_USER_VIEW = "https://pixe.la/v1/users/kenkaneki/graphs/test1.html"
pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "test1",
    "name": "Coding",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_config = {
    "date": formatted_date,
    "quantity": input("How many hours did you spent in coding? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_config = {
    "quantity": "2"
}

update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)
delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
