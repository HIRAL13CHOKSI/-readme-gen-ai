# File Organizer

## Overview
The File Organizer is a Python script designed to help users manage their files by sorting them into subfolders based on file type and creation date. This utility simplifies the organization of files within a specified directory, making it easier to locate and manage them.

## Features
- Sorts files into subfolders based on their file extensions.
- Creates year-based subfolders for better organization.
- Handles file name conflicts by prompting the user to rename or skip files.
- Automatically creates destination directories if they do not exist.

## Installation
To use the File Organizer, ensure you have Python installed on your system. No additional libraries are required beyond the standard library.

1. Download the script `fileorganizer.py`.
2. Ensure you have a valid `extensiondict.py` file that maps file extensions to their respective folder names.

## Usage
Run the script from the command line, providing the source directory and destination directory as arguments.

```bash
python fileorganizer.py <source_directory> <destination_directory>
```

### Example Command
```bash
python fileorganizer.py "C:/Users/YourUsername/Downloads" "C:/Users/YourUsername/Documents/OrganizedFiles"
```

## Examples
1. **Organizing Downloads**: If you have files in your Downloads folder and want to organize them into a Documents folder, you would run:
   ```bash
   python fileorganizer.py "C:/Users/YourUsername/Downloads" "C:/Users/YourUsername/Documents/OrganizedFiles"
   ```

2. **Handling Conflicts**: If a file with the same name already exists in the destination folder, the script will prompt you to either rename the file or leave it in the source directory.

## Limitations or Notes
- The script requires a valid `extensiondict.py` file that defines how file extensions are categorized. Without this, the script will not function correctly.
- Ensure that the source and destination paths are correctly formatted and accessible.
- The script currently uses Windows command syntax for moving files. Adjustments may be needed for compatibility with other operating systems.
- The script does not handle all possible exceptions comprehensively; ensure to monitor for any unexpected behavior during execution.
