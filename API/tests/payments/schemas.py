# 📄 API/tests/payments/schemas.py
payments_schema = {
    "type": "object",
    "required": ["id", "booking_id", "status", "amount", "payment_method"],
    "properties": {
        "id": {"type": "string"},
        "booking_id": {"type": "string"},
        "status": {
            "type": "string",
            "enum": ["pending", "success", "failed"]
        },
        "amount": {"type": "number"},
        "payment_method": {
            "type": "string",
            "enum": ["credit_card", "paypal", "bank_transfer"]  # ajusta a los métodos reales soportados
        }
    }
}
