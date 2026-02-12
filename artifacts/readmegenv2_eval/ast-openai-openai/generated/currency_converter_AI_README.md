```markdown
# Currency Converter
A simple command-line tool for converting currencies.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
Currency Converter is a command-line application that allows users to convert amounts between different currencies. It leverages the `requests` library to fetch current exchange rates and provides a straightforward interface for users to specify the amount, base currency, target currency, and an optional date for historical rates.

### Notable Features
- Convert currencies using real-time exchange rates.
- Support for specifying a date to retrieve historical rates.
- Simple output option for streamlined results.

## Requirements
- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform

## Dependencies
### Standard Library Modules
- `argparse`
- `datetime`
- `decimal`
- `typing`

### Third-Party Packages
- `requests`

## Installation
To install the required dependencies, you can use the provided `requirements.txt` file:

```bash
pip install -r ../requirements.txt
```

For an editable installation, you can run:

```bash
pip install -e .
```

## Usage
To run the currency converter, use the following command:

```bash
python currency_converter.py -a <value> -b <value> -t <value> -d <value> --simple-output
```

## Flags
| Flag                | Alias | Type | Required | Default | Help                                         |
|---------------------|-------|------|----------|---------|----------------------------------------------|
| `-a`                |       | str  | No       | None    | Amount to convert                           |
| `-b`                |       | str  | No       | None    | Base currency code                          |
| `-t`                |       | str  | No       | None    | Target currency code                        |
| `-d`                |       | str  | No       | None    | Date for historical conversion              |
| `--simple-output`   | `-s`  | bool | No       | None    | If present, only converted amount is returned |

## Environment Variables
| Name | Default | Description                       |
|------|---------|-----------------------------------|
| None | None    | Controls runtime behavior          |

## Examples
1. Basic conversion:
   ```bash
   python currency_converter.py -a 100 -b USD -t EUR
   ```

2. Conversion with historical date:
   ```bash
   python currency_converter.py -a 100 -b USD -t EUR -d 2023-01-01
   ```

## Input/Output
| Input               | Output               |
|---------------------|---------------------|
| Amount, Base, Target, Date | Converted amount |

## Testing
To run the tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Invalid currency code.
  - **Solution**: Ensure that the currency codes are valid and supported.
  
- **Issue**: Network error when fetching rates.
  - **Solution**: Check your internet connection and try again.

## Contributing
Coming soon.

## License
Coming soon.
```
