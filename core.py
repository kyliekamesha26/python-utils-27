import functools
import time
from typing import Any, Callable, Dict, Tuple


class MemoizedPipeline:
    def __init__(self, maxsize: int = 128, ttl: float = 60.0):
        self.maxsize = maxsize
        self.ttl = ttl
        self._cache: Dict[Tuple[Any, ...], Tuple[float, Any]] = {}

    def memoize(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in self._cache:
                timestamp, result = self._cache[key]
                if now - timestamp < self.ttl:
                    return result

            result = func(*args, **kwargs)
            if len(self._cache) >= self.maxsize:
                oldest_key = min(self._cache, key=lambda k: self._cache[k][0])
                del self._cache[oldest_key]

            self._cache[key] = (now, result)
            return result

        return wrapper

    def clear(self) -> None:
        self._cache.clear()
