# lock_files.py README

## Overview
`lock_files.py` is a Python utility for encrypting and decrypting files using AES encryption with a common password. It is designed to secure files before uploading them to cloud storage services like Dropbox or Google Drive. Users can specify passwords directly, use a password file, or enter passwords interactively.

## Features
- Encrypt and decrypt files with AES encryption.
- Support for password management via command line or password files.
- Ability to lock multiple files and directories at once.
- Option to specify custom file extensions for locked files.
- In-place encryption/decryption mode.
- Compatibility with OpenSSL for cross-tool encryption/decryption.
- Multi-threading support for processing multiple files concurrently.

## Installation
To use `lock_files.py`, ensure you have Python installed along with the `cryptography` library. You can install the required library using pip:

```bash
pip install cryptography
```

## Usage
The basic command structure for using `lock_files.py` is as follows:

```bash
lock_files.py [OPTIONS] [<FILES_OR_DIRS>]+
```

### Example Commands
1. **Encrypt files:**
   ```bash
   lock_files.py file1.txt file2.txt dir1 dir2
   Password: secret
   Re-enter password: secret
   ```

2. **Decrypt files:**
   ```bash
   lock_files.py --unlock file1.txt.locked
   ```

3. **Using a password file:**
   ```bash
   echo 'secret' > password-file
   chmod 0600 password-file
   lock_files.py -p password-file file1.txt
   lock_files.py -p password-file --unlock file1.txt.locked
   ```

4. **In-place encryption:**
   ```bash
   lock_files.py -P 'secret' -i -l file.txt
   ```

5. **OpenSSL compatibility:**
   ```bash
   lock_files.py -P 'secret' -c --lock file1.txt
   ```

## Examples
- **Locking multiple directories:**
   ```bash
   lock_files.py -P 'secret' project1 project2
   ```

- **Using a custom extension for locked files:**
   ```bash
   lock_files.py -P 'secret' -s .EncRypt file.txt
   ```

- **Unlocking files with a custom extension:**
   ```bash
   lock_files.py -P 'secret' -s .EncRypt --unlock file.txt.EncRypt
   ```

## Limitations or Notes
- **In-Place Mode:** Using the `--inplace` option can be risky as it overwrites files directly. Ensure you have backups to prevent data loss.
- **Password Security:** Specifying passwords directly in the command line with `-P` can expose them in command history. Use password files for better security.
- **Thread Management:** The utility supports multi-threading for processing files, but be cautious with system resources when processing large files or many files simultaneously.
- **OpenSSL Compatibility:** To ensure compatibility with OpenSSL, use the `-c` option during both encryption and decryption.

For further details and options, refer to the help command:
```bash
lock_files.py -h
```

## License
This project is licensed under the MIT License. For more information, visit the [GitHub repository](https://github.com/jlinoff/lock_files).
