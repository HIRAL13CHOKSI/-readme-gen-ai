```markdown
# Lock Files
Encrypt and decrypt files using AES encryption with a common password.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue)

## Overview
Lock Files is a command-line tool that allows users to encrypt and decrypt files using AES encryption. It is particularly useful for securing files before uploading them to storage services like Dropbox or Google Drive. Notable features include:

- Support for password management via command line or password files.
- Options for in-place encryption and compatibility with OpenSSL.
- Multi-threaded processing for handling large files efficiently.

## Requirements
- **Python Version**: 3.x
- **Operating System**: Cross-platform (Linux, macOS, Windows)

## Dependencies
### Standard Library Modules
- `argparse`
- `base64`
- `getpass`
- `inspect`
- `multiprocessing`
- `os`
- `queue`
- `subprocess`
- `sys`
- `threading`

### Third-Party Packages
- `Queue`
- `cryptography`
- `google-generativeai`
- `groq`
- `openai`

### External Tools
- `getconf`

## Installation
To install the required dependencies, use the following command:

```bash
pip install -r ../requirements.txt
```

For an editable install, run:

```bash
pip install -e .
```

## Usage
To run the tool, use the following command:

```bash
python lock_files.py FILES <value1> <value2> ...
```

### Example Commands
1. Encrypt files:
   ```bash
   lock_files.py file1.txt file2.txt dir1 dir2
   Password: secret
   Re-enter password: secret
   ```

2. Unlock a file using a password file:
   ```bash
   lock_files.py -p password-file --unlock file1.txt.locked
   ```

## Flags
| Flag                   | Alias | Type   | Required | Default | Help                                                                                          |
|------------------------|-------|--------|----------|---------|-----------------------------------------------------------------------------------------------|
| --openssl              | -c    | bool   | No       |         |                                                                                               |
| --decrypt              | -d    | bool   | No       |         | Unlock/decrypt files. This option is deprecated. It is the same as --unlock.                 |
| --encrypt              | -e    | bool   | No       |         | Lock/encrypt files. This option is deprecated. This is the same as --lock and is the default. |
| --inplace              | -i    | bool   | No       |         | Overwrite files in place.                                                                      |
| --jobs                 | -j    | int    | No       | 1       | Specify the maximum number of active threads.                                                  |
| --lock                 | -l    | bool   | No       |         | Lock files.                                                                                   |
| --overwrite            | -o    | bool   | No       |         | Overwrite files that already exist.                                                            |
| --password-file        | -p    | str    | No       |         | File that contains the password.                                                               |
| --password             | -P    | str    | No       |         | Specify the password on the command line.                                                     |
| --recurse              | -r    | bool   | No       |         | Recurse into subdirectories.                                                                   |
| --suffix               | -s    | str    | No       | .locked | Specify the extension used for locked files.                                                  |
| --unlock               | -u    | bool   | No       |         | Unlock files.                                                                                 |
| --verbose              | -v    | str    | No       | 0       | Increase the level of verbosity.                                                               |
| --version              | -V    | str    | No       |         | Show program's version number and exit.                                                       |
| --wll                  | -w    | int    | No       | 72      | The width of each locked/encrypted line.                                                      |
| --warn                 | -W    | bool   | No       |         | Warn if a single file lock/unlock fails.                                                      |
| FILES                  |       | str    | No       |         | Files to process.                                                                              |

## Environment Variables
| Name         | Default | Description                     |
|--------------|---------|---------------------------------|
| NUM_THREADS  | None    | Controls runtime behavior       |

## Examples
1. Encrypt multiple files:
   ```bash
   lock_files.py file1.txt file2.txt dir1 dir2
   ```

2. Decrypt a file using a password:
   ```bash
   lock_files.py -p ./password --unlock file1.txt.locked
   ```

## Input/Output
| Input                     | Output                        |
|---------------------------|-------------------------------|
| Files to be processed     | Encrypted files with .locked extension |

## Testing
To run tests, use the following command:

```bash
pytest
```

## Troubleshooting
- **Issue**: Files not being encrypted.
  - **Solution**: Ensure you have write permissions for the files.
  
- **Issue**: Password file not found.
  - **Solution**: Verify the path to the password file is correct.

## Contributing
Coming soon.

## License
Coming soon.
```
