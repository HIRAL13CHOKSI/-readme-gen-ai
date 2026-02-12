```markdown
# Network Scanner

A Python script to scan and identify devices on a network.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
![Placeholder Badge](https://img.shields.io/badge/status-alpha-red)

## Overview

The Network Scanner script identifies devices on a network and categorizes them as either known (MAC address in `data/device.json`) or unknown. It leverages the `device`, `getmac`, `network`, and `prettytable` libraries to gather device information and present it in a user-friendly format.

Notable features:

-   Identifies devices connected to the network.
-   Categorizes devices as "known" or "unknown" based on a predefined list.

## Requirements

-   Python 3.7+
-   Any modern operating system.

## Dependencies

### Standard Library

-   `datetime`
-   `json`
-   `os`
-   `sys`

### Third-Party Packages

-   `device`
-   `getmac`
-   `google-generativeai`
-   `groq`
-   `network`
-   `openai`
-   `prettytable`

## Installation

To install the Network Scanner and its dependencies, follow these steps:

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Install the required packages using `pip`:

    ```bash
    pip install -r ../requirements.txt
    ```

    Alternatively, install in editable mode:

    ```bash
    pip install -e .
    ```

## Usage

To run the Network Scanner, execute the following command:

```bash
python Network_Scanner.py
```

## Flags

None

## Examples

1.  Run the network scanner to identify devices on the network:

    ```bash
    python Network_Scanner.py
    ```

## Input/Output

| Input         | Output                               |
| ------------- | ------------------------------------ |
| Network data  | List of known and unknown devices. |

## Testing

The project includes tests. To run them, use `pytest`:

```bash
pytest
```

## Troubleshooting

1.  **Permission errors:** Ensure you have the necessary permissions to run network scanning tools. You may need to run the script with elevated privileges (e.g., using `sudo` on Linux).
2.  **Missing dependencies:** If you encounter errors related to missing modules, double-check that you have installed all the required dependencies using `pip install -r ../requirements.txt`.

## Contributing

Coming soon

## License

Coming soon
```
