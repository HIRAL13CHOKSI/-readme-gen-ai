```markdown
# lock_files.py

## Overview

`lock_files.py` is a Python utility for encrypting and decrypting files using AES encryption with a shared password. It's designed to secure files before uploading them to cloud storage services.  The script allows you to manage encryption keys through manual entry, command-line arguments, or secure password files.  It can recursively process directories and supports OpenSSL compatibility.

## Features

*   **AES Encryption:** Uses AES encryption for securing files.
*   **Password Options:** Supports password entry via command line, secure file, or interactive prompt.
*   **Recursive Processing:** Can recursively process directories to encrypt/decrypt all files within.
*   **OpenSSL Compatibility:** Offers an option to encrypt/decrypt files in a manner compatible with OpenSSL.
*   **Multi-threading:** Supports multi-threaded processing to improve performance on large sets of files.
*   **In-place Mode:** Can overwrite files in place.
*   **Custom Suffix:** Allows specifying a custom suffix for encrypted files.
*   **Warning Mode:** Can continue processing even if some files cannot be locked/unlocked.

## Installation

No installation is required.  The script is standalone and requires only the `cryptography` module, which can be installed using pip:

```bash
pip install cryptography
```

## Usage

```
lock_files.py [OPTIONS] [<FILES_OR_DIRS>]+
```

### Options

*   `-c, --openssl`: Enables OpenSSL compatibility for encryption/decryption.
*   `-d, --decrypt`: Unlock/decrypt files (deprecated, use `--unlock`).
*   `-e, --encrypt`: Lock/encrypt files (deprecated, use `--lock`).
*   `-i, --inplace`: Enables in-place mode, overwriting the original file (implies `-o -s ''`).
*   `-j NUM_THREADS, --jobs NUM_THREADS`: Specifies the maximum number of active threads (default: 1).
*   `-l, --lock`: Lock files (default action if neither `--lock` nor `--unlock` is specified).
*   `-o, --overwrite`: Overwrite existing files.
*   `-p PASSWORD_FILE, --password-file PASSWORD_FILE`: Specifies a file containing the password.
*   `-P PASSWORD, --password PASSWORD`: Specifies the password on the command line (insecure).
*   `-r, --recurse`: Recursively process subdirectories.
*   `-s EXTENSION, --suffix EXTENSION`: Specifies the extension for locked files (default: `.locked`).
*   `-u, --unlock`: Unlock files.
*   `-v, --verbose`: Increases verbosity level (single `-v` for summary, two or more for detailed output).
*   `-V, --version`: Shows the program's version number and exit.
*   `-w INTEGER, --wll INTEGER`:  The width of each locked/encrypted line (default: 72).
*   `-W, --warn`: Treat file processing failures as warnings instead of errors.

### Example Commands

1.  **Lock a single file, prompting for the password:**

    ```bash
    lock_files.py file.txt
    ```

2.  **Unlock a file using a password provided on the command line:**

    ```bash
    lock_files.py -P 'secret' --unlock file.txt.locked
    ```

3.  **Lock a directory recursively using a password file:**

    ```bash
    lock_files.py -p pass.txt -r project_dir
    ```

4.  **Lock a file using a custom suffix:**

    ```bash
    lock_files.py -P 'secret' -s .Encrypted file.txt
    ```

5.  **Unlock a file in place:**

    ```bash
    lock_files.py -P 'secret' -i -u file.txt
    ```

## Examples

1.  **Locking and unlocking a single file with interactive password prompt:**

    ```bash
    lock_files.py file.txt
    Password: <enter password>
    Re-enter password: <re-enter password>
    ls file.txt*
    file.txt.locked
    lock_files.py --unlock file.txt.locked
    Password: <enter password>
    Re-enter password: <re-enter password>
    ls file.txt*
    file.txt
    ```

2.  **Using a password file:**

    ```bash
    echo 'my_secret_password' > pass.txt
    chmod 0600 pass.txt
    lock_files.py -p pass.txt file1.txt
    lock_files.py -p pass.txt --unlock file1.txt.locked
    ```

3.  **OpenSSL compatibility:**

    ```bash
    lock_files.py -P secret -c --lock file.txt
    openssl enc -aes-256-cbc -d -a -salt -pass pass:secret -in file.txt.locked -out file.txt
    ```

## Limitations or Notes

*   Storing passwords on the command line using `-P` is insecure and not recommended.
*   In-place mode (`-i`) can lead to data loss if the disk runs out of space during the write operation.
*   The script relies on the `cryptography` module.  Ensure it's installed before running.
*   When using OpenSSL compatibility, ensure you use the `-c` flag for both encryption and decryption.
*   The number of threads specified with `-j` can impact performance. Experiment to find the optimal value for your system.
```
