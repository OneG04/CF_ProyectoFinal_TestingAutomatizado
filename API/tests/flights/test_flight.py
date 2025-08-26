from API.utils.settings import FLIGHT, BASE_URL
import requests
from jsonschema import validate

flight_schema = {
    "type": "object",
    "required" : ["origin", "destination", "departure_time", "arrival_time", "base_price", "aircraft_id"],
    "properties": {
        "origin":{"type": "string","minLength": 3, "maxLength": 3},
        "destination":{"type": "string","minLength": 3, "maxLength": 3},
        "departure_time":{"type": "string", "format": "date-time"},
        "arrival_time":{"type": "string", "format": "date-time"},
        "base_price":{"type": "number", "minimum": 0},
        "aircraft_id":{"type": "string"}
    },
    "additionalProperties": False
}

def test_create_flight_schema(flight):
    validate(instance=flight, schema=flight_schema)

def test_get_all_flight_bug_found(flight, auth_headers):
    r = requests.get(f"{BASE_URL}{FLIGHT}", headers=auth_headers)
    lista = r.text
    assert r.status_code == 500
    assert lista != ""