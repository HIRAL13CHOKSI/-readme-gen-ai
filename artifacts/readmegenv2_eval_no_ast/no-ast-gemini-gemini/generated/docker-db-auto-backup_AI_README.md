This README describes `docker-db-auto-backup.py`, which is a test suite for a Docker database auto-backup utility, not the utility itself. Information about the backup utility's features and usage is inferred directly from these tests.

---

# docker-db-auto-backup.py

## Overview

This script is a `pytest` test suite designed to verify the functionality of a separate `db-auto-backup.py` utility. It rigorously tests various aspects of a Docker database backup solution, including its ability to back up different database types, handle compression, and integrate with notification services.

**Note:** This script is a test file. It does not perform database backups directly. It requires the actual `db-auto-backup.py` utility to be present in the same directory to execute successfully.

## Features (of the *tested utility*)

Based on the test cases, the `db-auto-backup.py` utility is designed to offer the following capabilities:

*   **Multi-Database Support**: Capable of backing up various Dockerized database containers, specifically tested for MariaDB, MySQL, PostgreSQL, and Redis.
*   **Backup Destination**: Creates backups in a `backups` subdirectory within the current working directory.
*   **Secure Permissions**: Ensures backup files are created with restricted file permissions (`0o600`).
*   **Compression Options**: Supports multiple compression algorithms for backups, including Gzip (`.gz`), LZMA/XZ (`.xz`), and Bzip2 (`.bz2`), in addition to plain (uncompressed) backups. The `COMPRESSION` environment variable configures this.
*   **Success Notification Hooks**: Integrates with external services to send success notifications after backups. This is configured via environment variables:
    *   `SUCCESS_HOOK_URL`: A generic URL for post-backup notifications.
    *   `HEALTHCHECKS_ID` (with optional `HEALTHCHECKS_HOST`): For Healthchecks.io integration.
    *   `UPTIME_KUMA_URL`: For Uptime Kuma integration.
*   **Intelligent Container Detection**: Identifies database types by analyzing Docker container names and image tags (e.g., `postgres`, `mysql`, `mariadb`, `redis`).

## Installation

To run *these tests*, you need:

1.  **Python 3.x**: Ensure you have a compatible Python version installed.
2.  **`pytest`**: Install the `pytest` testing framework:
    ```bash
    pip install pytest
    ```
3.  **`db-auto-backup.py` utility**: The actual backup utility must be present in the same directory as this test script. The source code for `db-auto-backup.py` was not provided with this script.

## Usage

This script is a test suite and is executed using `pytest`.

To run all tests:

1.  Navigate to the directory containing both `docker-db-auto-backup.py` and `db-auto-backup.py`.
2.  Execute `pytest` with the script's path:
    ```bash
    pytest docker-db-auto-backup.py
    ```

A successful run will indicate that the `db-auto-backup.py` utility passes all defined tests.

## Examples

The tests demonstrate how the *backup utility* (`db-auto-backup.py`) would be configured and behave.

**1. Running backups with Gzip compression:**

The `test_backup_runs_compressed` test suggests the utility processes a `COMPRESSION` environment variable.

```bash
# Example of how the backup utility (not this test script) would be run
COMPRESSION=gzip python db-auto-backup.py
```

This would create backup files like `your-container-name.sql.gz`.

**2. Sending success notifications to Healthchecks.io:**

The `test_healthchecks_success_hook_url` test shows integration via `HEALTHCHECKS_ID`.

```bash
# Example of how the backup utility (not this test script) would be run
HEALTHCHECKS_ID=your-unique-healthchecks-id python db-auto-backup.py
```

**3. Sending success notifications to Uptime Kuma:**

The `test_uptime_kuma_success_hook_url` test shows integration via `UPTIME_KUMA_URL`.

```bash
# Example of how the backup utility (not this test script) would be run
UPTIME_KUMA_URL=https://your-uptime-kuma-instance/api/push/your-ping-key python db-auto-backup.py
```

## Limitations or Notes

*   **Test Suite Only**: This `docker-db-auto-backup.py` script is a test suite and *does not perform any database backups itself*. Its sole purpose is to test another utility.
*   **Missing Utility**: The core `db-auto-backup.py` utility, which this script tests, was not provided. Without it, these tests cannot be run successfully, as indicated by the `FileNotFoundError` in the `--help` output.
*   **Inferred Functionality**: All features and usage patterns described above are inferred from the structure and assertions within the test cases.
