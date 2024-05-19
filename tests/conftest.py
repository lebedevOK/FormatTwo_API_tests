import pytest
from endpoints.main_endpoints import get_auth_token


@pytest.fixture
def auth_token():
    return get_auth_token()
