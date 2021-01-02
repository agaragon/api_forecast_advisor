import requests
import unittest

BASE = "http://127.0.0.1:5000/analysis?"
FIRST_PARAM = "initial_date=hello&"
SECOND_PARAM = "final_date=world&"


class Test_no_analysis_param_wont_crash(unittest.TestCase):
    def test_response_is_converted_to_json(self):
        requests.get(BASE+FIRST_PARAM+SECOND_PARAM).json()
