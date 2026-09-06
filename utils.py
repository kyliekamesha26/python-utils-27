import time
from typing import Any, Callable, Dict, Generator, List, TypeVar

T = TypeVar("T")


def chunk_list(lst: List[T], size: int) -> Generator[List[T], None, None]:
    """Split a list into chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


def deep_merge(dict_a: Dict[Any, Any], dict_b: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge dictionary b into dictionary a."""
    result = dict_a.copy()
    for key, value in dict_b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def retry(retries: int = 3, delay: float = 0.1) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Retry decorator with specified attempts and delay."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_exception = Exception("Unknown failure")
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise last_exception

        return wrapper

    return decorator
