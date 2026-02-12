# Random Password Generator

## Overview
This Python utility provides a flexible way to generate strong, random passwords. It allows for extensive customization of password length, inclusion of various character types (uppercase, lowercase, numbers, special characters), and even generation of passwords composed of unique characters.

## Features
*   **Customizable Length:** Define minimum and maximum password lengths.
*   **Character Type Control:** Specify minimum counts for uppercase letters, lowercase letters, numbers, and special characters.
*   **Character Exclusion:** Exclude specific characters from being used in generated passwords for each character type.
*   **Non-Duplicate Passwords:** Generate passwords where each character is unique.
*   **Flexible Character Sets:** Utilizes a comprehensive set of alphanumeric and special characters.
*   **Security Conscious:** Employs `secrets.choice` for cryptographic randomness where available, falling back to `random.choice`.

## Installation
This is a single-file Python script with no external dependencies beyond the standard library. To use it, simply download the `password_generator.py` file to your project directory.

## Usage
The `password_generator.py` script provides a `PasswordGenerator` class, which can be imported and used within your Python applications or scripts.

**Basic Steps:**
1.  Import the `PasswordGenerator` class from the `password_generator.py` file.
2.  Create an instance of `PasswordGenerator`.
3.  Optionally, set various properties on the instance to customize the password generation rules.
4.  Call the `generate()`, `non_duplicate_password()`, or `shuffle_password()` methods.

### Available Properties for Customization:
You can set these properties on a `PasswordGenerator` instance before calling `generate()`:

| Property          | Description                                            | Default Value |
| :---------------- | :----------------------------------------------------- | :------------ |
| `minlen`          | Minimum length of the generated password               | 6             |
| `maxlen`          | Maximum length of the generated password               | 16            |
| `minuchars`       | Minimum uppercase characters required in password      | 1             |
| `minlchars`       | Minimum lowercase characters required in password      | 1             |
| `minnumbers`      | Minimum numbers required in password                   | 1             |
| `minschars`       | Minimum special characters required in password        | 1             |
| `excludeuchars`   | String of uppercase characters to exclude              | `""`          |
| `excludelchars`   | String of lowercase characters to exclude              | `""`          |
| `excludenumbers`  | String of numbers to exclude                           | `""`          |
| `excludeschars`   | String of special characters to exclude                | `""`          |

## Examples

To use the generator, save the provided source code as `password_generator.py`. You can then interact with it in another Python script or a Python REPL:

```python
# Assuming password_generator.py is in the same directory
from password_generator import PasswordGenerator

# 1. Generate a basic password with default settings
print("--- Basic Password ---")
generator = PasswordGenerator()
password = generator.generate()
print(f"Generated password: {password}")
# Example output: pM!3N$fJ9gT8

# 2. Generate a password with custom length requirements
print("\n--- Custom Length Password ---")
generator_custom_len = PasswordGenerator()
generator_custom_len.minlen = 10
generator_custom_len.maxlen = 20
password_custom_len = generator_custom_len.generate()
print(f"Generated password (10-20 chars): {password_custom_len}")
# Example output: K3qW6c#@Lz5G

# 3. Generate a password with specific character requirements
print("\n--- Specific Character Requirements ---")
generator_strong = PasswordGenerator()
generator_strong.minlen = 12
generator_strong.maxlen = 12 # Fixed length
generator_strong.minuchars = 3
generator_strong.minlchars = 3
generator_strong.minnumbers = 3
generator_strong.minschars = 3
password_strong = generator_strong.generate()
print(f"Generated strong password (3 each type, 12 chars): {password_strong}")
# Example output: G1@hI!j2K3^l

# 4. Generate a password excluding certain characters
print("\n--- Exclude Characters ---")
generator_exclude = PasswordGenerator()
generator_exclude.minlen = 15
generator_exclude.maxlen = 15
generator_exclude.excludelchars = "aeiou" # Exclude lowercase vowels
generator_exclude.excludeuchars = "AEIOU" # Exclude uppercase vowels
generator_exclude.excludenumbers = "015"   # Exclude digits 0, 1, 5
password_exclude = generator_exclude.generate()
print(f"Generated password (no vowels, no 0,1,5): {password_exclude}")
# Example output: W#X-2Y4b6c$d7

# 5. Generate a non-duplicate character password
print("\n--- Non-Duplicate Password ---")
generator_unique = PasswordGenerator()
password_unique = generator_unique.non_duplicate_password(10)
print(f"Generated unique char password (10 chars): {password_unique}")
# Example output: Xm3(v.2bL^

# Attempting to generate a password that exceeds the unique character limit
try:
    generator_unique.non_duplicate_password(80) 
except ValueError as e:
    print(f"Attempted to generate too long a unique password: {e}")
    # Expected output: Attempted to generate too long a unique password: Length should be less than 77 characters.

# 6. Using the shuffle_password method
print("\n--- Shuffle Password ---")
# Note: This method generates a *new* password by randomly selecting characters
# from the input string up to the specified maxlen, then shuffling them.
shuffled_password = generator.shuffle_password("MyStrongPass123", 10)
print(f"New 10-char password from 'MyStrongPass123': {shuffled_password}")
# Example output: rSg13oPytS (composed of characters from "MyStrongPass123")
```

## Limitations or Notes
*   **`shuffle_password` Behavior:** The `shuffle_password(password, maxlen)` method does not simply reorder the characters of the input `password`. Instead, it constructs a *new* password of `maxlen` characters by randomly selecting characters *from* the input `password`'s characters and then shuffling this new set. This means the output might not contain all characters from the input, or might contain duplicates even if the input had none.
*   **`non_duplicate_password` Length:** The `non_duplicate_password` method will raise a `ValueError` if the requested `maxlen` is 77 or greater, as stated in the source code's error message: "Length should be less than 77 characters." This limitation is due to the fixed number of unique characters available in the generator's internal character set.
*   **No Command-Line Interface:** This script is designed to be imported and used programmatically as a Python module. It does not provide a direct command-line interface for generating passwords.
