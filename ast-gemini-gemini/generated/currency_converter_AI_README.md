# Currency Converter
A command-line tool for currency conversion with historical rate lookups.

---

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/your-package-name.svg)](https://pypi.org/project/your-package-name/)
[![PyPI](https://img.shields.io/pypi/v/your-package-name.svg)](https://pypi.org/project/your-package-name/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Tests](https://github.com/your-org/your-repo/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/your-repo/actions/workflows/ci.yml)

## Overview

`currency_converter.py` is a versatile command-line utility for converting currencies. It allows users to specify an amount, base currency, target currency, and even a historical date for conversion. The tool leverages an external API (via the `requests` library) to fetch real-time and historical exchange rates. A notable feature is the `--simple-output` flag, which provides a concise, plain numerical result suitable for scripting.

## Requirements

*   **Python**: Python 3.8+
*   **Operating System**: OS Independent (Linux, macOS, Windows)

## Dependencies

### Python Packages

This project relies on the following Python packages:

*   `requests`: For making HTTP requests to fetch currency exchange rates.
*   `google-generativeai`: A dependency from the project context.
*   `groq`: A dependency from the project context.
*   `openai`: A dependency from the project context.

### External Tools

None specified.

## Installation

To get started with `currency_converter.py`, clone this repository and install the required dependencies using pip:

1.  Clone the repository (if not already done):
    ```bash
    git clone https://github.com/your-org/your-repo.git
    cd your-repo
    ```
2.  Install dependencies from the `requirements.txt` file:
    ```bash
    pip install -r ../requirements.txt
    ```

## Usage

Run the script from your terminal, providing the necessary arguments.

```bash
python currency_converter.py -a <value> -b <value> -t <value> -d <value> --simple-output
```

## Flags

The `currency_converter.py` script accepts the following command-line arguments:

| Flag            | Alias | Type | Required | Default | Help                                        |
| :-------------- | :---- | :--- | :------- | :------ | :------------------------------------------ |
| `-a`            | `-a`  | str  | False    |         |                                             |
| `-b`            | `-b`  | str  | False    |         |                                             |
| `-t`            | `-t`  | str  | False    |         |                                             |
| `-d`            | `-d`  | str  | False    |         |                                             |
| `--simple-output` | `-s`  | bool | False    |         | If present, only converted amount is returned |

## Environment Variables

None specified.

## Examples

### 1. Convert 100 EUR to USD for today

This example converts 100 Euros to US Dollars using current exchange rates, displaying the full output.

```bash
python currency_converter.py -a 100 -b EUR -t USD
```

### 2. Convert 500 GBP to JPY for a specific historical date with simple output

This example converts 500 British Pounds to Japanese Yen for January 1, 2023, and returns only the numerical conversion value.

```bash
python currency_converter.py -a 500 -b GBP -t JPY -d 2023-01-01 --simple-output
```

## Input/Output

| Type   | Description                                                                                             |
| :----- | :------------------------------------------------------------------------------------------------------ |
| Input  | Command-line flags for amount, base currency, target currency, and an optional date.                      |
| Output | By default, detailed conversion information. With `--simple-output`, only the converted numerical value. |

## Testing

This project includes tests to ensure reliability and correctness. To run the tests, navigate to the project root and use `pytest`:

```bash
pytest
```

## Troubleshooting

*   **API Rate Limit/Connection Errors**: If you encounter errors related to API calls, ensure your internet connection is stable. The underlying API might have rate limits; wait a few moments and try again.
*   **Invalid Currency Codes**: Ensure you are using valid ISO 4217 currency codes (e.g., `USD`, `EUR`, `JPY`). Incorrect codes will result in conversion failures.
*   **Invalid Date Format**: Dates should be provided in a standard format like `YYYY-MM-DD`. Using an incorrect format will lead to parsing errors.

## Contributing

Coming soon.

## License

Coming soon.
