from datetime import date
import unittest
from helpers.convert_from_date_string import convert_from_date_string


class Test_convert_from_date_string(unittest.TestCase):
    def test_expected_values(self):
        self.assertEqual(convert_from_date_string(
            '1994-01-12'), date(1994, 1, 12))
        self.assertEqual(convert_from_date_string(
            '2020-03-10'), date(2020, 3, 10))
        self.assertEqual(convert_from_date_string(
            '2019-07-08'), date(2019, 7, 8))
        self.assertEqual(convert_from_date_string(
            '2017-03-02'), date(2017, 3, 2))
