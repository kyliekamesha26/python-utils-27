from typing import Any, Iterable, Optional, TypeVar

T = TypeVar('T')

def flatten(items: Iterable[Any]) -> list[Any]:
    """Flatten a nested list structure into a single list."""
    result: list[Any] = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def chunk(items: list[T], size: int) -> list[list[T]]:
    """Split a list into smaller lists of fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]

def get_nested(data: dict[Any, Any], keys: list[str], default: Optional[Any] = None) -> Any:
    """Access deeply nested dictionary values safely."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current