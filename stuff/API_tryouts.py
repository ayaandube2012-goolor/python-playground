import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    response.raise_for_status()

data = response.json()["iss_position"]

longitude = data["longitude"]
latitude = data["latitude"]

iss_position = (latitude, longitude)
print(iss_position)
