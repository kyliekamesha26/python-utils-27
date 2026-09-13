import json
from pathlib import Path
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self._config = defaults or {}

    def load(self, path: str) -> None:
        file = Path(path)
        if file.exists():
            with open(file, 'r') as f:
                self._config.update(json.load(f))

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()