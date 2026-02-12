```markdown
# FMI Tool
A Python utility for interacting with FMI data.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
The FMI Tool is designed to facilitate the retrieval and processing of data from the Finnish Meteorological Institute (FMI). It leverages third-party libraries such as `requests` and `bs4` for web scraping and data handling. Notable features include:

- Simple command-line interface for executing scripts.
- Integration with external APIs for data retrieval.

## Requirements
- **Python version**: 3.6 or higher
- **Operating System**: Cross-platform

## Dependencies
### Standard Library Modules
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
To install the required dependencies, you can use the provided `requirements.txt` file:

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
| Name                | Default | Description                  |
|---------------------|---------|------------------------------|
| FMI_COORDINATES     | None    | Controls runtime behavior     |
| FMI_PLACE           | None    | Controls runtime behavior     |

## Examples
1. **Basic Execution**:
   ```bash
   python fmi.py
   ```

2. **With Environment Variables**:
   ```bash
   export FMI_COORDINATES="60.1695,24.9354"
   export FMI_PLACE="Helsinki"
   python fmi.py
   ```

## Input/Output
| Input Type | Output Type |
|------------|-------------|
| Coordinates | Weather Data |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Missing dependencies.
  - **Solution**: Ensure all dependencies are installed via `pip install -r ..\requirements.txt`.
  
- **Issue**: Environment variables not set.
  - **Solution**: Set the required environment variables before running the script.

## Contributing
Coming soon.

## License
Coming soon.
```
