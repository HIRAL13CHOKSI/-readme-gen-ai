# VPC Subnet Calculator

## Overview
The VPC Subnet Calculator is a Python utility designed to calculate the necessary subnets for an AWS Virtual Private Cloud (VPC) based on a given CIDR range and the number of Availability Zones (AZs) required. This tool helps in efficiently allocating IP address ranges for both private and public subnets.

## Features
- Calculates private and public subnets for an AWS VPC.
- Supports CIDR notation for specifying the VPC range.
- Automatically determines subnet sizes based on the number of AZs.
- Validates subnet sizes to ensure they meet AWS requirements.

## Installation
To use the VPC Subnet Calculator, you need to have Python installed on your machine. Additionally, the `netaddr` library is required. You can install it using pip:

```bash
pip install netaddr
```

## Usage
Run the script from the command line with the following syntax:

```bash
python vpc_subnet_calculator.py <vpc_cidr_range> <num_azs>
```

### Example Command
To calculate subnets for a VPC with a CIDR range of `10.0.0.0/16` and 3 Availability Zones, use the following command:

```bash
python vpc_subnet_calculator.py 10.0.0.0/16 3
```

## Examples
Here are a few example commands and their expected outputs:

1. **Example 1:**
   ```bash
   python vpc_subnet_calculator.py 10.0.0.0/16 2
   ```
   **Output:**
   ```
   10.0.0.0/18
   10.0.64.0/18
   ```

2. **Example 2:**
   ```bash
   python vpc_subnet_calculator.py 192.168.1.0/24 4
   ```
   **Output:**
   ```
   192.168.1.0/26
   192.168.1.64/26
   ```

## Limitations or Notes
- The script currently assumes that all subnets being subtracted are of equal size.
- The maximum subnet size is limited to `/28` and the minimum to `/16` as per AWS VPC requirements.
- Ensure that the `netaddr` library is installed before running the script to avoid import errors.

This README provides a comprehensive guide to using the VPC Subnet Calculator, enabling users to effectively manage their AWS VPC subnetting needs.
