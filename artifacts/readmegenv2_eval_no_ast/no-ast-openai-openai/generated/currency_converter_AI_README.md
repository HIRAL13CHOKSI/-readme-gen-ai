# Currency Converter Tool

## Overview
The Currency Converter Tool is a command-line utility that allows users to convert amounts between different currencies using real-time exchange rates. Users can specify the base currency, target currency, and an optional date for historical rates.

## Features
- Convert amounts between any two currencies.
- Retrieve exchange rates for a specified date or the latest rates.
- Simple output option for streamlined results.
- Input validation for currency codes and dates.

## Installation
This script requires Python 3 and the `requests` library. You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage
To use the Currency Converter Tool, run the script from the command line with the required parameters. The basic syntax is:

```bash
python currency_converter.py -a AMOUNT -b BASE -t TARGET [-d DATE] [-s]
```

### Parameters:
- `-a AMOUNT`: The amount you want to convert (required).
- `-b BASE`: The base currency code you are converting from (required).
- `-t TARGET`: The target currency code you are converting to (required).
- `-d DATE`: The date for which you want the conversion rates (optional, default is "latest").
- `-s`, `--simple-output`: If present, only the converted amount is returned.

### Example Commands
1. Convert 100 USD to EUR using the latest rates:
   ```bash
   python currency_converter.py -a 100 -b USD -t EUR
   ```

2. Convert 50 GBP to JPY for a specific date (2023-01-01):
   ```bash
   python currency_converter.py -a 50 -b GBP -t JPY -d 2023-01-01
   ```

3. Get a simple output of the conversion:
   ```bash
   python currency_converter.py -a 200 -b AUD -t CAD -s
   ```

## Examples
- **Input**: `python currency_converter.py -a 100 -b USD -t EUR`
  - **Output**: `100 USD = 85.50 EUR  (date: latest)`

- **Input**: `python currency_converter.py -a 150 -b EUR -t GBP -d 2022-12-31`
  - **Output**: `150 EUR = 127.30 GBP  (date: 2022-12-31)`

## Limitations or Notes
- Ensure that the currency codes are valid and exactly three letters long.
- The date must be in the format YYYY-MM-DD or "latest".
- The script relies on an external API for exchange rates; ensure you have internet access when running the tool.
- If the specified currency or date does not yield results, an error message will be displayed.
