# Network Scanner

A robust Python tool for scanning networks and classifying devices.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

## Overview

Network Scanner is a Python-based utility designed to probe your network and identify connected devices. It features the unique ability to classify devices as "known" or "unknown" by comparing discovered MAC addresses against a predefined list (e.g., in `data/device.json`). This allows for quick identification of new or unauthorized devices on your network.

**Key Features:**

*   **Device Discovery**: Scans the local network to identify active hosts.
*   **Device Classification**: Distinguishes between known and unknown devices based on a configurable list.
*   **Structured Output**: Presents scanning results in an easy-to-read format.

## Requirements

This tool requires Python 3.x to run. It has been developed and tested on common operating systems like Linux, macOS, and Windows.

## Dependencies

This project relies on a few standard Python libraries and several third-party packages.

### Standard Library Modules

*   `datetime`
*   `json`
*   `os`
*   `sys`

### Third-Party Packages

*   `device`
*   `getmac`
*   `google-generativeai`
*   `groq`
*   `network`
*   `openai`
*   `prettytable`

## Installation

To install Network Scanner, it's recommended to use a virtual environment.

1.  **Clone the repository (or download the script):**
    ```bash
    git clone https://github.com/your-repo/network-scanner.git # Replace with actual repo URL if available
    cd network-scanner
    ```

2.  **Install dependencies using the `requirements.txt` file:**
    Assuming `requirements.txt` is in the parent directory of `Network_Scanner.py`:
    ```bash
    pip install -r ../requirements.txt
    ```

3.  **For development or advanced usage, you can also install in editable mode:**
    ```bash
    pip install -e .
    ```

## Usage

Simply run the script from your terminal. Ensure your Python environment has all required dependencies installed.

```bash
python Network_Scanner.py
```

## Flags

None. This script does not currently support command-line flags.

## Environment Variables

None specified.

## Examples

The primary use case for `Network_Scanner.py` is to perform a network scan and identify known versus unknown devices.

1.  **Basic Network Scan:**
    Execute the script to perform a scan of your local network. The output will typically display a list of discovered devices, categorized by their MAC address against a predefined list.
    ```bash
    python Network_Scanner.py
    ```
    *Expected Output (Illustrative):*
    ```
    +-------------------+-------------------+-------------------+
    | IP Address        | MAC Address       | Status            |
    +-------------------+-------------------+-------------------+
    | 192.168.1.1       | XX:XX:XX:XX:XX:X1 | Known (Router)    |
    | 192.168.1.100     | YY:YY:YY:YY:YY:Y2 | Known (My Laptop) |
    | 192.168.1.105     | ZZ:ZZ:ZZ:ZZ:ZZ:Z3 | Unknown           |
    +-------------------+-------------------+-------------------+
    ```

2.  **Identifying Unknown Devices:**
    The core functionality revolves around the `create_device_list` function, which segregates devices into 'known' and 'unknown' categories. Running the script will automatically leverage this feature, highlighting any new or unexpected devices detected on your network.
    ```bash
    python Network_Scanner.py
    ```
    Review the output table to quickly spot any devices labeled "Unknown," which might warrant further investigation.

## Input/Output

| Type   | Description                                                                                                                                                                                                                                                                      |
| :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input**  | **Network Traffic**: Scans local network segments for active hosts. <br> **`data/device.json`**: (Inferred) A JSON file containing a list of MAC addresses of known devices for classification. |
| **Output** | **Console Output**: A tabular display (via `prettytable`) listing discovered devices, their IP and MAC addresses, and their classification (Known/Unknown).                                                                                                                   |

## Testing

The project includes a test suite to ensure functionality and reliability. It is recommended to run these tests after any modifications.

```bash
pytest
```

## Troubleshooting

1.  **Dependencies Not Found Error**:
    If you encounter `ModuleNotFoundError` or similar issues, ensure all required third-party packages are installed.
    *   **Solution**: Run `pip install -r ../requirements.txt` to install all dependencies.

2.  **No Devices Found / Incomplete Scan**:
    If the scanner returns no devices or misses some, it could be due to network permissions or firewall settings.
    *   **Solution**: Ensure your system's firewall is not blocking outgoing scan packets or incoming responses. Running the script with elevated privileges (e.g., `sudo python Network_Scanner.py` on Linux) might be necessary for certain network operations, but exercise caution.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the GNU General Public License v3.0 or any later version. See the [GNU website](https://www.gnu.org/licenses/) for more details.
