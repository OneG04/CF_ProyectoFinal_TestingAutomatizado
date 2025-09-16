from API.utils.settings import AUTH_LOGIN, AIRPORT, BASE_URL
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
def airport(auth_headers):
    airport_data = {
        "iata_code": "".join(random.choices(string.ascii_uppercase, k=3)),
        "city": "La Paz",
        "country": fake.country_code()
    }
    r = requests.post(BASE_URL + AIRPORT, json=airport_data, headers=auth_headers, timeout=5)
    #r = api_request("post", BASE_URL + AIRPORT, json=airport_data, headers=auth_headers)
    r.raise_for_status()
    airport_response = r.json()
    yield airport_response
    requests.delete(BASE_URL + AIRPORT + f'{airport_response["iata_code"]}', headers=auth_headers, timeout=5)

@pytest.fixture
def invalid_airport(auth_headers):
    airport_data = {
        "iata_code": "".join(random.choices(string.ascii_uppercase, k=3)),
        #"city": "La Paz",
        "country": fake.country_code()
    }

@pytest.fixture
def create_airport():
    return {
        "iata_code": "".join(random.choices(string.ascii_uppercase, k=3)),
        "city": "La Paz",
        "country": fake.country_code()
    }