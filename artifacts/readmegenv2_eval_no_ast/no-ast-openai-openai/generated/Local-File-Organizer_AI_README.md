# Local File Organizer

## Overview
The **Local File Organizer** is a Python script designed to help users organize files in a specified directory based on various criteria, such as content, date, or type. It provides a user-friendly interface for selecting organization methods and simulating the proposed directory structure before making any changes.

## Features
- Organize files by:
  - Content (using text and image processing models)
  - Date
  - Type
- Simulate and display the proposed directory structure before executing changes.
- Option to enable silent mode, which logs outputs to a file instead of displaying them in the terminal.
- Supports text and image file processing using advanced models.
- User prompts for input paths and organization methods.

## Installation
To run this script, ensure you have Python installed on your machine. You will also need to install the required dependencies, which are not specified in this README. You can typically install them using pip:

```bash
pip install -r requirements.txt
```

*Note: The script imports modules like `file_utils`, `data_processing_common`, and others, which must be available in your Python environment.*

## Usage
1. Clone or download the repository containing the script.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

```bash
python Local-File-Organizer.py
```

4. Follow the on-screen prompts to organize your files.

### Example Commands
- When prompted for the directory to organize, enter the full path, e.g., `C:\Users\YourUsername\Documents\MyFiles`.
- Choose the organization method by entering `1`, `2`, or `3` for content, date, or type, respectively.

## Examples
1. **Organizing by Content**:
   - Select "1" when prompted.
   - The script will initialize models for processing text and image files, then organize files based on their content.

2. **Organizing by Date**:
   - Select "2" when prompted.
   - The script will organize files based on their last modified date.

3. **Organizing by Type**:
   - Select "3" when prompted.
   - The script will categorize files into folders based on their file types (e.g., images, documents).

## Limitations or Notes
- Ensure that all required modules are available in your Python environment, as the script relies on them for functionality.
- The script may take some time to process files, especially if there are many files or large files in the specified directory.
- If you encounter a `ModuleNotFoundError`, ensure that the necessary modules are installed and accessible in your Python path.

This README provides a concise guide to using the Local File Organizer script effectively. For further assistance, refer to the script's inline comments or documentation for the imported modules.
