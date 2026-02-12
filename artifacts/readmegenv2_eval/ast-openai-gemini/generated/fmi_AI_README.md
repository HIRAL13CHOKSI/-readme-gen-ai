```markdown
# FMI Tool
A Python utility for interacting with FMI data.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
The FMI Tool is designed to facilitate interactions with FMI (Finnish Meteorological Institute) data. It leverages several third-party libraries to enhance its functionality, including `requests` for HTTP requests and `bs4` for HTML parsing. Notable features include:

- Data retrieval from FMI services.
- Integration with external APIs for enhanced data processing.

## Requirements
- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies
### Standard Library
- `os`
- `warnings`

### Third-Party Packages
- `bs4`
- `observation`
- `requests`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, use the following command:

```bash
pip install -r ..\requirements.txt
```

For an editable install, run:

```bash
pip install -e .
```

## Usage
To run the FMI Tool, execute the following command:

```bash
python fmi.py
```

## Flags
None

## Environment Variables
| Name               | Default | Description                       |
|--------------------|---------|-----------------------------------|
| FMI_COORDINATES    | None    | Controls runtime behavior         |
| FMI_PLACE          | None    | Controls runtime behavior         |

## Examples
1. Basic execution:
   ```bash
   python fmi.py
   ```

2. If you need to set environment variables before running:
   ```bash
   export FMI_COORDINATES='your_coordinates'
   export FMI_PLACE='your_place'
   python fmi.py
   ```

## Input/Output
| Input                | Output               |
|----------------------|----------------------|
| FMI coordinates      | FMI data response    |
| FMI place            | FMI data response    |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Environment variables not set correctly.
  - **Solution**: Ensure that `FMI_COORDINATES` and `FMI_PLACE` are defined in your environment.

- **Issue**: Missing dependencies.
  - **Solution**: Run `pip install -r ..\requirements.txt` to install all required packages.

## Contributing
Coming soon.

## License
Coming soon.
```
