import time
from functools import wraps
from typing import Callable, Any, Dict, Tuple

def memoize_with_ttl(ttl: float) -> Callable:
    cache: Dict[Tuple[Any, ...], Tuple[Any, float]] = {}

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            now = time.monotonic()
            key = (args, tuple(sorted(kwargs.items()))) if kwargs else args
            if key in cache:
                val, expiry = cache[key]
                if now < expiry:
                    return val
            result = func(*args, **kwargs)
            cache[key] = (result, now + ttl)
            return result

        def cache_clear() -> None:
            cache.clear()

        wrapper.cache_clear = cache_clear  # type: ignore
        return wrapper
    return decorator

def fast_flatten(d: Dict[str, Any], sep: str = ".") -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    stack = [(d, "")]
    while stack:
        curr, prefix = stack.pop()
        for k, v in curr.items():
            new_key = f"{prefix}{sep}{k}" if prefix else k
            if isinstance(v, dict) and v:
                stack.append((v, new_key))
            else:
                result[new_key] = v
    return result