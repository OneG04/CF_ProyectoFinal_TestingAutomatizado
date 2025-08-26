from API.utils.settings import AUTH_LOGIN, BASE_URL, FLIGHT
from API.utils.api_helpers import api_request
import os
import random
import string

import requests, pytest, faker
from dotenv import load_dotenv

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
def flight(auth_headers):
    flight_data = {
        "origin": "".join(random.choices(string.ascii_uppercase, k=3)),
        "destination": "".join(random.choices(string.ascii_uppercase, k=3)),
        "departure_time": "2025-08-19T18:01:27.712Z",
        "arrival_time": "2025-08-19T18:01:27.712Z",
        "base_price": random.randint(500,2000),
        "aircraft_id": "string"
        #"aircraft_id": "".join(random.choices(string.digits, k=4))
    }
    r = requests.post(f"{BASE_URL}{FLIGHT}", json=flight_data, headers=auth_headers, timeout=5)
    #r.raise_for_status()
    flight_response = r.json()
    yield flight_response
    #requests.delete(f"{BASE_URL}{FLIGHT}/{flight_response["id"]}", json = flight_data, headers = auth_headers, timeout = 5)
    #requests.delete(BASE_URL + FLIGHT + f'{flight_response["id"]}', headers=auth_headers, timeout=5)