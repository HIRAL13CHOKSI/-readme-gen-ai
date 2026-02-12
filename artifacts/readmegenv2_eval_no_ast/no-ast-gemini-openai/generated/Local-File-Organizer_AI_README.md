```markdown
# Local File Organizer

## Overview

This Python script organizes files within a specified directory. It provides three organization modes: by content (using AI models to categorize files), by date, and by file type. The script offers a "silent mode" where outputs are logged to a file instead of being displayed in the terminal.  It simulates the directory structure before making changes, allowing the user to confirm the intended outcome.

**Note**: This script requires several custom modules (`file_utils`, `data_processing_common`, `text_data_processing`, `image_data_processing`, `output_filter`, and `nexa.gguf`) that are not included in the provided code. To use this script, you must implement these modules.

## Features

*   **Organization Modes:**
    *   **By Content:** Utilizes AI models to categorize images and text files based on their content.
    *   **By Date:** Organizes files into subdirectories based on their modification date.
    *   **By Type:** Organizes files into subdirectories based on their file extension.
*   **Dry Run Simulation:**  Displays a simulated directory structure before any changes are made, allowing users to preview the organization.
*   **Silent Mode:** Logs all outputs to a text file (`operation_log.txt`) instead of displaying them in the terminal.
*   **Error Handling:** Includes basic error handling for invalid file paths and unsupported file types.
*   **NLTK Data Handling**: Ensures required NLTK data (stopwords, punkt, wordnet) is downloaded.

## Installation

1.  Save the script as `Local-File-Organizer.py`.
2.  **Crucially, implement the following missing modules:**
    *   `file_utils.py`: Contains functions `display_directory_tree`, `collect_file_paths`, `separate_files_by_type`, and `read_file_data`.
    *   `data_processing_common.py`: Contains functions `compute_operations`, `execute_operations`, `process_files_by_date`, and `process_files_by_type`.
    *   `text_data_processing.py`: Contains function `process_text_files`.
    *   `image_data_processing.py`: Contains function `process_image_files`.
    *   `output_filter.py`:  Defines a context manager `filter_specific_output` to suppress specific outputs.
    *   `nexa/gguf.py`: Contains classes `NexaVLMInference` and `NexaTextInference`.
3.  Ensure you have the `nltk` package installed. If not, install it using `pip install nltk`.

## Usage

1.  Run the script from the command line:

    ```bash
    python Local-File-Organizer.py
    ```

2.  The script will prompt you for the following information:

    *   Whether to enable silent mode.
    *   The path of the directory you want to organize.
    *   The path to store the organized files (or press Enter to use the default "organized\_folder" within the input directory).

3.  You will then be prompted to select an organization mode:

    *   Enter `1` for content-based organization.
    *   Enter `2` for date-based organization.
    *   Enter `3` for type-based organization.
    *   Enter `/exit` to quit.

4.  After selecting a mode, the script will simulate the proposed directory structure.  You will be asked to confirm the changes before they are applied.

## Examples

### Example 1: Organizing a directory by file type

1.  Run the script: `python Local-File-Organizer.py`
2.  Answer "no" to silent mode.
3.  Enter the input directory: `C:\MyFiles`
4.  Press Enter to use the default output directory.
5.  Select mode 3 (by type).
6.  Review the simulated directory structure.
7.  Answer "yes" to proceed.

This will create subdirectories within `C:\MyFiles\organized_folder` (or wherever you specify), with names based on file extensions, and move the files accordingly.

### Example 2: Using silent mode

1.  Run the script: `python Local-File-Organizer.py`
2.  Answer "yes" to silent mode.
3.  Enter the input directory: `/home/user/documents`
4.  Enter the output directory: `/home/user/organized`
5.  Select mode 2 (by date).
6.  Answer "yes" to proceed.

All output will be logged to `operation_log.txt` in the script's directory.

## Limitations or Notes

*   **Missing Modules:** The script relies on external modules (`file_utils`, `data_processing_common`, `text_data_processing`, `image_data_processing`, `output_filter`, and `nexa.gguf`) which are not included in the code. These need to be implemented separately for the script to function.
*   **AI Model Initialization:**  The content-based organization mode requires the `NexaVLMInference` and `NexaTextInference` classes which are part of the missing modules.  These likely involve downloading and initializing AI models, which can take a significant amount of time and resources. The model paths are hardcoded as `"llava-v1.6-vicuna-7b:q4_0"` and `"Llama3.2-3B-Instruct:q3_K_M"`.
*   **Error Handling:** The error handling is basic.  More robust error handling should be implemented.
*   **File Reading:**  The `read_file_data` function within `file_utils` must handle various text file encodings to prevent errors.
*   **NLTK Download:** The NLTK data download is done without progress information. Consider adding feedback to the user during download.
*   **Link Handling:** The script tracks 'hardlink' and 'symlink' counts, but it doesn't appear to be actually creating them, or behaving differently based on their presence.
*   **Context Window:** Consider the context window (n\_ctx) of the text inference model, particularly for long files.  The code comments mention adding `n_ctx=2048` if context window errors occur.
```
