import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._defaults: Dict[str, Any] = defaults or {}
        self._config: Dict[str, Any] = self._defaults.copy()

    def load_file(self, path: str) -> None:
        if not os.path.isfile(path):
            return
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            self._config.update(data)

    def override_with_env(self, prefix: str = "APP_") -> None:
        for env_key, env_value in os.environ.items():
            if not env_key.startswith(prefix):
                continue
            key = env_key[len(prefix):].lower()
            self._config[key] = env_value

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    def all(self) -> Dict[str, Any]:
        return self._config.copy()

    def reset(self) -> None:
        self._config = self._defaults.copy()