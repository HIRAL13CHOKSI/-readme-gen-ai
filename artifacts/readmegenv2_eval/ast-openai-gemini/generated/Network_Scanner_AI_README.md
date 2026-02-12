```markdown
# Python Network Scanner
A simple tool for scanning and identifying devices on a network.

![License](https://img.shields.io/badge/license-GPL%20v3-blue.svg) ![Python Version](https://img.shields.io/badge/python-3.x-yellow.svg)

## Overview
The Python Network Scanner is a utility designed to scan local networks and identify connected devices. It categorizes devices into known and unknown based on a predefined list. This tool leverages third-party libraries for device detection and presents the results in a structured format.

### Notable Features
- Identifies known and unknown devices on the network.
- Utilizes external libraries for enhanced functionality.

## Requirements
- **Python Version**: 3.x
- **Operating System**: Cross-platform (Linux, macOS, Windows)

## Dependencies
### Standard Library
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

For an editable installation, you can run:

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
None specified

## Examples
1. **Basic Usage**: To scan the network and display the results, run:
   ```bash
   python Network_Scanner.py
   ```

2. **Using Docker**: (Note: No Dockerfile is provided, but if it were, the command would look like this)
   ```bash
   docker build -t network-scanner .
   docker run network-scanner
   ```

## Input/Output
| Input                | Output                         |
|----------------------|--------------------------------|
| Network configuration| List of known and unknown devices |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: The scanner does not detect any devices.
  - **Solution**: Ensure that you are connected to the correct network and that the necessary permissions are granted.
  
- **Issue**: Errors related to missing dependencies.
  - **Solution**: Verify that all dependencies are installed as per the `requirements.txt` file.

## Contributing
Coming soon.

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://www.gnu.org/licenses/) for more details.
```
