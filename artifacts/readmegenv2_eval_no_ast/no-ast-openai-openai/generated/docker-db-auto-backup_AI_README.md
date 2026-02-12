# Docker Database Auto Backup

## Overview
The `docker-db-auto-backup.py` script is a Python utility designed to automate the backup of Docker database containers. It facilitates the creation of backups for various database types, ensuring that the backup files are stored securely and can be compressed if desired.

## Features
- Automatically backs up Docker database containers.
- Supports multiple database types including MySQL, MariaDB, PostgreSQL, and Redis.
- Allows for compression of backup files using various algorithms (gzip, lzma, bz2, etc.).
- Validates the integrity and permissions of backup files.
- Provides hooks for success notifications via web URLs.

## Installation
To use this script, ensure you have Python installed on your system. You will also need to have the `pytest` library for running tests. You can install it using pip:

```bash
pip install pytest
```

## Usage
1. Place the `docker-db-auto-backup.py` script in your desired directory.
2. Ensure that the `db-auto-backup.py` module is present in the same directory, as it is required for the script to function.
3. Run the script using Python:

```bash
python docker-db-auto-backup.py
```

## Examples
To run the backup with a specific compression algorithm, you can set the `COMPRESSION` environment variable before executing the script:

```bash
COMPRESSION=gzip python docker-db-auto-backup.py
```

You can also specify other environment variables for success hooks:

```bash
export SUCCESS_HOOK_URL="https://example.com"
export HEALTHCHECKS_ID="1234"
python docker-db-auto-backup.py
```

## Limitations or Notes
- The script requires the presence of the `db-auto-backup.py` module in the same directory to function correctly. Ensure that this file is available.
- The backup directory is set to `backups` in the current working directory. Ensure you have write permissions to this directory.
- The script is designed to work with Docker containers, so Docker must be installed and running on your machine.
- The script does not handle the creation of the backup directory; ensure it exists or modify the script to create it if necessary.
