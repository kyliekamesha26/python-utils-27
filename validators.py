from typing import Any, Optional, Union


def validate_email(email: str) -> bool:
    """Validate string format against basic email structure."""
    if not isinstance(email, str) or "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and all(parts)


def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if numeric value is within inclusive bounds."""
    return min_val <= value <= max_val


def validate_length(data: str, min_len: int, max_len: Optional[int] = None) -> bool:
    """Verify string length constraints."""
    if not isinstance(data, str):
        return False
    if max_len is not None and len(data) > max_len:
        return False
    return len(data) >= min_len


def validate_type(obj: Any, expected_type: type) -> bool:
    """Check instance type of provided object."""
    return isinstance(obj, expected_type)