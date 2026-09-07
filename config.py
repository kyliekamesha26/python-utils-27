import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults = defaults or {}
        self._config = self.defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        self._config.update(data)

    def load_from_json(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Config file not found: {filepath}')
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.load_from_dict(data)

    def load_from_env(self, prefix: str = '') -> None:
        for key in self._config:
            env_key = f'{prefix}{key.upper()}'
            if env_key in os.environ:
                val = os.environ[env_key]
                try:
                    self._config[key] = json.loads(val)
                except json.JSONDecodeError:
                    self._config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def data(self) -> Dict[str, Any]:
        return self._config.copy()
