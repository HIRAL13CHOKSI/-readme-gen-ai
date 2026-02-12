```markdown
# VPC Subnet Calculator

A tool to calculate optimal subnet configurations for VPCs.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/your-username/your-repo/actions/workflows/tests.yml/badge.svg)](https://github.com/your-username/your-repo/actions/workflows/tests.yml)
[![Codecov](https://codecov.io/gh/your-username/your-repo/branch/main/graph/badge.svg?token=YOUR_TOKEN)](https://codecov.io/gh/your-username/your-repo)

## Overview

This Python script calculates the optimal subnet configurations for a given VPC CIDR range and number of availability zones (AZs).  It leverages the `netaddr` library to perform network calculations. The script determines the largest possible subnet size that allows for an even distribution of subnets across the specified number of AZs.

## Requirements

*   Python 3.7+
*   Operating System: Platform independent

## Dependencies

### Python Standard Library

*   `__future__`
*   `argparse`
*   `math`

### Third-Party Packages

*   `netaddr`
*   `google-generativeai`
*   `groq`
*   `openai`

## Installation

To install the VPC Subnet Calculator and its dependencies, use `pip`:

```bash
pip install -r ../requirements.txt
```

For an editable install, use:

```bash
pip install -e .
```

## Usage

```
python vpc_subnet_calculator.py vpc_cidr_range <value> num_azs <value>
```

## Flags

| Flag              | Alias | Type   | Required | Default | Help                       |
| ----------------- | ----- | ------ | -------- | ------- | -------------------------- |
| `vpc_cidr_range`  |       | `str`  |          |         | eg. 10.0.0.0/16          |
| `num_azs`         |       | `int`  |          |         | Number of AZs to use       |

## Examples

1.  Calculate subnets for the CIDR range `10.0.0.0/16` across 3 availability zones:

    ```bash
    python vpc_subnet_calculator.py vpc_cidr_range 10.0.0.0/16 num_azs 3
    ```

2.  Calculate subnets for the CIDR range `192.168.0.0/24` across 2 availability zones:

    ```bash
    python vpc_subnet_calculator.py vpc_cidr_range 192.168.0.0/24 num_azs 2
    ```

## Input/Output

| Input             | Output                                             |
| ----------------- | -------------------------------------------------- |
| VPC CIDR Range    | List of calculated subnets for each availability zone |
| Number of AZs     |                                                    |

## Testing

To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting

1.  **Incorrect VPC CIDR Range:** Ensure the provided VPC CIDR range is valid and in the correct format (e.g., `10.0.0.0/16`).
2.  **Invalid Number of AZs:** The number of AZs must be a positive integer.

## Contributing

Coming soon.

## License

Coming soon.
```
