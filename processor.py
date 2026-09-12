import sys

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a dictionary")
    if "payload" not in data:
        raise KeyError("missing mandatory payload field")
    return True

def process_stream(data_stream):
    for item in data_stream:
        try:
            if validate_input(item):
                print(f"processing: {item['payload']}")
        except (ValueError, KeyError) as e:
            print(f"validation error: {e}", file=sys.stderr)
        except Exception as e:
            print(f"unexpected system error: {e}", file=sys.stderr)

if __name__ == "__main__":
    test_data = [{"payload": "task_1"}, "invalid", {"invalid": "data"}]
    process_stream(test_data)