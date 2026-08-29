import re
from typing import Any


def validate_email(value: str) -> bool:
    if not isinstance(value, str) or not value:
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, value) is not None


def validate_url(value: str) -> bool:
    if not isinstance(value, str) or not value:
        return False
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
    return re.match(pattern, value) is not None


def validate_phone(value: str) -> bool:
    if not isinstance(value, str) or not value:
        return False
    cleaned = re.sub(r"[\s\-\(\)]", "", value)
    pattern = r"^\+?\d{10,15}$"
    return re.match(pattern, cleaned) is not None


def validate_age(value: Any) -> bool:
    try:
        age = int(value)
        return 0 < age < 150
    except (ValueError, TypeError):
        return False


def validate_positive_int(value: Any) -> bool:
    try:
        num = int(value)
        return num > 0
    except (ValueError, TypeError):
        return False


def validate_non_empty_string(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    return len(value.strip()) > 0


def validate_list_not_empty(value: Any) -> bool:
    if not isinstance(value, list):
        return False
    return len(value) > 0


def validate_dict_keys(value: Any, required_keys: list) -> bool:
    if not isinstance(value, dict):
        return False
    return all(key in value for key in required_keys)


def validate_ip_address(value: str) -> bool:
    if not isinstance(value, str) or not value:
        return False
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(pattern, value) is not None