```markdown
# Lock Files
Encrypt and decrypt files using AES encryption with a common password.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue)

## Overview
Lock Files is a command-line tool that allows users to encrypt and decrypt files using AES encryption. It is particularly useful for securing files before uploading them to storage services like Dropbox or Google Drive. The tool supports both manual password entry and password retrieval from a specified file, enhancing usability and security.

### Notable Features
- AES encryption for secure file locking.
- Support for batch processing of files and directories.
- Options for in-place modifications and compatibility with OpenSSL.
- Verbose output for detailed processing information.

## Requirements
- **Python Version**: 3.6 or higher
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
To install the required dependencies, use the provided requirements file:

```bash
pip install -r ../requirements.txt
```

For an editable install, you can run:

```bash
pip install -e .
```

## Usage
To run the script, use the following command:

```bash
python lock_files.py FILES <file1> <file2> ...
```

For example, to encrypt files:

```bash
$ lock_files.py file1.txt file2.txt dir1 dir2
Password: secret
Re-enter password: secret
```

## Flags
| Flag                | Alias | Type   | Required | Default | Help                                                                                      |
|---------------------|-------|--------|----------|---------|-------------------------------------------------------------------------------------------|
| --openssl           | -c    | bool   | No       |         |                                                                                           |
| --decrypt           | -d    | bool   | No       |         | Unlock/decrypt files. This option is deprecated. It is the same as --unlock.             |
| --encrypt           | -e    | bool   | No       |         | Lock/encrypt files. This option is deprecated. This is the same as --lock and is default.|
| --inplace           | -i    | bool   | No       |         | Overwrite files in place.                                                                 |
| --jobs              | -j    | int    | No       | 1       | Specify the maximum number of active threads.                                             |
| --lock              | -l    | bool   | No       |         | Lock files.                                                                                |
| --overwrite         | -o    | bool   | No       |         | Overwrite files that already exist.                                                       |
| --password-file     | -p    | str    | No       |         | File that contains the password.                                                           |
| --password          | -P    | str    | No       |         | Specify the password on the command line.                                                 |
| --recurse           | -r    | bool   | No       |         | Recurse into subdirectories.                                                               |
| --suffix            | -s    | str    | No       | .locked | Specify the extension used for locked files.                                              |
| --unlock            | -u    | bool   | No       |         | Unlock files.                                                                              |
| --verbose           | -v    | str    | No       | 0       | Increase the level of verbosity.                                                           |
| --version           | -V    | str    | No       |         | Show program's version number and exit.                                                  |
| --wll               | -w    | int    | No       | 72      | The width of each locked/encrypted line.                                                  |
| --warn              | -W    | bool   | No       |         | Warn if a single file lock/unlock fails.                                                  |
| FILES               |       | str    | No       |         | Files to process.                                                                         |

## Environment Variables
| Name          | Default | Description                  |
|---------------|---------|------------------------------|
| NUM_THREADS   | None    | Controls runtime behavior     |

## Examples
Encrypt files using a password file:

```bash
$ cat >password-file
thisismysecretpassword
EOF
$ chmod 0600 password-file
$ lock_files.py -p password-file file1.txt
```

Decrypt files:

```bash
$ lock_files.py -p password-file --unlock file1.txt.locked
```

## Input/Output
| Input                     | Output                       |
|---------------------------|------------------------------|
| Files to be encrypted     | Encrypted files with .locked extension |
| Encrypted files           | Decrypted files              |

## Testing
To run tests, use:

```bash
pytest
```

## Troubleshooting
- **Issue**: Files not writable.
  - **Solution**: Ensure you have write permissions for the files.
  
- **Issue**: Incorrect password.
  - **Solution**: Verify the password or use a password file.

## Contributing
Coming soon.

## License
Coming soon.
```
