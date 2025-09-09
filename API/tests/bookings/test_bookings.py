from random import random
import string

import requests
from jsonschema import validate

from API.utils.settings import BOOKING
from API.utils.settings import BASE_URL

booking_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "flight_id": {"type": "string"},
        "user_id": {"type": "string"},
        "status": {"type": "string"},
        "passengers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "full_name": {"type": "string"},
                    "passport": {"type": "string"},
                    "seat": {"type": "string"}
                },
                "required": ["full_name", "passport", "seat"]
            }
        }
    },
    "required": ["id", "flight_id", "user_id", "status", "passengers"]
}

def test_create_booking_schema(booking):
    validate(instance=booking, schema=booking_schema)

def test_get_all_bookings_bug_found(flight, auth_headers):
    r = requests.get(f"{BASE_URL}{BOOKING}", headers=auth_headers)
    lista = r.text
    assert r.status_code == 500
    assert lista != ""
