```markdown
# VPC Subnet Calculator
A tool for calculating subnets within a given VPC CIDR range.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview
The VPC Subnet Calculator is a command-line tool designed to help users calculate subnets based on a specified VPC CIDR range and the number of Availability Zones (AZs) to use. It leverages the `netaddr` library for IP address manipulations and provides a straightforward interface for subnet calculations.

### Notable Features
- Calculate subnets based on CIDR notation.
- Specify the number of Availability Zones for subnet distribution.

## Requirements
- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform

## Dependencies
### Standard Library
- `__future__`
- `argparse`
- `math`

### Third-Party Packages
- `netaddr`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, you can use the provided `requirements.txt` file:

```bash
pip install -r ../requirements.txt
```

For an editable install, you can run:

```bash
pip install -e .
```

## Usage
To run the VPC Subnet Calculator, use the following command:

```bash
python vpc_subnet_calculator.py vpc_cidr_range <value> num_azs <value>
```

## Flags
| Flag          | Alias | Type | Required | Default | Help                     |
|---------------|-------|------|----------|---------|--------------------------|
| vpc_cidr_range|       | str  | No       | None    | eg. 10.0.0.0/16         |
| num_azs      |       | int  | No       | None    | Number of AZs to use    |

## cURL Options Passthrough
None specified.

## Environment Variables
None specified.

## Examples
1. Basic usage to calculate subnets:
   ```bash
   python vpc_subnet_calculator.py vpc_cidr_range 10.0.0.0/16 num_azs 3
   ```

2. Example with different CIDR range:
   ```bash
   python vpc_subnet_calculator.py vpc_cidr_range 192.168.1.0/24 num_azs 2
   ```

## Input/Output
| Input                       | Output                      |
|-----------------------------|-----------------------------|
| VPC CIDR range              | Calculated subnets          |
| Number of Availability Zones | Subnet distribution details  |

## Testing
To run the tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: Invalid CIDR range format.
  - **Solution**: Ensure the CIDR notation is correct (e.g., 10.0.0.0/16).
  
- **Issue**: Incorrect number of AZs specified.
  - **Solution**: Verify that the number of AZs is a positive integer.

## Contributing
Coming soon.

## License
Coming soon.
```
