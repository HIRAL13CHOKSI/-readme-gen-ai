# Network Scanner

## Overview
The Network Scanner is a Python utility designed to scan a local network for connected devices. It identifies both known and unknown devices based on a predefined JSON file containing device information. The results are displayed in a formatted table and logged for future reference.

## Features
- Scans the local network for devices.
- Differentiates between known and unknown devices.
- Displays device information in a readable table format.
- Logs the scan results to a file for record-keeping.
- Supports customization through a JSON configuration file.

## Installation
To use the Network Scanner, you need to have Python installed on your machine. Additionally, you will need to install the required dependencies. You can do this using pip:

```bash
pip install getmac prettytable
```

## Usage
To run the Network Scanner, execute the script from the command line. Ensure that you have a valid `devices.json` file in the `data` directory, or create one as specified below.

```bash
python Network_Scanner.py
```

### Example Command
```bash
python Network_Scanner.py
```

## Examples
### Creating the `devices.json` File
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

### Output
Upon running the script, you will see output similar to the following:

```
Known Devices
+---------------------+-------------+---------------------+------------------+----------+---------+
|     MAC ADDRESS     |     IP      |    NAME IN NETWORK  |       NAME       | LOCATION | ALLOWED |
+---------------------+-------------+---------------------+------------------+----------+---------+
| 00:00:00:00:00:00   | 192.168.1.2 | Device Name         | John Appleseed   |          |   True  |
+---------------------+-------------+---------------------+------------------+----------+---------+

Unknown Devices
+---------------------+-------------+---------------------+
|     MAC ADDRESS     |     IP      |    NAME IN NETWORK  |
+---------------------+-------------+---------------------+
| 00:00:00:00:00:01   | 192.168.1.3 | Unknown Device       |
+---------------------+-------------+---------------------+
```

A log file will also be created in the `data` directory with the date as its filename, containing the details of the scanned devices.

## Limitations or Notes
- Ensure that the `data/devices.json` file exists and is correctly formatted before running the script. If the file is missing or incorrectly formatted, the script will prompt you with instructions on how to create it.
- The script requires network access and may take some time to complete depending on the network size.
- The script may need to be run with administrative privileges depending on your operating system and network configuration.
- If you encounter a `ModuleNotFoundError`, ensure that the required packages (`getmac` and `prettytable`) are installed.
