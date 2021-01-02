import requests
from json import load
from random import randint
from os.path import join
from sys import path
import unittest

file_name = join(path[0],'app','api_tests' ,'registered_ids.json')
f = open(file_name)
locales = load(f)['locales']
random_id = randint(0, len(locales))

BASE = f"http://127.0.0.1:5000/city?id={locales[random_id]}"

class Test_get_city_from_api(unittest.TestCase):
    def test_response_is_converted_to_json(self):
        requests.get(BASE).json()
# print(response.json())
