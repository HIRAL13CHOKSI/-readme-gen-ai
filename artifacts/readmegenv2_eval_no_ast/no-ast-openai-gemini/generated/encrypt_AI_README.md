# Encrypt.py README

## Overview
`encrypt.py` is a standalone Python script that provides functionality for encrypting and decrypting files using the AES (Advanced Encryption Standard) algorithm. It utilizes a password to generate a secure encryption key and supports file operations in CBC (Cipher Block Chaining) mode.

## Features
- Encrypt and decrypt files securely using AES.
- Password-based key generation using SHA-256 hashing.
- Handles files in chunks to support large files.
- Automatically creates an output file with a prefix "(encrypted)" for encrypted files.

## Installation
To run this script, you need to have Python installed along with the `pycryptodome` library, which provides the necessary cryptographic functions. You can install it using pip:

```bash
pip install pycryptodome
```

Make sure to have the required permissions to read and write files in the directory where you are running the script.

## Usage
To use the script, run it from the command line. You will be prompted to choose between encrypting or decrypting a file.

### Example Commands
1. **Encrypt a file:**
   ```bash
   python encrypt.py
   ```
   - Follow the prompts to enter the file name and password.

2. **Decrypt a file:**
   ```bash
   python encrypt.py
   ```
   - Follow the prompts to enter the encrypted file name and password.

## Examples
1. **Encrypting a file named `example.txt`:**
   - Run the script and select 'E' for encrypt.
   - Enter `example.txt` when prompted for the file name.
   - Enter a secure password when prompted.

2. **Decrypting the file:**
   - Run the script and select 'D' for decrypt.
   - Enter `(encrypted)example.txt` when prompted for the file name.
   - Enter the same password used for encryption.

## Limitations or Notes
- The script requires the `pycryptodome` library. Ensure it is installed before running the script.
- The encrypted file will have the prefix "(encrypted)" added to its name.
- The script handles padding for files that are not a multiple of 16 bytes in length.
- Ensure that you remember the password used for encryption, as it is required for decryption.
- The script does not handle exceptions or errors extensively; ensure that the file paths and passwords are correct to avoid runtime errors.
