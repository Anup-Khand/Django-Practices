import requests
import json
# from api
# URL = "http://127.0.0.1:8000/list/"

# r = requests.get(url=URL)
# data = r.json()
# print(data)


# to api

URL = "http://127.0.0.1:8000/sc/"
data = {
    'name': 'Ram',
    'Age': 20,
    'City': 'Chitwan'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=data)
data = r.json()
print(data)
