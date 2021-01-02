from requests import get
from json import load
from random import randint
from os.path import join
from sys import path
from datetime import date

filename = 'api_tests/registered_ids.json'
f = open(filename)
locales = load(f)['locales']
random_id = randint(0, len(locales))


BASE = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'
DAYS = '/days/15'
TOKEN = '?token=b22460a8b91ac5f1d48f5b7029891b53'


def get_api_response(id):
    today = str(date.today())
    response = get(BASE+str(id)+DAYS+TOKEN).json()
    file_path = join(path[0], 'api_responses', f'{id}_{today}.json')
    api_response_file = open(file_path, 'w')
    api_response_file.write(str(response))
    api_response_file.close()


if __name__ == '__main__':

    get_api_response(locales[random_id])
