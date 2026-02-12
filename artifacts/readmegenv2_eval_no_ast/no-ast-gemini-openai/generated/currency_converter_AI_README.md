```markdown
# Currency Converter

## Overview

This Python script is a command-line tool for converting currencies using real-time exchange rates from an online API. It allows you to specify the amount, base currency, target currency, and optionally a specific date for the conversion.

## Features

*   **Currency Conversion:** Converts an amount from one currency to another.
*   **Date Specification:** Uses the latest exchange rates or rates from a specified date.
*   **Command-Line Interface:**  Provides a user-friendly command-line interface for easy use.
*   **Interactive Input:** Prompts for missing arguments if not provided via command line.
*   **Simple Output:**  Option to display only the converted amount.

## Installation

1.  Save the script to a file, for example, `currency_converter.py`.
2.  Ensure you have Python 3 installed.
3.  No external libraries need to be installed using pip, as the script uses the `requests` module which is usually bundled in standard python library installation.

## Usage

Run the script from the command line:

```bash
python currency_converter.py [options]
```

### Options

*   `-a AMOUNT`: Amount you want to convert.
*   `-b BASE`: Base currency code (e.g., USD).
*   `-t TARGET`: Target currency code (e.g., EUR).
*   `-d DATE`: Date for conversion rates in YYYY-MM-DD format, or `latest` for the most recent rates. Defaults to `latest`.
*   `-s`, `--simple-output`: If present, only the converted amount is printed.

If any of the arguments are missing, the script will prompt you to enter them interactively.

## Examples

1.  **Convert 100 USD to EUR using the latest exchange rates:**

    ```bash
    python currency_converter.py -a 100 -b USD -t EUR
    ```

    Output:

    ```
    100 USD = 92.34 EUR  (date: latest)
    ```

2.  **Convert 50 EUR to GBP using exchange rates from 2023-10-27 with simple output:**

    ```bash
    python currency_converter.py -a 50 -b EUR -t GBP -d 2023-10-27 -s
    ```

    Output:

    ```
    43.40
    ```

3.  **Run the script without arguments to use interactive mode:**

    ```bash
    python currency_converter.py
    ```

    The script will then prompt you to enter the amount, base currency, target currency, and date.

## Limitations or Notes

*   The script relies on the `api.ratesapi.io` API for exchange rates. Ensure you have network connectivity.
*   The API may have usage limits or be subject to changes, which could affect the script's functionality.
*   Currency codes must be three letters long.
*   Date must be in "YYYY-MM-DD" format or the string "latest".
```
