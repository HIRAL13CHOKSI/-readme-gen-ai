# `fileorganizer.py`

Organize your files effortlessly by type and creation date.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://example.com/build-status)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://example.com/license)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## Overview

`fileorganizer.py` is a powerful and intuitive script designed to help you declutter your digital workspace. This tool allows you to scan any specified folder and automatically move files into structured subfolders based on their file type (extension) and creation date. By intelligently sorting your documents, images, videos, and more, `fileorganizer.py` ensures your directories remain clean and easy to navigate.

**Notable Features:**

*   **Type-Based Sorting:** Automatically groups files by their extensions into designated subfolders.
*   **Date-Based Organization:** Further refines organization by creating subfolders based on file creation date.
*   **Simple CLI Interface:** Easily specify source and destination directories for quick organization.

## Requirements

*   **Python:** Version 3.8 or newer.
*   **Operating System:** Cross-platform (tested on Windows, macOS, Linux).

## Dependencies

### Standard Library Modules

*   `datetime`
*   `os`
*   `sys`

### Third-Party Packages

*   `extensiondict`
*   `google-generativeai`
*   `groq`
*   `openai`

### External Tools

None specified.

## Installation

To get started with `fileorganizer.py`, clone the repository and install the necessary dependencies using `pip`.

```bash
# Clone the repository
git clone https://github.com/your-org/your-repo.git
cd your-repo

# Install dependencies from the requirements file
pip install -r ../requirements.txt

# For local development (if fileorganizer.py is part of a larger package)
# If this is a standalone script, this step might not be necessary.
# pip install -e .
```

## Usage

Run the script from your terminal, providing the source and destination directories as positional arguments.

```bash
python fileorganizer.py <source_directory> <destination_directory>
```

Replace `<source_directory>` with the path to the folder you want to organize, and `<destination_directory>` with the path where you want the organized files to be moved.

## Flags

None. This script currently relies on positional arguments.

## Environment Variables

None specified.

## Examples

### Example 1: Organizing a Downloads Folder

Organize files from your `~/Downloads` folder into a new `~/OrganizedFiles` directory. The script will create subfolders like `~/OrganizedFiles/Documents`, `~/OrganizedFiles/Images`, etc., and further organize within those by creation date.

```bash
python fileorganizer.py ~/Downloads ~/OrganizedFiles
```

### Example 2: Cleaning up a Project Workspace

Clean up a temporary workspace folder named `~/MyProject/temp` and move files to `~/MyProject/Archive`.

```bash
python fileorganizer.py ~/MyProject/temp ~/MyProject/Archive
```

## Input/Output

| Type    | Description                                                     |
| :------ | :-------------------------------------------------------------- |
| **Input** | Source directory path (`src_base`), Destination directory path (`dst_base`) |
| **Output** | Files moved from `src_base` to `dst_base` within type-specific and date-specific subfolders. |

## Testing

This project includes tests to ensure reliability. You can run them using `pytest` (recommended).

```bash
# Ensure pytest is installed
pip install pytest

# Run tests
pytest
```

## Troubleshooting

1.  **"FileNotFoundError" or "Permission Denied"**:
    *   **Issue**: The script cannot access the specified source or destination directories.
    *   **Solution**: Double-check that the paths you provided are correct and that you have read/write permissions for both directories. On Linux/macOS, you might need to use `sudo` for system-level directories, though this is generally discouraged for user files.
2.  **Files not moving as expected**:
    *   **Issue**: Files are not appearing in the destination directory or are not sorted correctly.
    *   **Solution**: Verify that `extensiondict` (a key dependency for file type recognition) is correctly installed. Ensure there are actual files in the source directory. Check the script's output for any error messages that might indicate a problem during the move operation.
3.  **Missing `requirements.txt`**:
    *   **Issue**: The `requirements.txt` file is expected at `../requirements.txt` but might be missing or misplaced.
    *   **Solution**: Ensure you have navigated to the `your-repo` directory and that the `requirements.txt` file exists one level up, or adjust the `pip install -r` command to the correct path.

## Contributing

Contributions are welcome! Please refer to the project's contribution guidelines (if available) for details on how to submit pull requests, report bugs, and suggest features.

## License

This project is distributed under the MIT License. See the `LICENSE` file for more details.
