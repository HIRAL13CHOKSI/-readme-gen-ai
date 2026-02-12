```markdown
# Network Scanner

## Overview

This Python script scans your local network to identify connected devices. It attempts to retrieve the MAC address, IP address, and hostname for each device. The script categorizes devices as either "known" (based on MAC addresses found in a `devices.json` file) or "unknown."  The scan results are displayed in a table format in the console and saved to a daily log file in the `data/` directory.

## Features

*   **Network Scanning:** Discovers devices connected to the local network.
*   **MAC Address Retrieval:** Attempts to retrieve the MAC address for each discovered device.
*   **Device Categorization:** Classifies devices as "known" or "unknown" based on a user-provided `devices.json` file.
*   **Data Display:** Presents scan results in a user-friendly table format using the `PrettyTable` library.
*   **Logging:** Saves detailed scan results to a daily log file within the `data/` directory.

## Installation

1.  **Install Python:** Ensure you have Python 3 installed on your system.

2.  **Install Dependencies:** Install the required Python packages using pip:

    ```bash
    pip install getmac prettytable
    ```

## Usage

1.  **Prepare `devices.json` (Optional):** Create a `data` directory (if it doesn't exist) and place a `devices.json` file inside it. This file allows the script to identify known devices. The `devices.json` file should have the following structure:

    ```json
    {
        "00:00:00:00:00:00": {
            "type": "Device",
            "owner": "John Appleseed",
            "location": null,
            "allowed": true
        },
        "AA:BB:CC:DD:EE:FF": {
            "type": "Router",
            "owner": "Jane Doe",
            "location": "Living Room",
            "allowed": true
        }
    }
    ```

    If you do not create a `devices.json` file, all devices will be reported as 'unknown'.
2.  **Run the Script:** Execute the script from the command line:

    ```bash
    python Network_Scanner.py
    ```

## Examples

*   **Basic Scan:** Running the script without a `devices.json` file will scan the network and list all discovered devices as "unknown."

    ```bash
    python Network_Scanner.py
    ```

*   **Scan with Device Identification:** Create a `devices.json` file with MAC addresses of known devices. When you run the script, these devices will be identified with their associated information (owner, location, etc.).

    ```bash
    python Network_Scanner.py
    ```

## Output

The script will output two tables to the console: "Known Devices" and "Unknown Devices".  A log file containing the detailed scan results will be created in the `data/` directory, named according to the current date (e.g., `data/2023-10-27.log`).  The script prints the log file location to the console.

## Limitations or Notes

*   **Root Privileges:**  The script may require root/administrator privileges to perform network scanning operations effectively on some systems.
*   **Error Handling:**  The script includes basic error handling for keyboard interrupts and missing `devices.json` files, but may not cover all possible network errors.
*   **Network Connectivity:**  Ensure you are connected to the network you intend to scan.
*   **Scanning Time:** Network scanning can take a while, especially on larger networks. A message will be printed if the script is stopped prematurely. Connection problems can also increase scan time.
