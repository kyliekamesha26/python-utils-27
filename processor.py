from typing import Any, Dict, List


class ValidationError(ValueError):
    """Raised when input data fails validation checks."""
    pass


def validate_payload(data: Any) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")

    if "id" not in data:
        raise ValidationError("Missing required field: id")

    if not isinstance(data["id"], (int, str)):
        raise ValidationError("Field 'id' must be an integer or string")

    if "value" not in data:
        raise ValidationError("Missing required field: value")

    return data


def process_inputs(inputs: List[Any]) -> List[Dict[str, Any]]:
    processed_results = []
    for index, item in enumerate(inputs):
        try:
            validated = validate_payload(item)
            processed_results.append({
                "id": validated["id"],
                "status": "success",
                "data": validated["value"]
            })
        except ValidationError as err:
            processed_results.append({
                "index": index,
                "status": "failed",
                "error": str(err)
            })
    return processed_results