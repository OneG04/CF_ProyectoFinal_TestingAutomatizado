from API.utils.settings import BASE_URL, USERS
from API.utils.fixture_utils import auth_headers
import os
import random
import string

import requests, pytest, faker
from dotenv import load_dotenv

load_dotenv()
fake =faker.Faker()


@pytest.fixture
def user(auth_headers, role: str = "passenger"):

    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "full_name": fake.name(),
        "role": role
    }

    r= requests.post(f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers, timeout=5)
    r.raise_for_status()
    user_created = r.json()
    yield user_created
    requests.delete(f"{BASE_URL}{USERS}/{user_created['id']}", headers=auth_headers,timeout=5)