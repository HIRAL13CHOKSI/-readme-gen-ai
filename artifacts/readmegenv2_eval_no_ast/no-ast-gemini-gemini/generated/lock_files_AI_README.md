# lock_files.py

Encrypt and decrypt files using AES encryption.

## Overview

`lock_files.py` is a Python utility for securely encrypting and decrypting files, primarily designed to protect sensitive data before it's uploaded to cloud storage services like Dropbox or Google Drive. It employs AES encryption with a common password.

By default, the script encrypts files by appending a `.locked` extension (e.g., `document.txt` becomes `document.txt.locked`) and removes the original file. Decryption reverses this process, looking for files with the specified extension. The tool supports processing individual files and entire directories, offers various methods for password input (command line, secure file, or interactive prompt), includes OpenSSL compatibility, and leverages multi-threading for efficient processing.

## Features

*   **AES Encryption/Decryption:** Securely locks and unlocks files using the Advanced Encryption Standard.
*   **Flexible Password Input:**
    *   **Interactive Prompt (Default):** Prompts the user to enter the password twice for confirmation.
    *   **Password File (`-p`/`--password-file`):** Reads the password from the first non-comment, non-empty line of a specified file.
    *   **Command Line (`-P`/`--password`):** Allows specifying the password directly as an argument (note: less secure for sensitive passwords).
*   **Lock/Unlock Modes:**
    *   **Lock (`-l`/`--lock`):** The default action. Encrypts files and appends a configurable suffix (default: `.locked`). The original file is removed.
    *   **Unlock (`-u`/`--unlock`):** Decrypts files by removing the configured suffix. The encrypted file is removed.
*   **Recursive Directory Processing (`-r`/`--recurse`):** Traverses into subdirectories to find and process all files.
*   **Customizable Suffix (`-s`/`--suffix`):** Change the default `.locked` extension to any custom string (e.g., `.enc`, `.mysecret`).
*   **In-Place Operation (`-i`/`--inplace`):** Encrypts or decrypts a file without changing its name, overwriting the original content. (See Limitations below for important notes).
*   **OpenSSL Compatibility (`-c`/`--openssl`):** Encrypt and decrypt files in a format compatible with OpenSSL's `enc -aes-256-cbc` command. This option must be used consistently for both operations.
*   **Multi-threading (`-j NUM_THREADS`/`--jobs NUM_THREADS`):** Configures the maximum number of active threads for parallel file processing, improving performance for large sets of files. Default is 1.
*   **Verbose Output (`-v`/`--verbose`):** Control the level of output. A single `-v` provides a summary report; `-vv` shows detailed information for each file processed.
*   **Error Handling (`-W`/`--warn`):** By default, the script exits on file processing errors. This option changes errors to warnings, allowing the program to continue processing other files.
*   **Output Line Wrapping (`-w INTEGER`/`--wll INTEGER`):** Specifies the maximum line width for the base64 encoded encrypted output. Set to `0` to disable line wrapping. Default is `72`.

## Installation

This is a single-file Python script. To use it:

1.  **Download the script:** Save the `lock_files.py` file to your preferred location.
2.  **Install dependencies:** This script requires the `cryptography` Python library. Install it using pip:
    ```bash
    pip install cryptography
    ```
3.  **Make it executable (Optional, on Linux/macOS):**
    ```bash
    chmod +x lock_files.py
    ```

You can then run the script using `python lock_files.py` or `./lock_files.py` (if made executable).

## Usage

```
USAGE:
  lock_files.py [OPTIONS] [<FILES_OR_DIRS>]+
```

**POSITIONAL ARGUMENTS:**

*   `FILES`                 One or more files or directories to process.

**OPTIONS:**

*   `-h, --help`            Show this help message and exit.
*   `-c, --openssl`         Enable OpenSSL compatibility. This option must be specified for both encryption and decryption operations if OpenSSL compatibility is desired.
*   `-d, --decrypt`         Unlock/decrypt files. (Deprecated; use `--unlock`).
*   `-e, --encrypt`         Lock/encrypt files. (Deprecated; use `--lock`).
*   `-i, --inplace`         Enable in-place mode. Overwrites files with encrypted/decrypted content. Equivalent to `-o -s ''`.
*   `-j NUM_THREADS, --jobs NUM_THREADS`
    Specify the maximum number of active threads for parallel processing. Default: `1`.
*   `-l, --lock`            Explicitly set to lock files. This is the default action if neither `--lock` nor `--unlock` is specified.
*   `-o, --overwrite`       Overwrite files that already exist without prompting. Used implicitly with `--inplace`.
*   `-p PASSWORD_FILE, --password-file PASSWORD_FILE`
    Specify a file from which to read the password. The first non-empty, non-comment line will be used.
