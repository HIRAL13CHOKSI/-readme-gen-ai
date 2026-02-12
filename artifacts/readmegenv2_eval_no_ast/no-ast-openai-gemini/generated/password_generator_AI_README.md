# Password Generator

## Overview
The Password Generator is a Python utility designed to create secure, random passwords based on customizable criteria. It allows users to specify the minimum and maximum length of the password, as well as the required number of uppercase letters, lowercase letters, numbers, and special characters.

## Features
- Generate random passwords with customizable criteria.
- Ensure a minimum number of specific character types (uppercase, lowercase, numbers, special characters).
- Shuffle generated passwords for added security.
- Generate non-duplicate passwords of specified lengths.

## Installation
To use the Password Generator, you need Python installed on your system. This script is standalone and does not require any external libraries beyond the Python standard library.

1. Download the script from the repository or copy the code into a file named `password_generator.py`.
2. Ensure you have Python 3.x installed.

## Usage
To use the Password Generator, you can create an instance of the `PasswordGenerator` class and call its methods to generate passwords.

### Example Commands
```python
from password_generator import PasswordGenerator

# Create an instance of the PasswordGenerator
password_gen = PasswordGenerator()

# Generate a password with default settings
password = password_gen.generate()
print("Generated Password:", password)

# Customize settings
password_gen.minlen = 8
password_gen.maxlen = 12
password_gen.minuchars = 2
password_gen.minlchars = 2
password_gen.minnumbers = 2
password_gen.minschars = 2

# Generate a customized password
custom_password = password_gen.generate()
print("Custom Generated Password:", custom_password)

# Generate a non-duplicate password of length 10
non_duplicate_password = password_gen.non_duplicate_password(10)
print("Non-Duplicate Password:", non_duplicate_password)
```

## Examples
1. **Default Password Generation**:
   ```python
   password = password_gen.generate()
   print(password)  # Example output: 'aB3$cD'
   ```

2. **Custom Password Generation**:
   ```python
   password_gen.minlen = 10
   password_gen.maxlen = 14
   password_gen.minuchars = 3
   password_gen.minnumbers = 2
   password_gen.minschars = 2
   custom_password = password_gen.generate()
   print(custom_password)  # Example output: 'A1b$C2dE!'
   ```

3. **Non-Duplicate Password**:
   ```python
   non_duplicate_password = password_gen.non_duplicate_password(10)
   print(non_duplicate_password)  # Example output: 'A1b2C3d4E5'
   ```

## Limitations or Notes
- The minimum length of the password must be at least the sum of the minimum required characters of each type.
- The maximum length must be greater than or equal to the minimum length.
- The `non_duplicate_password` method generates passwords without repeating characters, but the maximum length should not exceed 77 characters due to the available character set.
- If any of the character requirements are set to negative values, a `ValueError` will be raised.

This utility is ideal for generating secure passwords for various applications, ensuring compliance with common security standards.
