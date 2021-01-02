# import requests
from requests import get
from flask_restful import fields, marshal_with

BASE = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'
DAYS = '/days/15'
TOKEN = '?token=b22460a8b91ac5f1d48f5b7029891b53'


def get_city_forecast(id):
    id = str(id)
    return get(BASE+id+DAYS+TOKEN).json()
