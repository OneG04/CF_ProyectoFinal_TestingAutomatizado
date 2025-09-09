from API.utils.settings import AUTH_LOGIN, AIRPORT, BASE_URL, BOOKING
from API.utils.api_helpers import api_request
import os
import pytest
import random
import string
import requests


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

@pytest.fixture
def booking (auth_headers):
    booking_data = {
            "id": "".join(random.choices(string.ascii_letters + string.digits, k=8)),
            "flight_id": "".join(random.choices(string.ascii_letters + string.digits, k=8)),
            "user_id": "".join(random.choices(string.ascii_letters + string.digits, k=8)),
            "status": "draft",
            "passengers": [
                {
                    "full_name": "Diana Vazquez",
                    "passport": "A12345678",
                    "seat": "12A"
                }
            ]
    }

    r = requests.post (f"{BASE_URL}{BOOKING}", json=booking_data, headers=auth_headers, timeout=5)
    # r.raise_for_status()
    booking_response = r.json()
    yield booking_response


