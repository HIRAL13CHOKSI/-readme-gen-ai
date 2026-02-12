# Currency Converter

This Python utility allows you to convert currency amounts between different currencies using historical or the latest exchange rates. It can be run directly from the command line with arguments or interactively if arguments are omitted.

## Overview

The script fetches real-time or historical currency exchange rates from `api.ratesapi.io` to perform conversions. You can specify the amount, the base currency, the target currency, and optionally a date for which to retrieve the exchange rates.

## Features

*   **Currency Conversion**: Converts a specified amount from one currency to another.
*   **Flexible Rate Dates**: Supports fetching rates for a specific date (`YYYY-MM-DD`) or the most recent rates (`latest`).
*   **Interactive Mode**: Prompts the user for missing arguments if the script is run without full command-line parameters.
*   **Customizable Output**: Provides an option to output only the converted numerical value, useful for scripting.
*   **Input Validation**: Validates currency codes (must be 3 alphabetic characters) and date formats.

## Installation

This is a single-file Python script.

1.  **Save the script**:
    Save the provided source code into a file named `currency_converter.py`.

2.  **Install dependencies**:
    This script requires the `requests` library to fetch data from the API. Install it using pip:
    ```bash
    pip install requests
    ```

## Usage

Run the script from your terminal using Python. If any required arguments (`amount`, `base`, `target`) are not provided on the command line, the script will enter an interactive "wizard" mode, prompting you for the necessary information.

```bash
python currency_converter.py [OPTIONS]
```

**Arguments:**

*   `-a AMOUNT` (`--amount AMOUNT`): The numerical amount you wish to convert.
*   `-b BASE` (`--base BASE`): The 3-letter currency code of the currency you are converting *from* (e.g., `USD`, `EUR`, `GBP`).
*   `-t TARGET` (`--target TARGET`): The 3-letter currency code of the currency you are converting *to* (e.g., `JPY`, `AUD`, `CAD`).
*   `-d DATE` (`--date DATE`): The specific date for which to retrieve conversion rates, in `YYYY-MM-DD` format, or the string `"latest"` for the most current rates (default: `latest`).
*   `-s`, `--simple-output`: If this flag is present, only the raw converted amount will be printed to standard output. Otherwise, a formatted string is displayed.

## Examples

**1. Basic Conversion (Latest Rates)**
Convert 100 US Dollars to Euros using the most recent exchange rates.

```bash
python currency_converter.py -a 100 -b USD -t EUR
# Example output:
# 100 USD = 92.50 EUR  (date: latest)
```

**2. Conversion on a Specific Date**
Find out what 75 British Pounds were worth in Japanese Yen on January 15, 2023.

```bash
python currency_converter.py -a 75 -b GBP -t JPY -d 2023-01-15
# Example output:
# 75 GBP = 11723.45 JPY  (date: 2023-01-15)
```

**3. Simple Output for Scripting**
Get just the numeric value when converting 200 Canadian Dollars to Australian Dollars.

```bash
python currency_converter.py -a 200 -b CAD -t AUD -s
# Example output:
# 220.78
```

**4. Using Interactive Mode**
If you run the script without any arguments, it will guide you through the input process:

```bash
python currency_converter.py
# [*] Enter amount you want to convert > 50
# [*] Enter base currency code you are converting from > EUR
# [*] Enter target currency code you are converting to > USD
# [*] Enter date from which you want conversion rates, in format yyyy-mm-dd or string "latest" > 2024-03-01
# 50 EUR = 54.32 USD  (date: 2024-03-01)
```

## Limitations or Notes

*   **API Source**: This script relies on `api.ratesapi.io` for all currency exchange rates. Its availability, accuracy, and rate limits are dependent on this third-party service.
*   **Currency Codes**: All currency codes must be 3 uppercase alphabetic characters (e.g., `USD`, `EUR`, `JPY`).
*   **Date Format**: Dates must adhere to the `YYYY-MM-DD` format. The special string `"latest"` can be used for the most recent available rates.
*   **Precision**: Converted amounts are rounded to two decimal places by default.
*   **No API Key**: The `ratesapi.io` API currently does not require an API key for the basic services utilized by this script.
