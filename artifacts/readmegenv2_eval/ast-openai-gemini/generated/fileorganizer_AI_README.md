```markdown
# File Organizer
A script to organize files into subfolders based on their type.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue)

## Overview
File Organizer is a Python script that allows users to browse through any folder and move files into their respective subfolders based on file type. This tool simplifies file management by organizing files according to their extensions and creation dates.

### Notable Features
- Automatically sorts files into designated folders.
- Supports moving files based on their type.

## Requirements
- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies
### Standard Library
- `datetime`
- `os`
- `sys`

### Third-Party Packages
- `extensiondict`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, you can use the provided `requirements.txt` file:

```bash
pip install -r ../requirements.txt
```

For an editable install, run:

```bash
pip install -e .
```

## Usage
To run the script, use the following command:

```bash
python fileorganizer.py <arg>
```

## Flags
None

## Environment Variables
| Name | Default | Description |
|------|---------|-------------|
| None specified | - | Controls runtime behavior |

## Examples
1. Organize files in a specified directory:
   ```bash
   python fileorganizer.py /path/to/source /path/to/destination
   ```

2. Move files from one directory to another:
   ```bash
   python fileorganizer.py /path/to/source /path/to/destination
   ```

## Input/Output
| Input | Output |
|-------|--------|
| Source directory path | Organized files in destination directory |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Files are not moving as expected.
  - **Solution**: Ensure that the source and destination paths are correct and accessible.
  
- **Issue**: Script fails to run.
  - **Solution**: Verify that all dependencies are installed and that you are using a compatible Python version.

## Contributing
Coming soon.

## License
Coming soon.
```
