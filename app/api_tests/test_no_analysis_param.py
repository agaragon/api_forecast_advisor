import requests

BASE = "http://127.0.0.1:5000/analysis?"
FIRST_PARAM = "initial_date=hello&"
SECOND_PARAM = "final_date=world&"

response = requests.get(BASE+FIRST_PARAM+SECOND_PARAM)
print(response.json())
