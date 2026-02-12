This README provides an overview and instructions for the `Network_Scanner.py` utility.

---

# Network_Scanner.py

## Overview

`Network_Scanner.py` is a Python utility designed to scan your local network, discover active devices, and identify them by IP and MAC address. It categorizes discovered devices into "Known" or "Unknown" based on a configurable `data/devices.json` file. The results are displayed in clear tabular format in the console and logged to a daily file for historical tracking.

## Features

*   **Network Discovery:** Scans the local network to find active hosts.
*   **MAC Address Resolution:** Retrieves MAC addresses for discovered devices.
*   **Device Categorization:** Differentiates between "Known" and "Unknown" devices using a configurable `data/devices.json` file.
*   **Configurable Device Information:** "Known" devices can be assigned custom names, types, owners, locations, and "allowed" statuses.
*   **Tabular Output:** Presents scan results for both known and unknown devices in easy-to-read tables.
*   **Daily Logging:** Automatically creates or appends to a log file (`data/<current_date>.log`) with details of all scanned devices.
*   **Automatic Data Directory Creation:** Creates the `data` directory if it doesn't exist.

## Installation

This script requires Python 3.x.

1.  **Download the script:**
    Ensure `Network_Scanner.py` is in your desired directory. This script also relies on two other local modules: `device.py` and `network.py`. Make sure these files are present in the same directory as `Network_Scanner.py`.

2.  **Install dependencies:**
    The script uses external libraries that need to be installed.
    ```bash
    pip install getmac prettytable
    ```

## Usage

1.  **Prepare `data/devices.json` (Optional but recommended):**
    Create a directory named `data` in the same location as `Network_Scanner.py`. Inside this `data` directory, you can create a `devices.json` file. This JSON file defines devices that the scanner should recognize as "known" based on their MAC addresses.

    If `data/devices.json` is not found or is empty, the script will still run, but all devices will initially be categorized as "Unknown". The script will also print an example format for `devices.json` if it's missing or invalid.

    **Example `data/devices.json` format:**
    ```json
    {
        "00:00:00:00:00:00": {
            "type": "Router",
            "owner": "Network Admin",
            "location": "Server Rack",
            "allowed": true
        },
        "AA:BB:CC:DD:EE:FF": {
            "type": "Workstation",
            "owner": "John Doe",
            "location": "Office 1",
            "allowed": true
        }
    }
    ```

2.  **Run the script:**
    Execute the script directly from your terminal:
    ```bash
    python Network_Scanner.py
    ```

## Examples

When executed, the script will perform a network scan and then output two tables to your console: "Known Devices" and "Unknown Devices". It will also indicate the path to the log file containing all discovered devices.

**Example Console Output:**

```
Known Devices
+---------------+---------------+-----------------+-------------+-------------+---------+
|  MAC ADDRESS  |      IP       | NAME IN NETWORK |     NAME    |  LOCATION   | ALLOWED |
+---------------+---------------+-----------------+-------------+-------------+---------+
| 00:00:00:00:00:00 | 192.168.1.1   |     my-router   | My Home Router | Living Room |   True  |
| AA:BB:CC:DD:EE:FF | 192.168.1.105 |   johndoe-pc    |  John Doe PC |    Office   |   True  |
+---------------+---------------+-----------------+-------------+-------------+---------+

Unknown Devices
+---------------+---------------+-----------------+
|  MAC ADDRESS  |      IP       | NAME IN NETWORK |
+---------------+---------------+-----------------+
| 11:22:33:44:55:66 | 192.168.1.200 |    smart-tv     |
| DD:EE:FF:11:22:33 | 192.168.1.12  |    new-device   |
+---------------+---------------+-----------------+

You can find a log file with all devices in "data/2023-10-27.log"
```
*(Note: The date in the log file name will correspond to the current execution date.)*

## Limitations or Notes

*   This script requires the `device.py` and `network.py` files to be present in the same directory as `Network_Scanner.py` for successful execution, as it imports custom classes from them.
*   Network scanning can sometimes be slow, depending on your network size and configuration. The script includes a `KeyboardInterrupt` handler if you wish to stop scanning prematurely.
*   The script's functionality for network discovery and MAC address resolution relies on the underlying `network.py` and `getmac` modules, which may require specific network permissions depending on your operating system and environment.
*   The script does not currently support command-line arguments for configuration (e.g., specifying a different data path or network range). All configuration related to known devices is managed via `data/devices.json`, and network scanning parameters are likely internal to `network.py`.
