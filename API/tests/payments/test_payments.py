import pytest
import requests
import random
import string
from jsonschema import validate, ValidationError

from API.utils.settings import BASE_URL, PAYMENTS, AIRCRAFTS
from API.tests.payments.schemas import payments_schema  # ← Usamos este schema correctamente


def random_id(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


@pytest.fixture
def auth_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}


# ---------- TEST 1: Crear y obtener un payment ----------
def test_create_and_get_payment(auth_headers):
    # 1. Crear aircraft
    aircraft_data = {
        "model": "Boeing 737",
        "capacity": 180,
        "tail_number": f"XA-{random_id()[:6]}"  # ✅ máximo 10 caracteres
    }
    aircraft_response = requests.post("https://cf-automation-airline-api.onrender.com/aircrafts", json=aircraft_data,
                                      headers=auth_headers, timeout=5)

    assert aircraft_response.status_code in [200, 201], f"Aircraft creation failed: {aircraft_response.text}"

    # Obtener ID real del aircraft creado
    aircraft_response_data = aircraft_response.json()
    aircraft_id = aircraft_response_data["id"]

    # Crear flight_payload
    flight_payload = {
        "id": random_id(),
        "origin": "MEX",
        "destination": "JFK",
        "departure_time": "2025-09-30T10:00:00Z",
        "arrival_time": "2025-09-30T14:00:00Z",
        "price": 500.0,
        "base_price": 400.0,
        "airline": "AirTest",
        "aircraft_id": aircraft_id # <-- asegúrate que existe en tu DB
    }

    flight_response = requests.post(f"{BASE_URL}/flights", json=flight_payload, headers=auth_headers, timeout=5)
    assert flight_response.status_code in (200, 201), f"Flight creation failed: {flight_response.text}"
    flight_id = flight_response.json()["id"]

    booking_payload = {
        "id": random_id(),
        "user_id": "usr-123",  # asegúrate que este usuario exista
        "service": "flight",
        "date": "2025-09-30",
        "flight_id": flight_id,  # Usa un ID de vuelo que exista
        "passengers": [
            {
                "full_name": "John Doe",
                "age": 30,
                "passport": "A12345678"
            }
        ]
    }


    flight_response = requests.post(f"{BASE_URL}/flights", json=flight_payload, headers=auth_headers, timeout=5)
    assert flight_response.status_code in (200, 201), f"Flight creation failed: {flight_response.text}"
    flight_id = flight_response.json()["id"]

    booking_response = requests.post(f"{BASE_URL}/bookings", json=booking_payload, headers=auth_headers, timeout=5)
    assert booking_response.status_code in (200, 201), f"Booking creation failed: {booking_response.text}"

    booking_id = booking_response.json()["id"]

    payload = {
        "id": random_id(),
        "booking_id": booking_id,
        "status": random.choice(["pending", "success", "failed"]),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "payment_method": random.choice(["credit_card", "paypal", "bank_transfer"])
    }

    # POST
    post_response = requests.post(f"{BASE_URL}{PAYMENTS}", json=payload, headers=auth_headers, timeout=5)
    assert post_response.status_code in (200, 201), f"POST failed: {post_response.status_code} - {post_response.text}"

    created_payment = post_response.json()
    validate(instance=created_payment, schema=payments_schema)

    payment_id = created_payment["id"]

    # GET
    get_response = requests.get(f"{BASE_URL}{PAYMENTS}/{payment_id}", headers=auth_headers, timeout=5)
    assert get_response.status_code == 200, f"GET failed: {get_response.status_code} - {get_response.text}"

    fetched_payment = get_response.json()
    validate(instance=fetched_payment, schema=payments_schema)

    assert fetched_payment["id"] == payload["id"]
    assert fetched_payment["booking_id"] == payload["booking_id"]
    assert fetched_payment["status"] == payload["status"]

    # DELETE (opcional cleanup)
    delete_response = requests.delete(f"{BASE_URL}{PAYMENTS}/{payment_id}", headers=auth_headers)
    assert delete_response.status_code in (200, 204)


# ---------- TESTS 2-5: Usando fixture payments ----------
def test_create_payment_schema(payments):
    validate(instance=payments, schema=payments_schema)


def test_has_valid_status(payments):
    assert payments["status"] in ["pending", "success", "failed"]


def test_wrong_status_fail_schema():
    invalid_payment = {
        "id": "ABC123",
        "booking_id": "XYZ456",
        "status": "draft"  # inválido
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_payment, schema=payments_schema)


def test_no_empty_booking_id(payments):
    assert isinstance(payments["booking_id"], str)
    assert payments["booking_id"].strip() != "", "El booking_id está vacío o no es válido"

