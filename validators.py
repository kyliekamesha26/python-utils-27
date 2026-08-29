import re
from typing import Any, Optional


def is_valid_email(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, value) is not None


def is_valid_url(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
    return re.match(pattern, value) is not None


def is_valid_phone(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    digits = re.sub(r"[^0-9]", "", value)
    return 10 <= len(digits) <= 15


def is_valid_ip_address(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(pattern, value) is not None


def is_positive_integer(value: Any) -> bool:
    try:
        num = int(value)
        return num > 0
    except (ValueError, TypeError):
        return False


def is_valid_length(value: Any, min_len: int = 1, max_len: Optional[int] = None) -> bool:
    if not isinstance(value, str):
        return False
    length = len(value)
    if length < min_len:
        return False
    if max_len is not None and length > max_len:
        return False
    return True