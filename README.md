# python-utils-27

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

python-utils-27 is a lightweight collection of utility functions designed to simplify common programming tasks in Python. It provides reliable tools for file handling, string manipulation, and data processing without unnecessary dependencies.

## Features
- Robust file operations that automatically create directories and handle common errors
- String utilities for generating slugs, truncating text, and sanitizing user input
- Dictionary helpers supporting deep merges and safe access to nested keys
- Date and time conversion functions with support for multiple input formats

## Installation

Install the package using pip:

```bash
pip install python-utils-27
```

To install from source:

```bash
git clone https://github.com/Developer/python-utils-27.git
cd python-utils-27
pip install -e .
```

## Usage

```python
from python_utils_27 import file_utils, string_utils

# Write content to a file, creating parent directories if needed
file_utils.write('output/data.txt', 'Sample content here')

# Convert a title to a URL slug
slug = string_utils.to_slug('Python Utils 27 - Helpful Tools')
print(slug)  # python-utils-27-helpful-tools
```