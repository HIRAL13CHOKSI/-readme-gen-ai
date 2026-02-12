```markdown
# VPC Subnet Calculator

## Overview

This Python script calculates and displays a list of private and public subnets for an Amazon Web Services (AWS) Virtual Private Cloud (VPC), given a VPC CIDR range and the number of Availability Zones (AZs). It attempts to maximize the size of the subnets within the given constraints.

## Features

*   Calculates private and public subnets for a given VPC CIDR range and number of Availability Zones.
*   Automatically determines appropriate subnet sizes, attempting to maximize subnet size.
*   Ensures that the calculated subnet sizes fall within the acceptable range for AWS VPCs (/16 - /28).
*   Splits the VPC CIDR range into private and public subnets.

## Installation

1.  **Install Python:** Ensure you have Python 3 installed on your system.
2.  **Install the `netaddr` package:**
    ```bash
    pip install netaddr
    ```

## Usage

Run the script from the command line, providing the VPC CIDR range and the number of Availability Zones as arguments:

```bash
python vpc_subnet_calculator.py <vpc_cidr_range> <num_azs>
```

*   `<vpc_cidr_range>`: The CIDR range for your VPC (e.g., `10.0.0.0/16`).
*   `<num_azs>`: The number of Availability Zones you want to use.

## Examples

**Example 1: Calculate subnets for a VPC with CIDR range `10.0.0.0/16` across 2 Availability Zones:**

```bash
python vpc_subnet_calculator.py 10.0.0.0/16 2
```

This will output a list of four subnets - 2 private, and 2 public.  For example:

```
10.0.0.0/17
10.0.128.0/17
10.0.192.0/18
10.0.64.0/18
```

**Example 2: Calculate subnets for a VPC with CIDR range `192.168.0.0/24` across 3 Availability Zones:**

```bash
python vpc_subnet_calculator.py 192.168.0.0/24 3
```

This will output a list of six subnets - 3 private and 3 public. Note that the bitmask may change depending on the cidr range and number of AZs.  For example:

```
192.168.0.0/26
192.168.0.64/26
192.168.0.128/26
192.168.0.192/27
192.168.0.32/27
192.168.0.160/27
```

## Limitations or Notes

*   The script requires the `netaddr` library. Make sure you have it installed (`pip install netaddr`).
*   The script assumes the goal is to create equally sized subnets, and chooses sizes to create the largest possible subnets that fit within the provided CIDR range and number of AZs.
*   The script enforces AWS VPC subnet size limits. It will raise a `ValueError` if the calculated subnet size is outside the acceptable range (/16 to /28).
*   Error handling is basic; invalid inputs may cause the script to crash.
```
