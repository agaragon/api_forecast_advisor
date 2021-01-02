import requests

BASE = "http://127.0.0.1:5000/analysis?"
FIRST_PARAM = "initial_date=2020-12-01&"
SECOND_PARAM = "final_date=2021-01-05&"

response = requests.get(BASE+FIRST_PARAM+SECOND_PARAM)
print(response.json())
