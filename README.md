[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-27

A lightweight collection of production-ready Python helper utilities designed to streamline file I/O, dictionary manipulations, and performance tracking. Built to eliminate redundant boilerplate across Python 3.8+ projects and microservices.

## Features

* **Safe File Operations:** Atomic JSON and YAML reading/writing with automatic fallback handling and UTF-8 encoding defaults.
* **Dictionary Transformation:** Deep dictionary flattening and unflattening with custom separator support.
* **Execution Profiling:** Thread-safe execution time decorators with customizable logging hooks.
* **String Sanitization:** Fast slugification and text cleaning utilities tuned for pipeline processing.

## Installation

Install the package directly via `pip`:

```bash
pip install python-utils-27
```

Or install the latest development version directly from source:

```bash
pip install git+https://github.com/Developer/python-utils-27.git
```

## Quick Start

```python
from python_utils_27 import timed, safe_json_load, flatten_dict

# Track function execution duration automatically
@timed(logger_name="app.performance")
def Process_user_data():
    # Safely parse JSON with fallback on missing or corrupt files
    raw_config = safe_json_load("settings.json", default={"system": {"active": True}})
    
    # Transform nested structures into single-level key-value pairs
    flat_config = flatten_dict(raw_config, delimiter=".")
    
    return flat_config

if __name__ == "__main__":
    result = process_user_data()
    print(result)
    # Output: {'system.active': True}
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.