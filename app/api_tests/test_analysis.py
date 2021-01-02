import requests
import unittest


BASE = "http://127.0.0.1:5000/analysis?"
FIRST_PARAM = "initial_date=2020-12-01&"
SECOND_PARAM = "final_date=2021-01-05&"


class Test_analysis(unittest.TestCase):
    def test_analysis_response_is_converted_to_json(self):
        requests.get(BASE+FIRST_PARAM+SECOND_PARAM).json()
