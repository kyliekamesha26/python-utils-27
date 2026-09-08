import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config = defaults or {}

    def load_from_file(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                self._config.update(file_data)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __repr__(self) -> str:
        return f"ConfigLoader(keys={list(self._config.keys())})"

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()