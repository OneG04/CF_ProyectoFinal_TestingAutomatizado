from API.utils.settings import AUTH_LOGIN, BASE_URL
import os
import requests
import pytest

@pytest.fixture(scope="session")
def admin_token() -> str:

    user = os.getenv("ADMIN_USER")
    pwd = os.getenv("ADMIN_PASS")

    r = requests.post(BASE_URL + AUTH_LOGIN, data={"username": user, "password": pwd}, timeout = 5)
    r.raise_for_status()
    return r .json()["access_token"]

@pytest.fixture
def auth_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}