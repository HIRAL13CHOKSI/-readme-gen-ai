# `lock_files.py`
Encrypt and decrypt files using AES encryption and a common password.

[![PyPI](https://img.shields.io/pypi/v/your-package-name.svg)](https://pypi.org/project/your-package-name/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/your-org/your-repo/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/your-repo/actions/workflows/ci.yml)

## Overview

`lock_files.py` is a robust command-line tool designed for securely encrypting and decrypting files using AES encryption. It allows users to protect sensitive data before uploading it to cloud storage services like Dropbox or Google Drive.

Key Features:
*   **AES Encryption**: Utilizes AES for strong, industry-standard data protection.
*   **Flexible Password Handling**: Obtain passwords via command-line arguments, a secure password file, or interactive prompts.
*   **OpenSSL Compatibility**: Encrypt files that can be decrypted by OpenSSL, and vice-versa, using compatibility mode.
*   **In-Place Operations**: Modify files directly, with options for careful handling of existing data.
*   **Concurrency**: Leverage multiple threads to process a large number of files efficiently.
*   **Recursive Directory Processing**: Easily encrypt or decrypt entire directory trees.

## Requirements

*   **Python**: Version 3.8 or higher.
*   **Operating System**: Cross-platform (Linux, macOS, Windows).

## Dependencies

### Python Packages

This tool relies on the following third-party Python packages:

*   `cryptography`: For robust encryption primitives.
*   `Queue`: (Note: This may refer to a Python 2 backport or a distinct third-party package; for modern Python 3, `queue` is part of the standard library.)
*   `google-generativeai`: (Note: This dependency appears unrelated to the core encryption function of `lock_files.py` and may be a project-level dependency.)
*   `groq`: (Note: This dependency appears unrelated to the core encryption function of `lock_files.py` and may be a project-level dependency.)
*   `openai`: (Note: This dependency appears unrelated to the core encryption function of `lock_files.py` and may be a project-level dependency.)

Standard library modules used: `argparse`, `base64`, `getpass`, `inspect`, `multiprocessing`, `os`, `queue`, `subprocess`, `sys`, `threading`.

### External Tools

*   `getconf`: Used on Linux and Mac for determining the number of available CPU cores.

## Installation

To install the required dependencies, use `pip`. Assuming you have a `requirements.txt` file in the parent directory of `lock_files.py`:

```bash
pip install -r ../requirements.txt
```

If you are running `lock_files.py` from your current directory, ensure the script is executable:

```bash
chmod +x lock_files.py
```

## Usage

Run the script directly from your command line.

Encrypt `file1.txt` and `file2.txt` prompting for a password:

```bash
python lock_files.py file1.txt file2.txt
```

Unlock `file1.txt.locked` using a password file:

```bash
python lock_files.py -p password-file --unlock file1.txt.locked
```

Example of all available flags (replace `<value>` placeholders with actual values):

```bash
python lock_files.py --openssl --decrypt --encrypt --inplace --jobs <value> --lock --overwrite --password-file <value> --password <value> --recurse --suffix <value> --unlock --verbose <value> --version <value> --wll <value> --warn FILES <value1> <value2> ...
```

## Flags

The following command-line flags are available:

| Flag            | Alias | Type | Required | Default     | Help                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :-------------- | :---- | :--- | :------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--openssl`     | `-c`  | bool | False    |             |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--decrypt`     | `-d`  | bool | False    |             | Unlock/decrypt files. This option is deprecated. It is the same as `--unlock`.                                                                                                                                                                                                                                                                                                                                                   |
| `--encrypt`     | `-e`  | bool | False    |             | Lock/encrypt files. This option is deprecated. This is the same as `--lock` and is the default.                                                                                                                                                                                                                                                                                                                                  |
| `--inplace`     | `-i`  | bool | False    |             | In place mode. Overwrite files in place. It is the same as specifying: `-o -s ''`. This is dangerous because a disk full operation can cause data to be lost when a write fails. This allows you to duplicate the behavior of the previous version.                                                                                                                                                                                |
| `--jobs`        | `-j`  | int  | False    | 1           | Specify the maximum number of active threads. This can be helpful if there a lot of large files to process where large refers to files larger than a MB.                                                                                                                                                                                                                                                                            |
| `--lock`        | `-l`  | bool | False    |             | Lock files. Files are locked and the `.locked` extension is appended unless the `--suffix` option is specified.                                                                                                                                                                                                                                                                                                                    |
| `--overwrite`   | `-o`  | bool | False    |             | Overwrite files that already exist. This can be used in conjunction disable file existence checks. It is used by the `--inplace` mode.                                                                                                                                                                                                                                                                                             |
| `--password-file` | `-p`  | str  | False    |             | file that contains the password. The default behavior is to prompt for the password.                                                                                                                                                                                                                                                                                                                                           |
| `--password`    | `-P`  | str  | False    |             | Specify the password on the command line. This is not secure because it is visible in the command history.                                                                                                                                                                                                                                                                                                                       |
| `--recurse`     | `-r`  | bool | False    |             | Recurse into subdirectories.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--suffix`      | `-s`  | str  | False    | `.locked`   | Specify the extension used for locked files.                                                                                                                                                                                                                                                                                                                                                                                     |
| `--unlock`      | `-u`  | bool | False    |             | Unlock files. Files with the `.locked` extension are unlocked. If the `--suffix` option is specified, that extension is used instead of `.locked`.                                                                                                                                                                                                                                                                               |
| `--verbose`     | `-v`  | str  | False    | 0           | Increase the level of verbosity. A single `-v` generates a summary report. Two or more `-v` options show all of the files being processed.                                                                                                                                                                                                                                                                                       |
| `--version`     | `-V`  | str  | False    |             | Show program's version number and exit.                                                                                                                                                                                                                                                                                                                                                                                          |
| `--wll`         | `-w`  | int  | False    | 72          | The width of each locked/encrypted line. This is important because text files with very, very long can sometimes cause problems during uploads. If set to zero, no new lines are inserted.                                                                                                                                                                                                                                    |
| `--warn`        | `-W`  | bool | False    |             | Warn if a single file lock/unlock fails. Normally if the program tries to modify a fail and that modification fails, an error is reported and the programs stops. This option causes that event to be treated as a warning so the program continues.                                                                                                                                                                               |
| `FILES`         |      | str  | False    |             | files to process                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Environment Variables

| Name        | Default | Description                                 |
| :---------- | :------ | :------------------------------------------ |
| `NUM_THREADS` | `null`  | Controls the maximum number of active threads. |

## Examples

### 1. Basic File Encryption and Decryption

Encrypt `file1.txt` and `file2.txt`, and recursively process `dir1` and `dir2`. You will be prompted for the password.

```bash
python lock_files.py file1.txt file2.txt dir1 dir2
# Password: secret
# Re-enter password: secret
```

To unlock the encrypted files:

```bash
python lock_files.py --unlock file1.txt.locked file2.txt.locked dir1 dir2
# Password: secret
# Re-enter password: secret
```

### 2. Using a Password File

First, create a secure password file with restricted permissions:

```bash
cat > password-file <<EOF
thisismysecretpassword
EOF
chmod 0600 password-file
```

Now, use the password file to lock and unlock `data.txt`:

```bash
python lock_files.py -p password-file data.txt
# (data.txt will become data.txt.locked)

python lock_files.py -p password-file --unlock data.txt.locked
# (data.txt.locked will become data.txt)
```

### 3. OpenSSL Compatibility Mode

Encrypt a file using `lock_files.py` and then decrypt it using `openssl`:

```bash
python lock_files.py -P secret --lock file1.txt
# ls file1*
# file1.txt.locked

openssl enc -aes-256-cbc -d -a -salt -pass pass:secret -in file1.txt.locked -out file1.txt
```

Encrypt a file using `openssl` and then decrypt it using `lock_files.py`:

```bash
openssl enc -aes-256-cbc -e -a -salt -pass pass:secret -in file1.txt -out file1.txt.locked
# ls file1*
# file1.txt      file1.txt.locked

python lock_files.py -c -W -P secret --unlock file1.txt.locked
# ls file1*
# file1.txt
```
*Note the use of the `-W` (or `--warn`) option when decrypting with `lock_files.py` after OpenSSL encryption, as `file1.txt` might already exist, which would normally cause an error.*

## Input/Output

| Category | Description                                         |
| :------- | :-------------------------------------------------- |
| **Input**  | Files and directories paths; password (via prompt, file, or CLI). |
| **Output** | Encrypted files with `.locked` (or custom) suffix; decrypted files with suffix removed; optional verbose output. |

## Testing

This project includes tests to ensure its functionality and reliability. You can run them using `pytest` (ensure it's installed via `pip install pytest`).

```bash
pytest
```

## Troubleshooting

*   **"Permission denied" errors**: Ensure the script has read and write permissions for the files and directories it's trying to process. Use `chmod` to adjust permissions if necessary.
*   **Incorrect Password**: If decryption fails, double-check the password. Passwords are case-sensitive. If using a password file, ensure it contains the correct password on its first non-empty, non-commented line.
*   **File Loss with `--inplace`**: The `--inplace` flag overwrites original files. If an operation is interrupted (e.g., disk full), data loss can occur. Always back up critical files before using `--inplace`.
*   **`cryptography` import errors**: If you encounter errors related to `cryptography` not being found, ensure all dependencies are correctly installed using `pip install -r ../requirements.txt`.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests. Coming soon.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details. Coming soon.
