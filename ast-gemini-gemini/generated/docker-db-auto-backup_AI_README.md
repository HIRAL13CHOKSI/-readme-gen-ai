# Docker DB Auto Backup
Automate database backups from Docker containers with health check integrations.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/your-org/your-repo/actions) <!-- Placeholder -->

## Overview
`docker-db-auto-backup.py` is a powerful script designed to automate the process of backing up databases running within Docker containers. It provides robust integration with various health monitoring services, allowing you to notify endpoints like Healthchecks.io or Uptime Kuma upon successful backup operations. The script's core functionality involves identifying container names, initiating backup procedures, and handling success notifications, ensuring your critical data is regularly secured and monitored.

## Requirements
*   **Python**: Version 3.8 or higher.
*   **Operating System**: Linux, macOS, or Windows (with Docker Desktop if interacting with Docker containers, implied by the script's name and functions).

## Dependencies
This project relies on a few external packages and standard Python modules:

### Python Standard Library
*   `importlib`: For dynamic module loading.
*   `pathlib`: For object-oriented filesystem paths.
*   `typing`: For type hints.
*   `unittest`: For basic unit testing utilities.

### Third-Party Packages
The following packages are typically installed via the `requirements.txt` file and are essential for the script's operation or testing:
*   `google-generativeai`: Likely for AI-driven functionalities or integrations.
*   `groq`: Another package, possibly related to AI or specific API interactions.
*   `openai`: For integrating with OpenAI's APIs.
*   `pytest`: A robust testing framework used for validating script functionality.

## Installation
To get started with `docker-db-auto-backup.py`, first ensure you have Python 3.8+ installed.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-org/your-repo.git # Replace with actual repo URL
    cd your-repo/<path-to-script-directory> # Navigate to the directory containing docker-db-auto-backup.py
    ```

2.  **Install dependencies**:
    From the directory containing `docker-db-auto-backup.py`, run the following command to install all necessary third-party packages:
    ```bash
    pip install -r ..\requirements.txt
    ```

    *Note*: If you encounter issues with the `..\requirements.txt` path, ensure you are running the command from the directory where `docker-db-auto-backup.py` resides, or adjust the path to `requirements.txt` relative to your current working directory.

## Usage
Execute the script directly using Python.
```bash
python docker-db-auto-backup.py
```

## Flags
None. This script is primarily configured via environment variables.

## Environment Variables
The script leverages environment variables for configuration, particularly for integrating with health monitoring services.

| Name                | Default       | Description                                                                                                                                              |
| :------------------ | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HEALTHCHECKS_HOST` | `hc-ping.com` | The host for the Healthchecks.io service. Customize if using a self-hosted instance.                                                                     |
| `HEALTHCHECKS_ID`   | None          | The unique UUID for your check on Healthchecks.io. Required to notify Healthchecks.io.                                                                   |
| `SUCCESS_HOOK_URL`  | None          | A generic URL to send a POST request to upon successful backup. Useful for custom notifications or webhooks.                                             |
| `UPTIME_KUMA_URL`   | None          | The full URL for an Uptime Kuma push monitor. The script will send a GET request to this URL upon successful backup.                                     |

## Examples

### 1. Basic Backup Execution
Run the script to perform a backup without any external health check integrations. The script will attempt to back up databases from detected Docker containers.

```bash
python docker-db-auto-backup.py
```

### 2. Integrating with Healthchecks.io
To notify Healthchecks.io upon a successful backup, set the `HEALTHCHECKS_ID` environment variable.

```bash
# On Linux/macOS
export HEALTHCHECKS_ID="YOUR_HEALTHCHECKS_UUID"
python docker-db-auto-backup.py

# On Windows (Command Prompt)
set HEALTHCHECKS_ID="YOUR_HEALTHCHECKS_UUID"
python docker-db-auto-backup.py

# On Windows (PowerShell)
$env:HEALTHCHECKS_ID="YOUR_HEALTHCHECKS_UUID"
python docker-db-auto-backup.py
```

### 3. Integrating with Uptime Kuma
To integrate with Uptime Kuma, set the `UPTIME_KUMA_URL` environment variable with your monitor's push URL.

```bash
# On Linux/macOS
export UPTIME_KUMA_URL="https://your-uptime-kuma.com/api/push/YOUR_API_KEY?status=up&msg=OK"
python docker-db-auto-backup.py
```

## Input/Output

| Type   | Description                                                                                             |
| :----- | :------------------------------------------------------------------------------------------------------ |
| **Input**  | Docker container configurations (implied by filename and functions), environment variables.         |
| **Output** | Database backup files (location determined by script logic), HTTP requests to health check services. |

## Testing
This project includes tests to ensure reliability and correct functionality. The tests are written using the `pytest` framework and cover various aspects of the backup process and integration with health checks.

To run the tests:
```bash
pytest
```
The test suite includes functions like `test_backup_runs`, `test_backup_runs_compressed`, `test_get_container_names`, and various tests for health check integrations (`test_healthchecks_success_hook_url`, `test_uptime_kuma_success_hook_url`).

## Troubleshooting

1.  **`requirements.txt` path error during installation**: If `pip install -r ..\requirements.txt` fails, double-check your current working directory. The `..` implies the `requirements.txt` file is in the parent directory of where `docker-db-auto-backup.py` is located. Adjust the path as needed or navigate to the correct directory.
2.  **Backup not running / no output**:
    *   Ensure Docker is running and your database containers are active.
    *   Check for any error messages in the script's output.
    *   Verify that the script has the necessary permissions to access Docker and write backup files.
3.  **Health check not firing**:
    *   Confirm that the `HEALTHCHECKS_ID` or `UPTIME_KUMA_URL` environment variables are correctly set and exported before running the script.
    *   Verify the URLs/IDs against your Healthchecks.io or Uptime Kuma dashboard.
    *   Check network connectivity from the machine running the script to the health check service.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
