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
            },
        },
    },
}