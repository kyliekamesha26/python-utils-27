from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

class Config:
    """Configuration holder."""

    def __init__(self, data: Optional[Dict[str, Any]] = None) -> None:
        """Initialize with data dict."""
        self._data: Dict[str, Any] = data or {}
        for k, v in self._data.items():
            if isinstance(v, dict):
                setattr(self, k, Config(v))
            else:
                setattr(self, k, v)

    @classmethod
    def from_file(cls, path: Path) -> Config:
        """Load from JSON file."""
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        return cls(data)

    @classmethod
    def from_env(cls, prefix: str = "CONFIG_") -> Config:
        """Load from environment variables."""
        config: Dict[str, Any] = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                ckey = key[len(prefix):].lower()
                if value.isdigit():
                    config[ckey] = int(value)
                elif value.lower() in {"true", "false"}:
                    config[ckey] = value.lower() == "true"
                else:
                    config[ckey] = value
        return cls(config)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get value by key or default."""
        keys = key.split(".")
        val: Any = self._data
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                return default
        return val

    def set(self, key: str, value: Any) -> None:
        """Set value for key."""
        keys = key.split(".")
        curr: Dict[str, Any] = self._data
        for k in keys[:-1]:
            if k not in curr or not isinstance(curr[k], dict):
                curr[k] = {}
            curr = curr[k]
        curr[keys[-1]] = value
        setattr(self, keys[-1], value)

    def to_dict(self) -> Dict[str, Any]:
        """Return config as dict."""
        return self._data.copy()