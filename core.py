from typing import Any, Iterable, Dict, List, Optional

def deep_update(base: Dict[Any, Any], update: Dict[Any, Any]) -> Dict[Any, Any]:
    for key, value in update.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base

def chunk_list(data: Iterable[Any], size: int) -> List[List[Any]]:
    if size <= 0:
        raise ValueError("chunk size must be positive")
    data_list = list(data)
    return [data_list[i:i + size] for i in range(0, len(data_list), size)]

def filter_none(data: Dict[Any, Any]) -> Dict[Any, Any]:
    return {k: v for k, v in data.items() if v is not None}

def pluck(data: List[Dict[Any, Any]], key: Any, default: Any = None) -> List[Any]:
    return [item.get(key, default) for item in data]

def flatten(data: Iterable[Any]) -> List[Any]:
    result = []
    for item in data:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result