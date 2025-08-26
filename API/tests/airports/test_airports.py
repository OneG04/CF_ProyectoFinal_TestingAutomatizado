import pytest
from API.utils.settings import AIRPORT, BASE_URL
import requests
from jsonschema import validate


airport_schema = {
    "type": "object",
    "required": ["iata_code", "city", "country"],
    "properties": {
        "iata_code":{"type": "string", "minLength": 3, "maxLength": 3},
        "city": {"type":"string"},
        "country": {"type":"string"}
    },
    "additionalProperties": False
}

def test_create_airport_schema(airport):
    validate(instance=airport, schema=airport_schema)

def test_get_all_airports(airport, auth_headers):
    r = requests.get(f"{BASE_URL}{AIRPORT}", headers=auth_headers)
    lista = r.text
    assert r.status_code ==200
    assert lista != ""

def test_invalid_airport(invalid_airport, auth_headers):
    r = requests.post(f"{BASE_URL}{AIRPORT}", headers=auth_headers)
    assert r.status_code == 422