from typing import Any, Dict, List, Optional


class DataProcessor:
    def __init__(self, required_keys: Optional[List[str]] = None):
        self.required_keys = required_keys or ["id", "payload"]

    def validate_input(self, item: Any) -> bool:
        if not isinstance(item, dict):
            return False
        for key in self.required_keys:
            if key not in item or item[key] is None:
                return False
        return True

    def process_stream(self, stream: List[Any]) -> List[Dict[str, Any]]:
        results = []
        for raw_data in stream:
            if not self.validate_input(raw_data):
                continue

            payload = raw_data["payload"]
            if not isinstance(payload, (str, bytes, list, dict)):
                continue

            results.append({
                "id": raw_data["id"],
                "processed": True,
                "size": len(payload)
            })
        return results
