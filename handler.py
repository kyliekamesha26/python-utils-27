import json
from typing import Any, Dict, Optional

class DataHandler:
    @staticmethod
    def serialize(data: Any) -> str:
        try:
            return json.dumps(data, sort_keys=True)
        except (TypeError, ValueError):
            return ""

    @staticmethod
    def deserialize(data: str) -> Optional[Dict[str, Any]]:
        try:
            return json.loads(data)
        except (json.JSONDecodeError, TypeError):
            return None

    @staticmethod
    def flatten(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
        items = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(DataHandler.flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    @staticmethod
    def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
        keys = path.split('.')
        val = data
        try:
            for key in keys:
                val = val[key]
            return val
        except (KeyError, TypeError):
            return default