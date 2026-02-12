# Encrypt/Decrypt Utility

## Overview
This Python script provides a simple command-line utility for encrypting and decrypting files using AES (Advanced Encryption Standard) encryption. It utilizes a password-based key derivation method to secure the files, ensuring that sensitive data can be safely stored and transmitted.

## Features
- AES encryption in CBC (Cipher Block Chaining) mode.
- Password-based key generation using SHA-256 hashing.
- Ability to encrypt and decrypt files with a simple command-line interface.
- Automatically handles file sizes and initialization vectors (IVs).

## Installation
To use this script, you need to have Python installed on your machine along with the `pycryptodome` library, which provides the necessary cryptographic functions.

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install the `pycryptodome` library using pip:
   ```bash
   pip install pycryptodome
   ```

## Usage
Run the script from the command line. You will be prompted to choose between encrypting or decrypting a file.

### Example Commands
1. To encrypt a file:
   ```bash
   python encrypt.py
   ```
   - Follow the prompts to enter the file name and password.

2. To decrypt a file:
   ```bash
   python encrypt.py
   ```
   - Follow the prompts to enter the encrypted file name and password.

## Examples
- **Encrypting a file named `example.txt`:**
  ```
  Would you like to (E)ncrypt or (D)ecrypt?: E
  File to encrypt: example.txt
  Password: my_secure_password
  Done.
  ```

- **Decrypting the previously encrypted file:**
  ```
  Would you like to (E)ncrypt or (D)ecrypt?: D
  File to decrypt: (encrypted)example.txt
  Password: my_secure_password
  Done.
  ```

## Limitations or Notes
- Ensure that the `pycryptodome` library is installed, as the script will fail to run without it.
- The script creates an encrypted file prefixed with `(encrypted)`; ensure you have the correct file name when decrypting.
- The encryption process pads the file to ensure its size is a multiple of 16 bytes, which is required for AES.
- Always use strong passwords to enhance the security of your encrypted files.
