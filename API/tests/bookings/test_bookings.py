import requests
import random
import string
from jsonschema import validate
from API.tests.bookings.schema import booking_schema
from API.utils.settings import BASE_URL, BOOKING, FLIGHT

import uuid
import requests
from API.utils.settings import BASE_URL, BOOKING, FLIGHT

def random_id():
    return str(uuid.uuid4())[:8]

def test_create_booking_success(auth_headers):
    # 1. Crear aircraft
    aircraft_data = {
        "model": "Boeing 737",
        "capacity": 180,
        "tail_number": f"XA-{random_id()[:6]}"  # ✅ máximo 10 caracteres
    }

    aircraft_response = requests.post(f"{BASE_URL}/aircrafts", json=aircraft_data, headers=auth_headers, timeout=5)
    assert aircraft_response.status_code in [200, 201], f"Aircraft creation failed: {aircraft_response.text}"

    # Obtener ID real del aircraft creado
    aircraft_response_data = aircraft_response.json()
    aircraft_id = aircraft_response_data["id"]

    # 2. Crear vuelo con aircraft_id válido
    flight_data = {
        "origin": "MEX",
        "destination": "JFK",
        "departure_time": "2025-10-01T10:00:00",
        "arrival_time": "2025-10-01T14:00:00",
        "base_price": 250.0,
        "aircraft_id": aircraft_id
    }

    flight_response = requests.post(f"{BASE_URL}{FLIGHT}", json=flight_data, headers=auth_headers, timeout=5)
    print("Flight status:", flight_response.status_code)
    print("Flight body:", flight_response.text)
    assert flight_response.status_code in [200, 201], f"Flight creation failed: {flight_response.text}"

    # ✅ Obtener el ID correcto del vuelo
    flight_response_data = flight_response.json()
    flight_id = flight_response_data["id"]


    # 3. Crear booking con el flight_id real
    booking_data = {
        "flight_id": flight_id,
        "passengers": [
            {
                "full_name": "Ana García",
                "passport": "B98765432",
                "seat": "15B"
            }
        ]
    }

    booking_response = requests.post(f"{BASE_URL}{BOOKING}", json=booking_data, headers=auth_headers, timeout=5)
    assert booking_response.status_code in [200, 201], f"Booking creation failed: {booking_response.text}"

def test_create_booking_missing_passport(auth_headers):
    booking_data = {
        "id": random_id(),
        "flight_id": random_id(),
        "user_id": random_id(),
        "status": "draft",
        "passengers": [
            {
                "full_name": "Carlos Ruiz",
                # Falta el campo "passport"
                "seat": "22C"
            }
        ]
    }

    response = requests.post(f"{BASE_URL}{BOOKING}", json=booking_data, headers=auth_headers, timeout=5)
    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.json()}")

    # FastAPI devuelve 422 para errores de validación
    assert response.status_code == 422, f"Expected 422, got: {response.status_code}"

    # Validar que el error esté relacionado con "passport"
    error_response = response.json()
    error_detail = str(error_response).lower()
    assert "passport" in error_detail, f"Expected error mentioning 'passport', got: {error_response}"
