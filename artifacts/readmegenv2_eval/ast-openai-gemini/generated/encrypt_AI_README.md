```markdown
# Encrypt Tool
A simple encryption and decryption utility.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
The Encrypt Tool is a Python script designed for basic encryption and decryption tasks. It utilizes the `Crypto` library for cryptographic functions, enabling secure data handling. Notable features include:

- Simple command-line interface for encryption and decryption.
- Key management through the `getKey` function.

## Requirements
- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies
### Standard Library
- `os`

### Third-Party Packages
- `Crypto`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, use the provided `requirements.txt` file:

```bash
pip install -r ..\requirements.txt
```

For an editable installation, you can also run:

```bash
pip install -e .
```

## Usage
To run the Encrypt Tool, execute the following command:

```bash
python encrypt.py
```

## Flags
None

## cURL Options Passthrough
None

## Environment Variables
None specified

## Examples
### Example 1: Basic Encryption
Run the script to start the encryption process:

```bash
python encrypt.py
```

### Example 2: Docker (Not applicable as no Dockerfile is present)
None specified

## Input/Output
| Input          | Output         |
|----------------|----------------|
| Plain text     | Encrypted text  |
| Encrypted text | Decrypted text  |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Script fails to import `Crypto`.
  - **Solution**: Ensure the `Crypto` library is installed via pip.
  
- **Issue**: Python version is incompatible.
  - **Solution**: Upgrade to Python 3.6 or higher.

## Contributing
Coming soon.

## License
Coming soon.
```
