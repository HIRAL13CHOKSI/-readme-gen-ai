```markdown
# Currency Converter
A simple command-line tool for converting currency amounts.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
Currency Converter is a command-line tool that allows users to convert amounts between different currencies. It retrieves exchange rates from external sources and supports conversion for specified dates. Notable features include:
- Flexible command-line interface
- Support for simple output mode
- Date-specific conversion

## Requirements
- **Python version**: 3.6 or higher
- **Operating System**: Cross-platform

## Dependencies
### Standard Library
- `argparse`
- `datetime`
- `decimal`
- `typing`

### Third-Party Packages
- `requests`

## Installation
To install the required dependencies, use the provided requirements file:

```bash
pip install -r ../requirements.txt
```

For an editable install, you can run:

```bash
pip install -e .
```

## Usage
To use the Currency Converter, run the following command:

```bash
python currency_converter.py -a <value> -b <value> -t <value> -d <value> --simple-output
```

## Flags
| Flag            | Alias | Type | Required | Default | Help                                           |
|-----------------|-------|------|----------|---------|------------------------------------------------|
| `-a`            |       | str  | No       | None    | Amount to convert                              |
| `-b`            |       | str  | No       | None    | Base currency code                             |
| `-t`            |       | str  | No       | None    | Target currency code                           |
| `-d`            |       | str  | No       | None    | Date for the conversion (optional)            |
| `--simple-output` | `-s` | bool | No       | None    | If present, only converted amount is returned  |

## Environment Variables
| Name | Default | Description                     |
|------|---------|---------------------------------|
| None specified |         | Controls runtime behavior       |

## Examples
1. Basic conversion:
   ```bash
   python currency_converter.py -a 100 -b USD -t EUR -d 2023-01-01
   ```

2. Simple output mode:
   ```bash
   python currency_converter.py -a 100 -b USD -t EUR -d 2023-01-01 --simple-output
   ```

## Input/Output
| Input                     | Output                      |
|---------------------------|-----------------------------|
| Amount, Base Currency, Target Currency, Date | Converted amount or detailed output |

## Testing
To run the tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Invalid currency code.
  - **Solution**: Ensure that the currency codes are valid and supported.
  
- **Issue**: No exchange rate available for the specified date.
  - **Solution**: Check if the date is valid and if exchange rates are available for that date.

## Contributing
Coming soon.

## License
Coming soon.
```
