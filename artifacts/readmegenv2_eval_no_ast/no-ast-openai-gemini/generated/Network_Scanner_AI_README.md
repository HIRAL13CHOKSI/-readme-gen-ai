# Python Network Scanner

## Overview
The Python Network Scanner is a utility designed to scan the local network for devices and categorize them into known and unknown devices based on a predefined JSON file. It provides a clear output of the devices found, including their MAC addresses, IP addresses, and other relevant information.

## Features
- Scans the local network for devices.
- Categorizes devices into known and unknown based on a JSON configuration file.
- Outputs the results in a tabular format for easy reading.
- Logs the scan results to a file for future reference.

## Installation
To use the Python Network Scanner, you need to have Python installed on your system. Additionally, you will need to install the following dependencies:

1. `getmac` - For retrieving MAC addresses.
2. `prettytable` - For displaying results in a table format.

You can install these dependencies using pip:

```bash
pip install getmac prettytable
```

## Usage
To run the network scanner, execute the script from the command line:

```bash
python Network_Scanner.py
```

Make sure to have a `data/devices.json` file in the correct format (see the Examples section for the format).

## Examples
### Sample `devices.json` Format
Create a `devices.json` file in the `data` directory with the following format:

```json
{
    "00:00:00:00:00:00": {
        "type": "Device",
        "owner": "John Appleseed",
        "location": null,
        "allowed": true
    }
}
```

### Running the Scanner
After setting up the `devices.json` file, run the scanner:

```bash
python Network_Scanner.py
```

### Output
The output will display two tables:
- **Known Devices**: Lists devices found that are included in the `devices.json`.
- **Unknown Devices**: Lists devices found that are not included in the `devices.json`.

Additionally, a log file will be created in the `data` directory with the scan results.

## Limitations or Notes
- Ensure that the `data/devices.json` file exists and is correctly formatted before running the script.
- The script may take some time to scan the network, depending on the number of devices and network conditions.
- If the required modules (`getmac`, `prettytable`) are not installed, you will encounter an import error. Make sure to install them as mentioned in the Installation section.
- The script does not handle all possible exceptions and may terminate unexpectedly if there are issues with the network connection.
