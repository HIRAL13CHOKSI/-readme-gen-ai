```markdown
# File Encryption/Decryption Utility

## Overview

This Python script provides basic file encryption and decryption functionality using AES encryption with a SHA256-derived key.  It prompts the user to choose between encryption and decryption, then asks for the filename and password. The script encrypts or decrypts the file using the provided password as a key.

## Features

*   Encrypts files using AES encryption.
*   Decrypts files encrypted by this script.
*   Uses SHA256 to hash the password into a secure key.
*   Prepends the original file size to the encrypted file.

## Installation

1.  **Install the `pycryptodome` library:**

    Due to the error message about the missing `Crypto` module, you must install `pycryptodome`, which provides the necessary cryptographic functions. Use pip:

    ```bash
    pip install pycryptodome
    ```

2.  **Save the script:**

    Save the provided Python code as a `.py` file (e.g., `encrypt.py`).

## Usage

1.  **Run the script:**

    ```bash
    python encrypt.py
    ```

2.  **Choose to encrypt or decrypt:**

    The script will prompt you to enter 'E' for encryption or 'D' for decryption.

3.  **Enter the filename:**

    Enter the name of the file you want to encrypt or decrypt.

4.  **Enter the password:**

    Enter the password that will be used to encrypt or decrypt the file.  Remember this password, as it is required for decryption.

## Examples

### Encryption

```
Would you like to (E)ncrypt or (D)ecrypt?: E
File to encrypt: my_document.txt
Password: mysecretpassword
Done.
```

This will create an encrypted file named `(encrypted)my_document.txt`.

### Decryption

```
Would you like to (E)ncrypt or (D)ecrypt?: D
File to decrypt: (encrypted)my_document.txt
Password: mysecretpassword
Done.
```

This will create a decrypted file named `my_document.txt`, assuming `(encrypted)my_document.txt` was created with the same password.

## Limitations or Notes

*   **Dependency:** Requires the `pycryptodome` library. Make sure to install it before running the script.
*   **Password Security:**  The security of the encryption depends entirely on the strength of the password. Use a strong, unique password.
*   **Error Handling:** The script does not include comprehensive error handling.  It will likely crash if it encounters unexpected file errors or incorrect passwords during decryption.
*   **File Size:** The script prepends 16 bytes representing the file size.
*   **Padding:** The script uses space character padding to ensure the chunks are a multiple of 16 bytes during encryption.
*   **Decryption Filename:** The decryption function assumes that the encrypted filename starts with `(encrypted)`. If the encrypted file was renamed, decryption will fail or create a file with an unexpected name.
```
