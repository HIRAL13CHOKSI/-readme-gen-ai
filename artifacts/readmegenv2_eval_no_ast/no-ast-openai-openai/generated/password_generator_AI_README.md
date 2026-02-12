# Password Generator

## Overview
The Password Generator is a Python utility that creates random passwords based on customizable criteria. It allows users to specify the minimum and maximum length of the password, as well as the required number of uppercase letters, lowercase letters, numbers, and special characters.

## Features
- Generate random passwords with customizable properties.
- Specify minimum and maximum password lengths.
- Set requirements for the number of uppercase letters, lowercase letters, numbers, and special characters.
- Option to exclude specific characters from the password generation.
- Generate non-duplicate passwords.

## Installation
To use the Password Generator, ensure you have Python installed on your system. You can run the script directly without any additional installations, as it uses built-in libraries.

## Usage
To use the Password Generator, you can create an instance of the `PasswordGenerator` class and call its methods. Below are example commands demonstrating how to generate passwords.

### Example Commands
```python
from password_generator import PasswordGenerator

# Create an instance of the PasswordGenerator
password_gen = PasswordGenerator()

# Generate a random password with default settings
password = password_gen.generate()
print("Generated Password:", password)

# Customize properties
password_gen.minlen = 8
password_gen.maxlen = 12
password_gen.minuchars = 2
password_gen.minlchars = 2
password_gen.minnumbers = 2
password_gen.minschars = 2

# Generate a password with custom settings
custom_password = password_gen.generate()
print("Custom Generated Password:", custom_password)

# Generate a non-duplicate password of length 10
non_duplicate_password = password_gen.non_duplicate_password(10)
print("Non-Duplicate Password:", non_duplicate_password)
```

## Examples
1. **Default Password Generation**:
   - Generates a password with default settings (minimum length of 6, maximum length of 16, and at least one of each character type).

2. **Custom Password Generation**:
   - Set custom requirements for a password (e.g., minimum length of 8, at least 2 uppercase letters, 2 lowercase letters, 2 numbers, and 2 special characters).

3. **Non-Duplicate Password**:
   - Generate a password that does not repeat any characters, up to a specified length.

## Limitations or Notes
- The minimum length of the password must be at least the sum of the required character types (uppercase, lowercase, numbers, special characters).
- The maximum length must be greater than or equal to the minimum length.
- The `non_duplicate_password` method can only generate passwords of length less than 77 characters due to character limitations.
- If the required character types exceed the maximum length, a `ValueError` will be raised.

This utility is designed to help users create secure passwords easily while allowing for customization based on their security needs.
