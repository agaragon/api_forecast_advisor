import requests
from json import load
from random import randint
from os.path import join
from sys import path

file_name = join(path[0], 'registered_ids.json')
f = open(file_name)
locales = load(f)['locales']
random_id = randint(0, len(locales))

BASE = f"http://127.0.0.1:5000/city?id={locales[random_id]}"

response = requests.get(BASE)
print(response.json())
