import sys

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a dictionary")
    if "task_id" not in data or not isinstance(data["task_id"], int):
        raise ValueError("invalid or missing task_id")
    return True

def process_payload(data):
    print(f"Processing task: {data['task_id']}")
    return True

def main_loop(data_stream):
    for item in data_stream:
        try:
            validate_input(item)
            process_payload(item)
        except (ValueError, KeyError, TypeError) as e:
            print(f"Skipping invalid entry: {e}", file=sys.stderr)
            continue

if __name__ == "__main__":
    sample_data = [{"task_id": 1}, "invalid_data", {"task_id": 2}]
    main_loop(sample_data)