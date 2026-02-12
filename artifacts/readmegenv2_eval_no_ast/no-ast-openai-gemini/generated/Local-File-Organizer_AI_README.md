# Local File Organizer

## Overview
The **Local File Organizer** is a Python script designed to help users organize their files within a specified directory. It allows sorting files by content, date, or type, and provides a simulation of the proposed directory structure before making any changes. The script also supports silent mode for logging operations without displaying them in the terminal.

## Features
- Organize files by:
  - Content
  - Date
  - Type
- Simulate the proposed directory structure before executing changes.
- Silent mode for logging operations to a file.
- User-friendly prompts for input and confirmation.
- Supports processing of text and image files using machine learning models.

## Installation
To run the Local File Organizer, ensure you have Python installed on your machine. You will also need to install the required dependencies, which are not specified in the code but may include libraries for file handling and data processing.

1. Clone the repository or download the script.
2. Install necessary dependencies (if any) using pip:
   ```bash
   pip install <dependency_name>
   ```

## Usage
To use the Local File Organizer, run the script from the command line:

```bash
python Local-File-Organizer.py
```

### Example Commands
1. When prompted, enter the path of the directory you want to organize.
2. Choose the mode of organization:
   - Enter `1` for organizing by content.
   - Enter `2` for organizing by date.
   - Enter `3` for organizing by type.
3. Confirm the output path for organized files or press Enter to use the default.

## Examples
- To organize files in `C:\Users\colel\Documents\MyFiles` by content:
  1. Run the script.
  2. Input: `C:\Users\colel\Documents\MyFiles`
  3. Select mode: `1`
  4. Confirm output path or provide a new one.

## Limitations or Notes
- The script requires certain modules (`file_utils`, `data_processing_common`, `text_data_processing`, `image_data_processing`, `output_filter`, and `nexa.gguf`) that are not included in the provided code. Ensure these modules are available in your environment.
- The script uses NLTK for text processing; ensure NLTK data is downloaded as prompted.
- The script may take time to process files, especially if there are many files or large file sizes.
- The silent mode logs outputs to a text file instead of displaying them in the terminal, which can be useful for tracking operations without cluttering the console.
