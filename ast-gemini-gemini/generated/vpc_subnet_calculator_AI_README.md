# VPC Subnet Calculator

A utility for efficiently calculating and allocating VPC subnets based on a given CIDR range and number of Availability Zones (AZs).

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/your-package-name.svg)](https://pypi.org/project/your-package-name/)
[![PyPI](https://img.shields.io/pypi/v/your-package-name.svg)](https://pypi.org/project/your-package-name/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/travis/your-repo/your-project/main.svg?branch=main)](https://travis-ci.org/your-repo/your-project)

## Overview

The `vpc_subnet_calculator.py` script provides a command-line interface to help network architects and developers plan their AWS (or similar cloud) VPC subnetting. It takes a parent VPC CIDR range and the desired number of Availability Zones (AZs) as input, then intelligently allocates smaller, non-overlapping subnet CIDR blocks. This tool leverages the `netaddr` library for robust IP address and CIDR block manipulation.

### Notable Features
*   **Intelligent Allocation**: Calculates optimal subnet sizes and ranges.
*   **AZ Distribution**: Supports distributing subnets across a specified number of Availability Zones.
*   **Command-Line Interface**: Easy to use from the terminal.

## Requirements

*   **Python**: Version 3.8+ (recommended)
*   **Operating System**: Platform-agnostic (Linux, macOS, Windows)

## Dependencies

This project relies on the following Python packages:

### Third-party Packages
*   `netaddr`: For robust IP address and CIDR manipulation.
*   `google-generativeai`: (Potentially for AI-driven aspects, if integrated)
*   `groq`: (Potentially for AI-driven aspects, if integrated)
*   `openai`: (Potentially for AI-driven aspects, if integrated)

## Installation

To get started, first clone the repository and then install the required dependencies using the provided `requirements.txt` file:

```bash
# Clone the repository (replace with your actual repository URL)
git clone https://github.com/your-org/your-project.git
cd your-project

# Install dependencies
pip install -r ../requirements.txt
```

## Usage

Run the script from your terminal, providing the VPC CIDR range and the number of Availability Zones:

```bash
python vpc_subnet_calculator.py --vpc_cidr_range <value> --num_azs <value>
```

Replace `<value>` with your desired CIDR block (e.g., `10.0.0.0/16`) and the number of AZs (e.g., `3`).

## Flags

The script accepts the following command-line arguments:

| Flag              | Alias | Type | Required | Default | Help                                |
| :---------------- | :---- | :--- | :------- | :------ | :---------------------------------- |
| `--vpc_cidr_range` |       | `str` | False    |         | eg. 10.0.0.0/16                     |
| `--num_azs`        |       | `int` | False    |         | Number of AZs to use                |

## Environment Variables

None specified.

## Examples

Here are a few common usage examples for the VPC Subnet Calculator:

### Example 1: Calculate subnets for a /16 VPC across 3 AZs

This example demonstrates how to split a large `10.0.0.0/16` VPC CIDR block into smaller subnets suitable for 3 Availability Zones.

```bash
python vpc_subnet_calculator.py --vpc_cidr_range 10.0.0.0/16 --num_azs 3
```

Expected Output (simplified, actual output might vary based on calculation logic):
```
Calculated Subnets:
AZ 1: 10.0.0.0/18
AZ 1: 10.0.64.0/19
...
AZ 2: 10.0.128.0/18
AZ 2: 10.0.192.0/19
...
```

### Example 2: Calculate subnets for a /20 VPC across 2 AZs

This example shows subnetting a smaller `192.168.10.0/20` VPC across just 2 AZs.

```bash
python vpc_subnet_calculator.py --vpc_cidr_range 192.168.10.0/20 --num_azs 2
```

Expected Output (simplified):
```
Calculated Subnets:
AZ 1: 192.168.10.0/21
AZ 1: 192.168.18.0/22
...
AZ 2: 192.168.20.0/21
AZ 2: 192.168.28.0/22
...
```

## Input/Output

| Type   | Description                                           | Format                                    |
| :----- | :---------------------------------------------------- | :---------------------------------------- |
| Input  | VPC CIDR range and number of Availability Zones as CLI arguments. | `--vpc_cidr_range <CIDR>`, `--num_azs <int>` |
| Output | A list of calculated subnet CIDR blocks, typically grouped by AZ. | Text output to console                  |

## Testing

This project includes tests to ensure the correctness of subnet calculations. You can run them using `pytest`:

```bash
# Ensure pytest is installed
pip install pytest

# Run the tests
pytest
```

## Troubleshooting

*   **`netaddr` import error**: If you encounter an `ModuleNotFoundError: No module named 'netaddr'`, ensure you have installed all dependencies: `pip install -r ../requirements.txt`.
*   **Invalid CIDR format**: If the script returns an error about an invalid CIDR, double-check that your `--vpc_cidr_range` input (e.g., `10.0.0.0/16`) is correctly formatted and a valid IP range with a subnet mask.
*   **Unexpected subnet sizes**: The calculation logic aims to maximize subnet utilization. If the resulting subnet sizes aren't what you expected, consider the number of AZs requested; this directly influences how the parent CIDR is divided.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

Coming soon.