*   `-P PASSWORD, --password PASSWORD`
    Specify the password directly on the command line.
*   `-r, --recurse`         Recurse into subdirectories when a directory is specified as an input.
*   `-s EXTENSION, --suffix EXTENSION`
    Specify the file extension to use for locked files. Default: `.locked`.
*   `-u, --unlock`          Explicitly set to unlock files. Searches for files with the configured suffix.
*   `-v, --verbose`         Increase the level of verbosity. Use `-vv` for very detailed output.
*   `-V, --version`         Show the program's version number and exit.
*   `-w INTEGER, --wll INTEGER`
    Set the line width for base64 encoded encrypted output. `0` disables line wrapping. Default: `72`.
*   `-W, --warn`            Treat file modification errors as warnings, allowing the script to continue instead of exiting.

## Examples

```bash
# Example 1: Show help message
$ lock_files.py -h

# Example 2: Lock and then unlock a single file using a command-line password
$ lock_files.py -P 'supersecret' file.txt
$ ls file.txt*
file.txt.locked
$ lock_files.py -P 'supersecret' --unlock file.txt.locked
$ ls -1 file.txt*
file.txt

# Example 3: Lock and then unlock a set of directories recursively
$ lock_files.py -P 'supersecret' -r project1 project2
$ find project1 project2 --type f -name '*.locked'
# (output snipped, shows .locked files)
$ lock_files.py -P 'supersecret' -r --unlock project1 project2

# Example 4: Lock and then unlock using a custom extension
$ lock_files.py -P 'anothersecret' -s .EncRypt file.txt
$ ls file.txt*
file.txt.EncRypt
$ lock_files.py -P 'anothersecret' -s .EncRypt --unlock file.txt.EncRypt

# Example 5: Lock and then unlock a file in place (content changes, filename doesn't)
# WARNING: This mode is dangerous; data loss can occur if disk fills up during write.
$ lock_files.py -P 'inplacesecret' -i -l file.txt
$ ls file.txt*
file.txt
$ lock_files.py -P 'inplacesecret' -i -u file.txt
$ ls file.txt*
file.txt

# Example 6: Use a password file for convenience and security
$ echo 'mycomplexpassword' >pass.txt
$ chmod 0600 pass.txt # Recommended for security to restrict file permissions
$ lock_files.py -p pass.txt -l document.docx
$ lock_files.py -p pass.txt -u document.docx.locked

# Example 7: Encrypt and decrypt in an OpenSSL compatible manner
$ echo 'opensslpass' >pass.txt
$ chmod 0600 pass.txt
$ lock_files.py -p pass.txt -c -l openssl_file.txt
$ # Decrypt the locked file using OpenSSL
$ openssl enc -aes-256-cbc -d -a -salt -pass file:pass.txt -in openssl_file.txt.locked
$ # Encrypt a file using OpenSSL and then decrypt it using lock_files.py
$ openssl enc -aes-256-cbc -e -a -salt -pass pass:opensslpass -in original.txt -out original.txt.locked
$ lock_files.py -p pass.txt -c -u original.txt.locked
```

## Limitations or Notes

*   **Security of `--password`:** Specifying passwords directly on the command line (`-P`) is generally less secure as the password may be exposed in shell history, process listings, or logs. Using a password file (`-p`) or the interactive prompt is recommended for sensitive information.
*   **In-Place Mode (`-i`/`--inplace`) Risks:** While convenient, `in-place` mode carries a risk of data loss. If a write operation fails (e.g., due to a disk full error or power loss), the original file content might be corrupted or lost permanently. Use with caution.
*   **Deprecated Options:** The `-d`/`--decrypt` and `-e`/`--encrypt` options are deprecated. Please use `-u`/`--unlock` and `-l`/`--lock` respectively.
*   **Multiple Lockings:** You can apply the lock operation multiple times to the same file. Each time, another instance of the suffix (e.g., `.locked`) will be appended (e.g., `file.txt.locked.locked`). Each unlock operation will remove one suffix.
*   **OpenSSL Compatibility (`-c`):** When using the `--openssl` option, it is crucial to apply it consistently for both the encryption and decryption steps to ensure successful operations with OpenSSL.

---

**Version:** 1.1.3
**Copyright:** (c) 2015 Joe Linoff, all rights reserved
**License:** MIT Open Source
**Project:** [https://github.com/jlinoff/lock_files](https://github.com/jlinoff/lock_files)
