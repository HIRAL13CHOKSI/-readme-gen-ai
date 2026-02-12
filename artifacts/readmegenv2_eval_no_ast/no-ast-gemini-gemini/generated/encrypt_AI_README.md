This script provides a simple command-line utility for encrypting and decrypting files using AES-256 encryption. It takes a password from the user, derives an encryption key using SHA256, and then applies AES in CBC mode to secure the specified file.

## Overview

`encrypt.py` is a Python script that offers an interactive interface to encrypt or decrypt files. It secures your data by converting it into an unreadable format using a password-derived key and AES-256 encryption, and can revert the process to restore the original file.

## Features

*   **AES-256 Encryption:** Utilizes the Advanced Encryption Standard with a 256-bit key in Cipher Block Chaining (CBC) mode.
*   **Password-Based Key Derivation:** Derives a secure 256-bit encryption key from a user-provided password using the SHA256 hashing algorithm.
*   **Unique Initialization Vector (IV):** Generates a random 16-byte IV for each encryption operation to enhance security.
*   **File Handling:** Processes files in chunks (64KB), making it suitable for encrypting and decrypting large files efficiently.
*   **Interactive Command Line:** Guides the user through encryption and decryption steps via simple prompts.

## Installation

This script relies on the `pycryptodome` library for cryptographic operations. If you encounter a `ModuleNotFoundError` for `Crypto`, you need to install it.

Install the necessary library using pip:

```bash
pip install pycryptodome
```

## Usage

To use the script, run it directly from your terminal. It will then prompt you to choose between encrypting or decrypting a file, and ask for the filename and your password.

```bash
python encrypt.py
```

Follow the on-screen instructions:
1.  Enter `E` (or `e`) to encrypt or `D` (or `d`) to decrypt.
2.  Provide the path to the file you wish to process.
3.  Enter the password. This password will be used to derive the encryption key. For decryption, you must use the *exact same password* used during encryption.

## Examples

### 1. Encrypting a file

Let's say you have a file named `mysecretnotes.txt` that you want to encrypt.

```bash
$ python encrypt.py
Would you like to (E)ncrypt or (D)ecrypt?: E
File to encrypt: mysecretnotes.txt
Password: my_strong_password_123
Done.
```

After encryption, a new file will be created in the same directory, typically named `(encrypted)mysecretnotes.txt`. The original file remains untouched.

### 2. Decrypting a file

To decrypt the file you just encrypted, use the `(encrypted)` prefixed filename and the *same password*.

```bash
$ python encrypt.py
Would you like to (E)ncrypt or (D)ecrypt?: D
File to decrypt: (encrypted)mysecretnotes.txt
Password: my_strong_password_123
Done.
```

This will restore the original `mysecretnotes.txt` file, overwriting it if it already exists.

## Limitations or Notes

*   **Interactive Only:** The script currently operates exclusively through interactive command-line prompts and does not support command-line arguments for non-interactive use.
*   **Password Security:** The strength of your encryption is directly tied to the strength of your password. Always use strong, unique passwords. There is no password strength validation within the script.
*   **Filename Convention:** When a file is encrypted, the output file is named `(encrypted)<original_filename>`. For decryption, the script expects this `(encrypted)` prefix to correctly determine the original filename for output.
*   **Padding:** The script uses simple space padding for the last block during encryption. While generally effective due to post-decryption truncation, it's a basic form of padding.
