import json
from decimal import Decimal

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)  # Convert Decimal to string for JSON serialization
        return super().default(o)
