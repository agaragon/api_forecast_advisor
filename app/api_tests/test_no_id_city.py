from requests import get
import unittest

class Test_no_id_city(unittest.TestCase):
    def test_response_is_converted_to_json(self):
        get("http://127.0.0.1:5000/city?id=1").json()
