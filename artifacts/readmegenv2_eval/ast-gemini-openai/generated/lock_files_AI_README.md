# lock_files.py

Encrypt and decrypt files using AES encryption.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/username/repo/actions/workflows/tests.yml/badge.svg)](https://github.com/username/repo/actions/workflows/tests.yml)

## Overview

`lock_files.py` is a command-line tool for encrypting and decrypting files using AES encryption with a user-provided password. It's designed to lock files before uploading them to cloud storage services, providing an extra layer of security.

Key features:

*   Encrypt and decrypt individual files or entire directories.
*   Multiple password input methods: command-line, password file, or interactive prompt.
*   Multi-threading support for faster processing of large files.
*   Compatibility mode for OpenSSL interoperability.

This tool utilizes the external tool `getconf` for determining available cores.

## Requirements

*   Python 3.7+
*   Any operating system that supports Python.

## Dependencies

### Standard Library

*   argparse
*   base64
*   getpass
*   inspect
*   multiprocessing
*   os
*   queue
*   subprocess
*   sys
*   threading

### Third-Party Packages

*   cryptography
*   google-generativeai
*   groq
*   openai
*   Queue

### External Tools

*   `getconf`: Used to determine the number of available processor cores.

## Installation

Install the required dependencies using pip:

```bash
pip install -r ../requirements.txt
```

For an editable install:

```bash
pip install -e .
```

## Usage

```
python lock_files.py --openssl --decrypt --encrypt --inplace --jobs <value> --lock --overwrite --password-file <value> --password <value> --recurse --suffix <value> --unlock --verbose <value> --version <value> --wll <value> --warn FILES <value1> <value2> ...
```

## Flags

| Flag          | Alias | Type    | Required | Default   | Help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------|-------|---------|----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--openssl`   | `-c`  | bool    | No       |           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--decrypt`   | `-d`  | bool    | No       |           | Unlock/decrypt files. This option is deprecated. It is the same as --unlock.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--encrypt`   | `-e`  | bool    | No       |           | Lock/encrypt files. This option is deprecated. This is the same as --lock and is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--inplace`   | `-i`  | bool    | No       |           | In place mode. Overwrite files in place. It is the same as specifying: -o -s '' This is a dangerous because a disk full operation can cause data to be lost when a write fails. This allows you to duplicate the behavior of the previous version.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `--jobs`      | `-j`  | int     | No       | `1`       | Specify the maximum number of active threads. This can be helpful if there a lot of large files to process where large refers to files larger than a MB. Default: `1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `--lock`      | `-l`  | bool    | No       |           | Lock files. Files are locked and the ".locked" extension is appended unless the --suffix option is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--overwrite` | `-o`  | bool    | No       |           | Overwrite files that already exist. This can be used in conjunction disable file existence checks. It is used by the --inplace mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--password-file` | `-p` | str     | No       |           | file that contains the password. The default behavior is to prompt for the password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--password`  | `-P`  | str     | No       |           | Specify the password on the command line. This is not secure because it is visible in the command history.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `--recurse`   | `-r`  | bool    | No       |           | Recurse into subdirectories.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `--suffix`    | `-s`  | str     | No       | `.locked` | Specify the extension used for locked files. Default: `.locked`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `--unlock`    | `-u`  | bool    | No       |           | Unlock files. Files with the ".locked" extension are unlocked. If the --suffix option is specified, that extension is used instead of ".locked".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `--verbose`   | `-v`  | str    | No       | `0`      | Increase the level of verbosity. A single -v generates a summary report. Two or more -v options show all of the files being processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--version`   | `-V`  | str    | No       |           | Show program's version number and exit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--wll`       | `-w`  | int     | No       | `72`      | The width of each locked/encrypted line. This is important because text files with very, very long can sometimes cause problems during uploads. If set to zero, no new lines are inserted. Default: `72`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `--warn`      | `-W`  | bool    | No       |           | Warn if a single file lock/unlock fails. Normally if the program tries to modify a fail and that modification fails, an error is reported and the programs stops. This option causes that event to be treated as a warning so the program continues.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `FILES`       |       | str     | No       |           | files to process                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## cURL Options Passthrough

None specified.

## Environment Variables

| Name          | Default | Description                                   |
|---------------|---------|-----------------------------------------------|
| `NUM_THREADS` | `None`  | Controls runtime behavior |

## Examples

1.  **Encrypt multiple files using a password file:**

    ```bash
    lock_files.py -p password-file file1.txt file2.txt dir1 dir2
    ```

2.  **Decrypt a file using a password provided directly:**

    ```bash
    lock_files.py -P secret --unlock file1.txt.locked
    ```

3.  **Encrypt a file in OpenSSL compatible mode:**

    ```bash
    lock_files.py -P secret --lock file1.txt
    ```

## Input/Output

| Input           | Output                  |
|-----------------|-------------------------|
| File(s)         | Encrypted/Decrypted File(s) |
| Directory(ies) | Encrypted/Decrypted Files in Directory(ies) |

## Testing

To run the tests, use pytest:

```bash
pytest
```

## Troubleshooting

1.  **Permission denied errors:** Ensure the script has write permissions to the files being processed. Use the `--warn` flag to continue processing other files if a file cannot be written to.
2.  **Incorrect password:** Double-check the password or password file.  If using a password file, ensure it contains only the password on the first line and no leading/trailing whitespace.

## Contributing

Coming soon

## License

Coming soon
