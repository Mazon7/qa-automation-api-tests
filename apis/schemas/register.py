# schemas/regiser.py
valid_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
        "email_newsletter": {"type": "boolean"},
        "referral": {"type": "string"},
        "telegram_username": {"type": "string"}
    },
    "required": ["email", "password"]
}
