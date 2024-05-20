from endpoints.main_endpoints import *


# Тест на получение версии
def test_get_version():
    response = requests.get(BASE_URL_VERSION, headers=HEADERS)
    assert response.status_code == 200
    assert "version" in response.json()
    assert isinstance(response.json()["version"], str)


# Тест на авторизацию
def test_login(auth_token):
    data = {"username": users["tester"]["username"], "password": users["tester"]["password"]}
    response = requests.post(BASE_URL_LOGIN, json=data, headers=HEADERS)
    assert response.status_code == 200
    assert auth_token is not None


# Тест на получение профиля пользователя
def test_get_profile(auth_token):
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.get(BASE_URL_PROFILE, headers=headers)
    assert response.status_code == 200
    assert "data" in response.json()
    assert "id" in response.json()["data"]
    assert "first_name" in response.json()["data"]
    assert "last_name" in response.json()["data"]
    assert "email" in response.json()["data"]
    assert "is_active" in response.json()["data"]
    assert "avatar_url" in response.json()["data"]


# Тест на получение доступных сервисов
def test_get_services(auth_token):
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.get(BASE_URL_SERVICES, headers=headers)
    assert response.status_code == 200


# Тест на получение фильтров
def test_get_filters(auth_token):
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.get(BASE_URL_FILTER, headers=headers)
    assert response.status_code == 200
