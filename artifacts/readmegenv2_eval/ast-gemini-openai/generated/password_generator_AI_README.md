# Password Generator

A random password generator.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

## Overview

This Python script provides a `PasswordGenerator` class to generate strong, random passwords with customizable properties. It allows you to specify the minimum and maximum length of the password, as well as the minimum number of uppercase characters, lowercase characters, numbers, and special characters required.

Notable features:

-   Customizable password complexity.
-   Option to generate non-duplicate passwords.
-   Password shuffling for added security.

## Requirements

-   Python 3.7+
-   Any operating system that supports Python 3.7+

## Dependencies

### Standard Library

-   `copy`
-   `random`
-   `secrets`
-   `string`

### Third-Party Packages

-   `google-generativeai`
-   `groq`
-   `openai`

## Installation

To install the Password Generator and its dependencies, use the following command:

```bash
pip install -r ../requirements.txt
```

Alternatively, you can install it in editable mode:

```bash
pip install -e .
```

## Usage

```
python password_generator.py
```

## Flags

None

## Examples

1.  Generate a password using the default settings:

    ```bash
    python password_generator.py
    ```

## Input/Output

| Input  | Output                     |
| :----- | :------------------------- |
| *None* | A randomly generated password |

## Testing

To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting

1.  **Issue**: The script fails to run due to missing dependencies.
    **Solution**: Ensure all dependencies are installed using `pip install -r ../requirements.txt`.

2.  **Issue**: Passwords generated are not strong enough.
    **Solution**: Customize the `PasswordGenerator` class properties to increase the minimum requirements for character types and password length.

## Contributing

Coming soon

## License

Coming soon
