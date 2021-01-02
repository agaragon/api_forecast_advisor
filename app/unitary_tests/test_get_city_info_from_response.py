import unittest
from json import load
from datetime import date
from helpers.get_city_info_from_response import get_city_info_from_response
from os.path import join
from sys import path

dictionary = {}
file_names = ['4134_2020-12-31.json',
              '4492_2020-12-31.json', '8438_2020-12-31.json']
answers = {}
answers[1] = {
    'id': 4134,
    'name': 'Fernão',
    'state': 'SP',
    'country': 'BR  ',
    'date': '2020-12-31',
    'probability': 67,
    'precipitation': 12,
    'min_temp': 22,
    'max_temp': 28
}
answers[2] = {
    'id': 4492,
    'name': 'Zortéa',
    'state': 'SC',
    'country': 'BR  ',
    'date': '2020-12-31',
    'probability': 90,
    'precipitation': 30,
    'min_temp': 20,
    'max_temp': 26
}
answers[3] = {
    'id': 8438,
    'name': 'Matões do Norte',
    'state': 'MA',
    'country': 'BR  ',
    'date': '2020-12-31',
    'probability': 83,
    'precipitation': 15,
    'min_temp': 25,
    'max_temp': 30
}


def populate_dictonary_for_testing(file_name):
    file_path = join(path[0], 'unitary_tests', 'api_responses', file_name)
    f = open(file_path)
    dictionary[len(dictionary)+1] = load(f)


for file_name in file_names:
    populate_dictonary_for_testing(file_name)


class Test_get_city_info_from_response(unittest.TestCase):
    def test_expected_values(self):
        self.assertDictEqual(get_city_info_from_response(
            dictionary[1], 0), answers[1])
        self.assertDictEqual(get_city_info_from_response(
            dictionary[2], 0), answers[2])
        self.assertDictEqual(get_city_info_from_response(
            dictionary[3], 0), answers[3])
