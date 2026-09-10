import functools
from typing import Any, Callable, Dict

_CACHE: Dict[tuple, Any] = {}

def memoize_validator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

@memoize_validator
def validate_schema(data: dict, schema: dict) -> bool:
    if not isinstance(data, dict) or not isinstance(schema, dict):
        return False
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def clear_validator_cache() -> None:
    _CACHE.clear()

class DataValidator:
    __slots__ = ('schema',)

    def __init__(self, schema: dict):
        self.schema = schema

    def validate(self, data: dict) -> bool:
        return validate_schema(data, self.schema)