import pytest
from jsonschema import ValidationError
from jsonschema import validate


from API.tests.payments.conftest import payments

payments_schema = {
    "type": "object",
    "required": ["id","booking_id","status"],
    "properties":{
        "id": {"type": "string"},
        "booking_id":{"type": "string"},
        "status": {
            "type": "string",
            "enum": ["pending", "success","failed"]  #restricción solo 3 values
        }
    },
    "additionalProperties": False
}

def test_create_payment_schema(payment):
    validate(instance=payment, schema=payments_schema)

def test_has_valid_status(payment):
    assert payment["status"] in ["pending", "success", "failed"]

def test_wrong_status_fail_schema():
    invalid_payment = {
        "id": "def456",
        "booking_id": "87",
        "status": "draft"
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_payment, schema=payments_schema)

def test_no_empty_booking_id(payment):
    assert isinstance(payment["booking_id"], str) and payment["booking_id"].strip(), "El booking_id está vacío o no es válido"

