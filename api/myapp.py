import requests

URL = "http://127.0.0.1:8000/stulist/"

data = requests.get(url=URL)

d = data.json()

print(d)
