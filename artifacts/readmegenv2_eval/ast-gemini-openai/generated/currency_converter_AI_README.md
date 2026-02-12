# Currency Converter

A simple command-line tool to convert currencies using historical exchange rates.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen)](https://img.shields.io/badge/tests-passing-brightgreen)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

This Python script, `currency_converter.py`, allows you to convert an amount from one currency to another for a specific date. It fetches historical exchange rates and performs the conversion, offering a simple output option for streamlined results.

Notable features:

- Converts currencies using historical data.
- Provides simple output for scripts and command-line usage.
- Uses an interactive wizard when arguments are missing.

## Requirements

- Python 3.7+
- Tested on Linux, macOS, and Windows

## Dependencies

### Python Standard Library

- `argparse`
- `datetime`
- `decimal`
- `typing`

### Third-Party Packages

- `requests`
- `google-generativeai`
- `groq`
- `openai`

## Installation

Install the necessary dependencies using pip:

```bash
pip install -r ../requirements.txt
```

For an editable install:

```bash
pip install -e .
```

## Usage

```
python currency_converter.py -a <value> -b <value> -t <value> -d <value> --simple-output
```

## Flags

| Flag            | Alias | Type   | Required | Default | Help                                  |
|-----------------|-------|--------|----------|---------|---------------------------------------|
| `-a`            | `-a`  | `str`  | No       | `None`  |                                       |
| `-b`            | `-b`  | `str`  | No       | `None`  |                                       |
| `-t`            | `-t`  | `str`  | No       | `None`  |                                       |
| `-d`            | `-d`  | `str`  | No       | `None`  |                                       |
| `--simple-output` | `-s`  | `bool` | No       |         | If present, only converted amount is returned |

## Examples

1.  Convert 100 EUR to USD on 2023-01-01 and display the full output:

    ```bash
    python currency_converter.py -a 100 -b EUR -t USD -d 2023-01-01
    ```

2.  Convert 50 GBP to JPY on 2023-06-15 and display only the converted amount:

    ```bash
    python currency_converter.py -a 50 -b GBP -t JPY -d 2023-06-15 --simple-output
    ```

## Input/Output

| Input         | Description                      |
|---------------|----------------------------------|
| Amount        | The amount to convert.           |
| Base Currency | The currency to convert from.    |
| Target Currency | The currency to convert to.      |
| Date          | The date for the exchange rate. |

| Output        | Description                                        |
|---------------|----------------------------------------------------|
| Converted Amount | The amount converted to the target currency.     |
| Full Output     | Includes the converted amount, exchange rate, and other details. |

## Testing

This project includes tests. It is recommended to use `pytest` to run them:

```bash
pytest
```

## Troubleshooting

1.  **Incorrect conversion:** Ensure the base and target currency codes are valid and the date is in the correct format (YYYY-MM-DD).
2.  **Connection errors:** Verify your internet connection, as the script fetches exchange rates from an online API.

## Contributing

Coming soon.

## License

Coming soon.
