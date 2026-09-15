import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


def validate_item(item: Any) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise ValidationError(f"Expected dictionary, got {type(item).__name__}")

    item_id = item.get("id")
    if item_id is None:
        raise ValidationError("Missing required field: 'id'")

    try:
        item_id = int(item_id)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid 'id' value: {item_id}")

    value = item.get("payload")
    if value is None:
        raise ValidationError("Missing required field: 'payload'")

    return {"id": item_id, "payload": value}


def process_batch(items: List[Any]) -> List[Dict[str, Any]]:
    processed = []
    if not isinstance(items, list):
        logger.error("Input data must be a list")
        return processed

    for index, item in enumerate(items):
        try:
            validated_item = validate_item(item)
            processed.append(validated_item)
        except ValidationError as error:
            logger.warning(
                "Skipping item at index %d due to validation failure: %s",
                index,
                error,
            )
    return processed
