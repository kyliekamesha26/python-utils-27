import json
import os
from typing import Any, Dict, List, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    return [items[i:i + size] for i in range(0, len(items), size)]

def get_env(key: str, default: Optional[str] = None) -> str:
    return os.environ.get(key, default or "")

def flatten_list(nested: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested for item in sublist]

def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance