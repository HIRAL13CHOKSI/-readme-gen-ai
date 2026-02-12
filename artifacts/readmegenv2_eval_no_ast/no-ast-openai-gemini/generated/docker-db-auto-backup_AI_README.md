# Docker Database Auto Backup

## Overview
The `docker-db-auto-backup.py` script is a Python utility designed to automate the backup of Docker database containers. It verifies the successful execution of backup operations and checks the integrity of the backup files generated.

## Features
- Imports and executes a backup module from a specified file.
- Normalizes container names for consistent backup file naming.
- Validates that backups are created successfully and checks their file sizes and permissions.
- Supports various compression algorithms for backup files.
- Allows configuration of success notification URLs through environment variables.

## Installation
To use this script, ensure you have Python installed on your machine. You will also need to have the `pytest` library for running tests. You can install it using pip:

```bash
pip install pytest
```

## Usage
To run the backup script, execute the following command in your terminal:

```bash
python docker-db-auto-backup.py
```

Make sure that the `db-auto-backup.py` file is present in the same directory as this script, as it is required for the backup process.

## Examples
1. **Run the Backup:**
   ```bash
   python docker-db-auto-backup.py
   ```

2. **Set Environment Variables for Notifications:**
   Before running the script, you can set environment variables for success notifications:
   ```bash
   export SUCCESS_HOOK_URL="https://example.com"
   export HEALTHCHECKS_ID="1234"
   ```

## Limitations or Notes
- The script relies on the presence of `db-auto-backup.py` in the current working directory. Ensure that this file is available to avoid `FileNotFoundError`.
- The backup files are stored in a directory named `backups` created in the current working directory.
- The script checks for specific backup file names and sizes, which may need to be adjusted based on your database configuration and requirements.
- The script is designed for use with Docker containers running popular database systems like MySQL, MariaDB, PostgreSQL, and Redis. Ensure that your container names match the expected formats for successful backups.
