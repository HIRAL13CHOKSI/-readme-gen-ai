# lock_files.py

## Overview
`lock_files.py` is a Python script designed to encrypt and decrypt files using AES encryption with a common password. It is particularly useful for securing files before uploading them to cloud storage services like Dropbox or Google Drive. The script allows users to specify passwords directly, read them from a file, or enter them interactively.

## Features
- **Encryption and Decryption**: Secure files by encrypting them with a password and decrypt them when needed.
- **Password Management**: Use a password file for convenience or enter passwords manually.
- **Batch Processing**: Encrypt or decrypt multiple files and directories at once.
- **OpenSSL Compatibility**: Encrypt and decrypt files in a manner compatible with OpenSSL.
- **In-Place Modification**: Option to overwrite files in place.
- **Threading Support**: Process multiple files concurrently for improved performance.
- **Custom File Extensions**: Specify custom extensions for locked files.

## Installation
To run `lock_files.py`, ensure you have Python installed along with the `cryptography` library. You can install the required library using pip:

```bash
pip install cryptography
```

## Usage
Run the script from the command line with the following syntax:

```bash
python lock_files.py [OPTIONS] [<FILES_OR_DIRS>]+
```

### Example Commands
1. **Encrypt files**:
   ```bash
   python lock_files.py file1.txt file2.txt
   Password: secret
   Re-enter password: secret
   ```

2. **Decrypt files**:
   ```bash
   python lock_files.py --unlock file1.txt.locked
   Password: secret
   ```

3. **Using a password file**:
   ```bash
   echo 'secret' > password-file
   chmod 0600 password-file
   python lock_files.py -p password-file file1.txt
   python lock_files.py -p password-file --unlock file1.txt.locked
   ```

4. **OpenSSL compatibility**:
   ```bash
   python lock_files.py -c -P secret --lock file1.txt
   openssl enc -aes-256-cbc -d -a -salt -pass pass:secret -in file1.txt.locked -out file1.txt
   ```

## Examples
- **Locking multiple directories**:
   ```bash
   python lock_files.py -P 'secret' project1 project2
   ```

- **Using a custom suffix for locked files**:
   ```bash
   python lock_files.py -P 'secret' -s .EncRypt file.txt
   ```

- **Locking a file in place**:
   ```bash
   python lock_files.py -P 'secret' -i -l file.txt
   ```

## Limitations or Notes
- **Password Security**: Specifying passwords directly in the command line (using `-P`) is not secure as they may be visible in command history.
- **In-Place Mode**: Using the `--inplace` option can lead to data loss if the disk runs out of space during the write operation. It is recommended to use this option with caution.
- **Threading**: The script uses threading for performance, which may lead to complex behavior if not managed properly. Ensure that the environment can handle concurrent file operations.

For more details, refer to the help output by running:

```bash
python lock_files.py -h
``` 

## License
This script is licensed under the MIT Open Source License. For more information, visit the project repository at [GitHub](https://github.com/jlinoff/lock_files).
