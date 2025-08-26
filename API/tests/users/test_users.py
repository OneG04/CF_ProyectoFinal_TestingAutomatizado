from API.utils.settings import BASE_URL, USERS
from API.utils.fixture_utils import *
import requests
from jsonschema import validate

user_schema = {
    "type": "object",
    "required": ["id", "email", "full_name", "role"],
    "properties": {
        "id": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "full_name": {"type": "string"},
        "role": {"type": "string", "enum":["passenger", "admin"]}
    },
    "additionalProperties": True
}

def test_create_user_schema(user):
    validate(instance=user, schema=user_schema)

def test_get_all_user(auth_headers, limit=50):
    skip = 0
    results = []

    while True:
        r = requests.get(f"{BASE_URL}{USERS}", params={"skip": skip, "limit": limit}, headers=auth_headers, timeout=5)
        r.raise_for_status()
        users_list = r.json()

        if not users_list:
            break
        results.extend(users_list)
        skip += limit

    return results