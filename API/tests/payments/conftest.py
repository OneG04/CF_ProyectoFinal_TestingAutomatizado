import string
from random import random

import faker
import pytest
import requests

from API.utils.settings import PAYMENTS, BASE_URL, AUTH_LOGIN

load_dotenv()
fake =faker.Faker()

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
def payments(auth_headers):
    payment_data= {
        "id": "".join(random.choices(string.ascii_uppercase, k=3)),
        "booking_id": "".join(random.choices(string.ascii_uppercase, k=3)),
        "status": {
            "type": "string",
            "enum": ["pending", "success","failed"]  #restricción solo 3 values
        }
    }
    r = requests.post(f"{BASE_URL}{PAYMENTS}", json=payment_data, headers=auth_headers, timeout=5)
    #r.raise_for_status()
    flight_response = r.json()
    yield flight_response