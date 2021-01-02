from datetime import date


def convert_from_date_string(date_string):
    year, month, day = date_string.split('-')
    return date(int(year), int(month), int(day))
