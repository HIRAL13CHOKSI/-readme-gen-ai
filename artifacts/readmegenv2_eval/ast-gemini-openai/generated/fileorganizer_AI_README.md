```markdown
# File Organizer

A script to organize files in a directory into subfolders based on file type.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen)

## Overview

This Python script, `fileorganizer.py`, helps you declutter your directories by automatically sorting files into subfolders based on their file extensions. The script traverses a source directory and moves files to corresponding subdirectories within a destination directory, creating new subdirectories as needed.

Key features:

-   **Automated File Sorting**: Organizes files based on their extensions.
-   **Directory Traversal**: Recursively scans the source directory.
-   **Destination Management**: Creates subdirectories in the destination directory if they don't exist.

## Requirements

-   Python 3.7+
-   Any operating system that supports Python.

## Dependencies

### Standard Library

-   `datetime`
-   `os`
-   `sys`

### Third-Party Packages

-   `extensiondict`
-   `google-generativeai`
-   `groq`
-   `openai`

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r ..\requirements.txt
```

For an editable install, use:

```bash
pip install -e .
```

## Usage

```
python fileorganizer.py <arg>
```

## Flags

None

## Input/Output

| Input         | Output                                                                           |
| ------------- | -------------------------------------------------------------------------------- |
| Source folder | Files are moved into subfolders within the destination folder based on file type. |
| Destination folder | Contains the sorted subfolders with files.                                                                            |

## Examples

To run the script, navigate to the directory containing `fileorganizer.py` and execute it with the source directory as an argument:

```bash
python fileorganizer.py /path/to/source/directory
```

## Testing

This project includes tests. To run them, use `pytest`:

```bash
pytest
```

## Troubleshooting

-   **Permission Errors**: Ensure the script has the necessary permissions to read from the source directory and write to the destination directory.
-   **File Not Found Errors**: Double-check that the source directory path is correct and that the files exist.

## Contributing

Coming soon

## License

Coming soon
```
