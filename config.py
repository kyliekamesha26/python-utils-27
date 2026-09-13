import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self._defaults = defaults or {}
        self._config = self._defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self._update_deep(self._config, data)

    def load_from_env(self, prefix: str = "") -> None:
        for key, val in os.environ.items():
            if prefix and not key.startswith(prefix):
                continue
            clean_key = (key[len(prefix):] if prefix else key).lower()
            if clean_key in self._config:
                default_val = self._config[clean_key]
                if isinstance(default_val, bool):
                    self._config[clean_key] = val.lower() in ('true', '1', 'yes')
                elif isinstance(default_val, int):
                    self._config[clean_key] = int(val)
                elif isinstance(default_val, float):
                    self._config[clean_key] = float(val)
                else:
                    self._config[clean_key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def data(self) -> Dict[str, Any]:
        return self._config

    def _update_deep(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        for key, val in source.items():
            if isinstance(val, dict) and isinstance(target.get(key), dict):
                self._update_deep(target[key], val)
            else:
                target[key] = val