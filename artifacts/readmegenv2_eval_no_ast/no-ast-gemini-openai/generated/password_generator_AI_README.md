```markdown
# Password Generator

## Overview

This Python script provides a `PasswordGenerator` class for generating random passwords with customizable properties.  It allows you to specify minimum and maximum lengths, the minimum number of uppercase, lowercase, numeric, and special characters, and characters to exclude. It offers methods to generate passwords, shuffle existing strings into passwords, and create non-duplicate character passwords.

## Features

*   **Customizable Password Generation:** Control password length and character composition.
*   **Character Set Control:** Specify the minimum number of uppercase, lowercase, numeric, and special characters.
*   **Exclusion Lists:** Exclude specific characters from generated passwords.
*   **Password Shuffling:** Shuffle any given string into a password of a given length.
*   **Non-duplicate Character Passwords:** Generate passwords where each character is unique (up to a maximum length).

## Installation

No installation is required. The script is self-contained and requires no external dependencies beyond the Python standard library.  Just save the script as `password_generator.py`.

## Usage

To use the `PasswordGenerator` class, import it into your Python script:

```python
from password_generator import PasswordGenerator

# Create a PasswordGenerator object
pg = PasswordGenerator()

# Customize password properties (optional)
pg.minlen = 8  # Minimum length: 8
pg.maxlen = 12 # Max length: 12
pg.minuchars = 2 # Min. uppercase: 2
pg.minlchars = 2 # Min. lowercase: 2
pg.minnumbers = 2 # Min. numbers: 2
pg.minschars = 2 # Min. special chars: 2

# Generate a password
password = pg.generate()
print(password)

# Shuffle an existing string into a password
shuffled_password = pg.shuffle_password("mysecretkey", 10)
print(shuffled_password)

# Generate a password with non-duplicate characters
non_duplicate_password = pg.non_duplicate_password(10)
print(non_duplicate_password)
```

## Examples

Here are a few examples of how to use the `PasswordGenerator` class:

**Example 1: Basic password generation with default settings:**

```python
from password_generator import PasswordGenerator

pg = PasswordGenerator()
password = pg.generate()
print(password)
```

**Example 2: Password with custom length and character requirements:**

```python
from password_generator import PasswordGenerator

pg = PasswordGenerator()
pg.minlen = 12
pg.maxlen = 16
pg.minuchars = 3
pg.minlchars = 3
pg.minnumbers = 3
pg.minschars = 3
password = pg.generate()
print(password)
```

**Example 3: Shuffling a string into a password:**

```python
from password_generator import PasswordGenerator

pg = PasswordGenerator()
shuffled_password = pg.shuffle_password("myverystrongpassword", 15)
print(shuffled_password)
```

**Example 4: Generate non-duplicate password**
```python
from password_generator import PasswordGenerator

pg = PasswordGenerator()
non_duplicate_password = pg.non_duplicate_password(10)
print(non_duplicate_password)
```

## Limitations or Notes

*   The `non_duplicate_password` method is limited to a maximum length of 76 characters because it uses the predefined character sets, which contain 76 unique values.
*   Error handling is limited to checking negative character lengths and if `minlen` exceeds `maxlen`.
*   The `secrets` module is preferred for generating cryptographically secure random numbers if available (Python 3.6+). If not, it falls back to `random.choice`.
```
