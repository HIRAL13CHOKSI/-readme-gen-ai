```markdown
# Python Network Scanner
A simple tool for scanning and identifying devices on a network.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-GPLv3-blue)

## Overview
Python Network Scanner is a utility designed to scan a network and identify connected devices. It categorizes devices into known and unknown based on a predefined list. This tool leverages several third-party libraries to facilitate device detection and representation.

### Notable Features
- Creates a comprehensive list of devices on the network.
- Differentiates between known and unknown devices.

## Requirements
- **Python Version**: 3.x
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies
### Standard Library Modules
- `datetime`
- `json`
- `os`
- `sys`

### Third-Party Packages
- `device`
- `getmac`
- `network`
- `prettytable`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, you can use the provided `requirements.txt` file:

```bash
pip install -r ..\requirements.txt
```

For an editable install, run:

```bash
pip install -e .
```

## Usage
To run the network scanner, execute the following command:

```bash
python Network_Scanner.py
```

## Flags
None

## Environment Variables
| Name | Default | Description |
|------|---------|-------------|
| None specified | - | Controls runtime behavior |

## Examples
1. **Basic Network Scan**:
   ```bash
   python Network_Scanner.py
   ```

2. **Using Docker**: (Note: No Dockerfile is provided)
   ```bash
   # Docker build/run commands would go here if applicable
   ```

## Input/Output
| Input | Output |
|-------|--------|
| Network configuration | List of devices categorized as known or unknown |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Unable to detect devices on the network.
  - **Solution**: Ensure that you have the necessary permissions and that your network settings allow device discovery.
  
- **Issue**: Missing dependencies.
  - **Solution**: Verify that all required packages are installed as per the `requirements.txt`.

## Contributing
Coming soon.

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://www.gnu.org/licenses/) for more details.
```
