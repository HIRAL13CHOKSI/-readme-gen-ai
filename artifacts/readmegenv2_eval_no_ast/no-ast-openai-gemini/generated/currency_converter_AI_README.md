# Currency Converter Tool

## Overview
The Currency Converter Tool is a command-line utility that allows users to convert amounts from one currency to another using real-time exchange rates. The tool fetches conversion rates from an external API and supports historical rates based on a specified date.

## Features
- Convert amounts between different currencies.
- Fetch the latest or historical exchange rates.
- Simple output option for quick results.
- User-friendly command-line interface with input validation.

## Installation
To use the Currency Converter Tool, ensure you have Python 3 installed on your system. You can run the script directly without any additional installation steps, as it is a standalone Python script.

## Usage
To use the Currency Converter Tool, run the script from the command line with the required arguments. The basic syntax is:

```bash
python currency_converter.py -a <amount> -b <base_currency> -t <target_currency> [-d <date>] [-s]
```

### Command-Line Options
- `-a AMOUNT`: The amount you want to convert (required).
- `-b BASE`: The base currency code you are converting from (required).
- `-t TARGET`: The target currency code you are converting to (required).
- `-d DATE`: The date for which you want the conversion rates (optional, default is "latest").
- `-s, --simple-output`: If present, only the converted amount is returned.

## Examples
1. **Convert 100 USD to EUR using the latest rates:**
   ```bash
   python currency_converter.py -a 100 -b USD -t EUR
   ```

2. **Convert 50 GBP to JPY on a specific date (2023-01-01):**
   ```bash
   python currency_converter.py -a 50 -b GBP -t JPY -d 2023-01-01
   ```

3. **Get only the converted amount for 200 AUD to CAD:**
   ```bash
   python currency_converter.py -a 200 -b AUD -t CAD -s
   ```

## Limitations or Notes
- Ensure that the currency codes are valid and consist of three alphabetic characters.
- The tool relies on an external API for exchange rates, and any downtime or changes to the API may affect functionality.
- Historical rates are only available for dates supported by the API; invalid dates will result in an error.
- The script handles basic input validation, but users should ensure that the inputs are correct to avoid runtime errors.
