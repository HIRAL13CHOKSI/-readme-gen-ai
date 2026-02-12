```markdown
# AWS VPC Subnet Calculator

## Overview

This script is a command-line utility designed to assist in planning AWS Virtual Private Cloud (VPC) network configurations. It calculates suitable CIDR block subnets based on a given VPC CIDR range and the desired number of Availability Zones (AZs). The script generates two sets of subnets, typically for private and public network tiers, ensuring they adhere to common AWS VPC subnet sizing requirements.

## Features

*   **AWS VPC Subnet Calculation:** Automatically determines appropriate subnet CIDR blocks for a given VPC range, considering the number of Availability Zones.
*   **Multi-AZ Support:** Generates subnets suitable for deployment across a specified number of Availability Zones.
*   **Tiered Allocation:** Allocates an initial set of subnets (implicitly designed for "private" resources) and then finds the largest contiguous remaining IP space to allocate a second set of subnets (implicitly for "public" resources).
*   **AWS Constraints Aware:** Enforces AWS VPC subnet mask size limits, restricting allocations to between `/16` and `/28`.
*   **Robust IP Handling:** Leverages the `netaddr` library for accurate and efficient IP address and subnet manipulation.

## Installation

1.  **Save the script:** Save the provided Python code as `vpc_subnet_calculator.py`.
2.  **Install dependencies:** This script requires the `netaddr` Python library. You can install it using `pip`:

    ```bash
    pip install netaddr
    ```

## Usage

The script is executed from the command line and requires two positional arguments: the main VPC CIDR range and the number of Availability Zones.

```bash
python vpc_subnet_calculator.py <VPC_CIDR_RANGE> <NUMBER_OF_AZS>
```

*   `<VPC_CIDR_RANGE>`: The main CIDR block for your VPC (e.g., `10.0.0.0/16`, `172.31.0.0/20`).
*   `<NUMBER_OF_AZS>`: An integer representing the number of Availability Zones you plan to use for your subnets.

The script will output the calculated subnet CIDR blocks, one per line. The first set of subnets printed will correspond to the first allocation (e.g., "private"), followed by the second set (e.g., "public").

## Examples

#### Example 1: Calculate subnets for a `10.0.0.0/16` VPC across 2 Availability Zones

```bash
python vpc_subnet_calculator.py 10.0.0.0/16 2
```

**Output:**

```
10.0.0.0/18
10.0.64.0/18
10.0.128.0/19
10.0.160.0/19
```

*Explanation: The script first allocates two /18 subnets (for the 2 AZs) from `10.0.0.0/16`. Then, it identifies the largest remaining block (`10.0.128.0/17`) and allocates two /19 subnets from it for the second tier.*

#### Example 2: Calculate subnets for a `172.31.0.0/20` VPC across 3 Availability Zones

```bash
python vpc_subnet_calculator.py 172.31.0.0/20 3
```

**Output:**

```
172.31.0.0/22
172.31.4.0/22
172.31.8.0/22
172.31.12.0/24
172.31.13.0/24
172.31.14.0/24
```

*Explanation: The script allocates three /22 subnets from `172.31.0.0/20`. The largest remaining block is then identified as `172.31.12.0/22`, from which three /24 subnets are allocated for the second tier.*

## Limitations or Notes

*   **AWS-Specific Constraints:** The script explicitly incorporates AWS VPC subnet mask constraints, limiting valid subnet sizes to between `/16` and `/28`. Input that would result in subnets outside this range will raise an error.
*   **Priority in Allocation:** The script prioritizes the first set of subnets by allocating them directly from the main VPC CIDR. The second set of subnets is then allocated from the largest *remaining* contiguous IP block.
*   **Equal Subnet Sizing per Tier:** Within each allocated tier (e.g., all "private" subnets, or all "public" subnets), the script will allocate subnets of the same CIDR mask size to simplify planning.
```
