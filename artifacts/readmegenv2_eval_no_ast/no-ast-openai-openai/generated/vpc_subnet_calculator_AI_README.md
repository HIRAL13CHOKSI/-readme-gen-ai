# VPC Subnet Calculator

## Overview
The VPC Subnet Calculator is a Python utility designed to calculate the necessary subnets for an AWS Virtual Private Cloud (VPC) based on a given CIDR range and the number of Availability Zones (AZs) specified. This tool helps in efficiently managing IP address allocation within a VPC.

## Features
- Calculates private and public subnets for an AWS VPC.
- Supports CIDR notation for specifying the VPC range.
- Automatically adjusts subnet sizes based on the number of AZs.
- Validates subnet sizes to ensure they meet AWS requirements.

## Installation
To use the VPC Subnet Calculator, ensure you have Python installed on your system. You will also need to install the `netaddr` library, which can be done using pip:

```bash
pip install netaddr
```

## Usage
Run the script from the command line with the following syntax:

```bash
python vpc_subnet_calculator.py <vpc_cidr_range> <num_azs>
```

### Example Commands
1. To calculate subnets for a VPC with a CIDR range of `10.0.0.0/16` and 3 Availability Zones:
   ```bash
   python vpc_subnet_calculator.py 10.0.0.0/16 3
   ```

2. For a VPC with a CIDR range of `192.168.0.0/20` and 2 Availability Zones:
   ```bash
   python vpc_subnet_calculator.py 192.168.0.0/20 2
   ```

## Examples
Given the command:
```bash
python vpc_subnet_calculator.py 10.0.0.0/16 3
```
The output might look like:
```
10.0.0.0/18
10.0.64.0/18
10.0.128.0/18
10.0.192.0/18
```
This output represents the calculated private and public subnets based on the provided CIDR range and number of AZs.

## Limitations or Notes
- Ensure that the `netaddr` library is installed to avoid import errors.
- The script currently assumes that all subnets being subtracted are of equal size.
- The maximum subnet size is limited to `/28` and the minimum to `/16` as per AWS VPC requirements.
- The script does not handle cases where the provided CIDR range cannot accommodate the requested number of subnets.
