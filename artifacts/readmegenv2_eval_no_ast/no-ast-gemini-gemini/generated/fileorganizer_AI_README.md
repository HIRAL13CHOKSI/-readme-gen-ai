# File Organizer

## Overview
This Python script is a utility designed to help organize files within a specified directory. It automates the process of moving files from a source folder to a destination folder, categorizing them into subfolders based on their file type (extension) and further by their creation year.

## Features
*   **Automatic Categorization**: Moves files into intelligently named subfolders based on their file extension (e.g., `.pdf` files go into a "PDFs" folder, `.jpg` files into an "Images" folder). The specific mapping is configurable.
*   **Year-Based Subfolders**: Further organizes files by creating sub-subfolders for each file's creation year within its file type category (e.g., `Images/2023`, `PDFs/2022`).
*   **Duplicate File Handling**: Detects if a file with the same name already exists in the target destination. If a clash occurs, it interactively prompts the user to either rename the source file (by appending a number) and then move it, or skip moving the file altogether.
*   **Directory Creation**: Automatically creates necessary destination directories and subdirectories if they do not already exist.

## Installation
1.  **Save the script**: Download or copy the provided `fileorganizer.py` script to your desired location.

2.  **Create `extensiondict.py`**: This script relies on a companion file named `extensiondict.py` which defines how file extensions map to organizational folders. Create `extensiondict.py` in the **same directory** as `fileorganizer.py` with content similar to the example below.

    *   **Example `extensiondict.py` content:**
        ```python
        # extensiondict.py
        extension_dict = {
            '.jpg': 'Images',
            '.jpeg': 'Images',
            '.png': 'Images',
            '.gif': 'Images',
            '.bmp': 'Images',
            '.pdf': 'PDFs',
            '.doc': 'Documents',
            '.docx': 'Documents',
            '.txt': 'Documents',
            '.xls': 'Spreadsheets',
            '.xlsx': 'Spreadsheets',
            '.ppt': 'Presentations',
            '.pptx': 'Presentations',
            '.zip': 'Archives',
            '.rar': 'Archives',
            '.mp4': 'Videos',
            '.mov': 'Videos',
            '.avi': 'Videos',
            '.mp3': 'Audio',
            '.wav': 'Audio',
            '.exe': 'Executables',
            '.py': 'Scripts',
            # Add more extensions and their corresponding folder names as needed
        }

        def getpath(extension):
            """Returns the folder name for a given file extension."""
            # Default to 'Other' if the extension is not found in the dictionary
            return extension_dict.get(extension, 'Other')
        ```
    *   **Important**: Customize `extension_dict` in `extensiondict.py` to match your preferred organizational structure. Extensions not explicitly defined in the dictionary will be placed in a default 'Other' folder if you use the example `getpath` function.

## Usage
Run the script from your command line, providing the source directory path and the destination directory path as arguments.

```bash
python fileorganizer.py <source_directory_path> <destination_directory_path>
```

*   `<source_directory_path>`: The absolute or relative path to the folder containing the files you want to organize.
*   `<destination_directory_path>`: The absolute or relative path to the base folder where files will be moved and organized into subfolders.

**Example Command:**
```bash
python fileorganizer.py "C:\Users\YourUser\Downloads" "C:\Users\YourUser\Organized Files"
```

## Examples

Let's assume your `Downloads` folder (`C:\Users\YourUser\Downloads`) contains the following files:

```
Downloads/
├── report_2022.pdf (created in 2022)
├── vacation_pic.jpg (created in 2023)
├── project_plan.docx (created in 2023)
├── old_photo.png (created in 2021)
└── presentation.pptx (created in 2022)
```

And your `extensiondict.py` maps `.pdf` to `PDFs`, `.jpg`/`.png` to `Images`, `.docx` to `Documents`, and `.pptx` to `Presentations`.

After running the script with `python fileorganizer.py "C:\Users\YourUser\Downloads" "C:\Users\YourUser\Organized Files"`, your `Organized Files` directory might look like this:

```
Organized Files/
├── PDFs/
│   └── 2022/
│       └── report_2022.pdf
├── Images/
│   ├── 2023/
│   │   └── vacation_pic.jpg
│   └── 2021/
│       └── old_photo.png
├── Documents/
│   └── 2023/
│       └── project_plan.docx
└── Presentations/
    └── 2022/
        └── presentation.pptx
```
The files are also removed from the `Downloads` folder.

## Limitations or Notes

*   **Windows-Specific**: The script uses the `move` command via `os.system()`, which is a Windows shell command. This script will not work directly on macOS or Linux without modification to the `movefile` function. For cross-platform compatibility, Python's `shutil.move` function would typically be used.
*   **File Movement**: Files are *moved*, not copied. This means they are removed from the source directory once successfully transferred.
*   **Interactive**: When a file with the same name already exists in the destination, the script will pause and prompt for user input (`1` to rename and move, any other key to skip).
*   **Dependency on `extensiondict.py`**: The script's functionality is heavily reliant on the `extensiondict.py` file being correctly set up in the same directory and containing a `getpath` function and an `extension_dict` mapping file extensions to desired folder names.
*   **Renaming Logic**: If a file clash occurs and the user opts to rename, the renaming process happens in the *source* directory first (e.g., `original.txt` becomes `original1.txt`), and then this renamed file is moved. This process repeats until a unique name is found in the destination.
