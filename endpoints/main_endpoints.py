import requests
from data_for_tests.urls import *
from data_for_tests.users import *


# Функция для получения токена авторизации
def get_auth_token():
    data = {"username": users["tester"]["username"], "password": users["tester"]["password"]}
    response = requests.post(BASE_URL_LOGIN, json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()["access_token"]


# Заголовки для запросов
HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'http://91.227.17.182',
    'Referer': 'http://91.227.17.182/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'service': 'eputs',
}
