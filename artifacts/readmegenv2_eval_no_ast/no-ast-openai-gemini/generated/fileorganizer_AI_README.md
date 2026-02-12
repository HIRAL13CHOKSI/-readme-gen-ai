# File Organizer

## Overview
File Organizer is a Python script designed to help users organize files within a specified directory by moving them into subfolders based on their file type and creation date. This utility simplifies file management, making it easier to keep your workspace tidy.

## Features
- Sorts files into subfolders based on their extensions.
- Creates year-based folders for better organization.
- Handles filename conflicts by allowing users to rename files.
- Automatically creates destination directories if they do not exist.

## Installation
To use the File Organizer script, ensure you have Python installed on your system. You will also need to create a module named `extensiondict.py` that contains a dictionary mapping file extensions to their respective folder names.

1. **Clone or download the script**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create the `extensiondict.py` module**:
   Define a dictionary in `extensiondict.py` that maps file extensions to folder names. For example:
   ```python
   extension_dict = {
       '.txt': 'TextFiles',
       '.jpg': 'Images',
       '.png': 'Images',
       '.pdf': 'Documents',
       # Add more mappings as needed
   }

   def getpath(extension):
       return extension_dict.get(extension, 'Other')
   ```

## Usage
To run the script, use the command line to specify the source directory (where the files are located) and the destination directory (where the organized files will be moved).

### Command
```bash
python fileorganizer.py <source_directory> <destination_directory>
```

### Example
```bash
python fileorganizer.py C:/Users/colel/Documents/Downloads C:/Users/colel/Documents/OrganizedFiles
```

## Examples
1. **Organizing Downloads**:
   If your downloads folder contains various file types, running the script will move `.jpg` files to `OrganizedFiles/Images`, `.txt` files to `OrganizedFiles/TextFiles`, and so on, creating year-based subfolders as needed.

2. **Handling Conflicts**:
   If a file with the same name already exists in the destination folder, the script will prompt you to either rename the file or leave it in the source directory.

## Limitations or Notes
- Ensure that the `extensiondict.py` module is correctly set up with the necessary mappings for file extensions.
- The script currently does not handle symbolic links or special file types beyond those defined in the `extensiondict`.
- The script uses the `os.system` command to move files, which may not be the most efficient method for large file operations. Consider using the `shutil` module for improved performance in future versions.
