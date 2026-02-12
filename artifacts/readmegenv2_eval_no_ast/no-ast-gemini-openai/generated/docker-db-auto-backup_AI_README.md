```markdown
# Docker Database Auto Backup

## Overview

This utility automatically backs up databases in Docker containers. It identifies supported database containers (MariaDB, MySQL, PostgreSQL, Redis) and creates backups of their data. It can also compress the backups using gzip, lzma, xz, or bz2 algorithms. The script also supports sending success notifications via webhooks.

## Features

- Automatically detects and backs up MariaDB, MySQL, PostgreSQL, and Redis databases running in Docker containers.
- Supports compression of backups using gzip, lzma, xz, or bz2.
- Sends success notifications via webhooks to custom URLs, Healthchecks.io, or Uptime Kuma.

## Installation

1.  Place `db-auto-backup.py` in a directory accessible by your Docker host.
2.  Ensure the script has execute permissions.

## Usage

The script should be executed within a Docker container or on the Docker host. Backups are stored in a `backups` directory relative to the script's execution path.

Basic usage example (assuming the script is named `db-auto-backup.py`):

```bash
python db-auto-backup.py
```

The backup directory is created in the same directory as the script.

### Environment Variables

The following environment variables can be used to configure the backup process:

-   `COMPRESSION`: Specifies the compression algorithm to use. Supported values: `gzip`, `lzma`, `xz`, `bz2`, or `plain` (for no compression). Default is no compression.
-   `SUCCESS_HOOK_URL`: A URL to send a POST request to upon successful backup.
-   `HEALTHCHECKS_ID`: Your Healthchecks.io ID.  If set, a ping is sent to Healthchecks.io upon successful backup.
-   `HEALTHCHECKS_HOST`: (Optional) Custom host for Healthchecks.io. Defaults to `hc-ping.com`.
-   `UPTIME_KUMA_URL`: A URL to your Uptime Kuma instance. If set, a GET request is sent to this URL upon successful backup.

### Example Commands

1.  Run the script with gzip compression:

    ```bash
    COMPRESSION=gzip python db-auto-backup.py
    ```

2.  Run the script and send a success notification to a custom webhook URL:

    ```bash
    SUCCESS_HOOK_URL="https://example.com/webhook" python db-auto-backup.py
    ```

3.  Run the script with Healthchecks.io integration:

    ```bash
    HEALTHCHECKS_ID="your_healthchecks_id" python db-auto-backup.py
    ```

4.  Run the script with Uptime Kuma integration:

    ```bash
    UPTIME_KUMA_URL="https://uptime-kuma.example.com/api/push/your_uptime_kuma_id?status=up" python db-auto-backup.py
    ```

## Examples

After running the script, a `backups` directory will be created containing the database backups. The filenames will follow the format `<container_name>-<database_type>-1.<extension>`, where `<container_name>` is the normalized container name (underscores replaced with hyphens), `<database_type>` is the database type (e.g., `mariadb`, `mysql`, `psql`, `redis`), and `<extension>` is the compression extension (e.g., `.gz`, `.xz`, `.bz2`).

## Limitations or Notes

-   The script relies on the `db-auto-backup.py` file being present in the same directory as the script used to generate this readme.
-   The script currently supports only MariaDB, MySQL, PostgreSQL, and Redis databases.
-   The script assumes that the necessary database client tools (e.g., `mysqldump`, `pg_dump`, `redis-cli`) are available within the Docker containers being backed up.
-   The script creates backups with file permissions `600`, meaning only the owner (user running the script) has read/write access.
```
