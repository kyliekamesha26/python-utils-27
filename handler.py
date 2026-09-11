from typing import Any, Dict, Generator, Iterable, List


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "_"
) -> Dict[str, Any]:
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def safe_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
        if current is None:
            return default
    return current


def chunk_data(data: Iterable[Any], size: int) -> Generator[List[Any], None, None]:
    chunk = []
    for item in data:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
