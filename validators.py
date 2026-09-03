from typing import Any, Optional, Union


def validate_email(email: str) -> bool:
    """Validate email string format."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return len(email.split("@")[0]) > 0


def validate_int_range(value: int, min_val: int, max_val: int) -> bool:
    """Check if integer is within inclusive bounds."""
    return min_val <= value <= max_val


def validate_required(value: Any) -> bool:
    """Ensure input is not None or empty."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict, set)):
        return len(value) > 0
    return True


def sanitize_input(value: Optional[str]) -> str:
    """Remove whitespace and cast to string."""
    return str(value).strip() if value else ""


def validate_payload(data: dict, schema: dict) -> bool:
    """Verify dictionary keys against a schema mapping."""
    return all(k in data and isinstance(data[k], v) for k, v in schema.items())