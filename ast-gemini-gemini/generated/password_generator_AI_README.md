# Password Generator

A robust and customizable random password generator script.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/suryasr007/password_generator/actions)

## Overview

`password_generator.py` is a versatile Python script designed to generate strong, random passwords. It provides fine-grained control over password characteristics, allowing users to define minimum and maximum lengths, as well as the required count of uppercase characters, lowercase characters, numbers, and special characters. Built using Python's standard library, it ensures secure random number generation.

Key features include:

*   **Customizable Password Properties**: Easily define password length, character types (uppercase, lowercase, numbers, special characters).
*   **Secure Generation**: Leverages Python's `secrets` module for cryptographically strong random number generation.
*   **Character Shuffling**: Includes methods to shuffle generated characters for enhanced randomness.

## Requirements

*   **Python**: Version 3.8 or higher.
*   **Operating System**: Cross-platform compatibility (Windows, macOS, Linux).

## Dependencies

This project relies on the following packages:

### Standard Library Modules

*   `copy`
*   `random`
*   `secrets`
*   `string`

### Third-Party Packages

While the `password_generator.py` script itself only uses standard library modules for its core functionality, the project's `requirements.txt` includes:

*   `google-generativeai`
*   `groq`
*   `openai`

## Installation

To get started, clone the repository and install the project's dependencies:

```bash
git clone https://github.com/suryasr007/password_generator.git
cd password_generator
pip install -r ..\requirements.txt
```

For development, you can install the dependencies in editable mode (though for a single script, direct execution is common):

```bash
pip install -e .
```
*(Note: The editable install command is shown as a general practice, but for a standalone script, installing dependencies via `pip install -r` and running the script directly is typical.)*

## Usage

Simply run the script from your terminal:

```bash
python password_generator.py
```

## Flags

None specified. The script runs with default parameters when executed directly.

## Environment Variables

None specified.

## Examples

The script is designed for straightforward execution, generating a random password based on its internal logic, which is informed by the `PasswordGenerator` class's default properties (e.g., minimum length 6, maximum length 16, with at least one uppercase, lowercase, number, and special character).

1.  **Basic Password Generation**

    Execute the script to generate a secure, random password:

    ```bash
    python password_generator.py
    ```

    This command will print a randomly generated password to your console, similar to:

    ```
    @rA7!pX9fQe$2
    ```

    The generated password will adhere to the default security criteria implemented within the script's `PasswordGenerator` class. To customize these criteria, you would modify the script's source code or extend it to accept runtime parameters (e.g., via CLI arguments).

## Input/Output

| Type   | Description                               |
| :----- | :---------------------------------------- |
| Input  | None (parameters are internal defaults)   |
| Output | A single string representing the generated password |

## Testing

The project includes tests to ensure the reliability of the password generation logic. To run the tests, ensure `pytest` is installed and execute the following command from the project root:

```bash
pytest
```

## Troubleshooting

1.  **"No such file or directory" when running the script:**
    *   Ensure you are in the correct directory where `password_generator.py` is located.
    *   Verify the filename is spelled correctly.
2.  **`ModuleNotFoundError` for dependencies:**
    *   Make sure you have installed all required packages using `pip install -r ..\requirements.txt`.
    *   Confirm your Python environment is correctly activated if you are using a virtual environment.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details (if available in the repository).
