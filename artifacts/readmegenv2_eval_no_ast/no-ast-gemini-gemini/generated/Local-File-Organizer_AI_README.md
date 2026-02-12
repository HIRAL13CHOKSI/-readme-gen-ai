This README provides an overview and usage instructions for the `Local-File-Organizer.py` script.

---

# Local-File-Organizer.py

## Overview

`Local-File-Organizer.py` is an interactive Python utility designed to help users organize files within a specified directory. It offers three distinct methods for organization: by content (leveraging AI models for classification), by date (based on file modification times), or by file type. The script allows for a simulated dry run to preview changes and supports a "silent mode" for logging operations to a file.

## Features

*   **Multiple Organization Modes**:
    *   **By Content**: Utilizes large language models (NexaVLM and NexaText) to categorize files based on their content (e.g., text summaries, image descriptions).
    *   **By Date**: Sorts files into folders based on their creation or modification date.
    *   **By Type**: Organizes files into folders according to their file extensions (e.g., `images`, `documents`).
*   **AI Model Integration**: Dynamically initializes `NexaVLMInference` and `NexaTextInference` models for intelligent content-based categorization.
*   **Interactive User Interface**: Guides the user through path selection, organization mode choice, and confirmation of operations via command-line prompts.
*   **Dry Run Simulation**: Displays a proposed directory structure before executing any file operations, allowing users to review and confirm changes.
*   **Silent Mode**: Option to suppress console output and log all operational messages to a specified text file (`operation_log.txt`).
*   **NLTK Integration**: Automatically downloads necessary NLTK data (stopwords, punkt, wordnet) for text processing tasks.
*   **Robust Path Handling**: Checks for valid input paths and allows for custom or default output directory creation.

## Installation

To use this script, ensure you have Python installed (version 3.x recommended).

### Prerequisites

1.  **Python Packages**: This script requires several external Python libraries. Install them using pip:
    ```bash
    pip install nltk nexa # (nexa is inferred as the source of NexaVLMInference and NexaTextInference)
    ```
2.  **NLTK Data**: The script will automatically download necessary NLTK data (`stopwords`, `punkt`, `wordnet`) upon its first run. Ensure you have an internet connection for this initial setup.
3.  **Companion Modules**: This script relies on several companion Python modules (`file_utils.py`, `data_processing_common.py`, `text_data_processing.py`, `image_data_processing.py`, `output_filter.py`) which must be present in the same directory as `Local-File-Organizer.py` or available in your Python path. These modules are imported directly by the script to provide its functionality.
4.  **AI Models**: For "By Content" organization, the script will attempt to initialize and potentially download the specified AI models (`llava-v1.6-vicuna-7b:q4_0` for image inference and `Llama3.2-3B-Instruct:q3_K_M` for text inference). This process is handled by the `nexa` library, which might require a network connection and significant disk space for model files.

## Usage

Run the script directly from your terminal:

```bash
python Local-File-Organizer.py
```

The script will guide you through the following steps:

1.  **Silent Mode**: Choose whether to log output to `operation_log.txt` instead of the console.
2.  **Input Directory**: Enter the full path to the directory you wish to organize. The script will validate this path.
3.  **Output Directory**: Enter the full path where organized files should be moved. If left blank, a new folder named `organized_folder` will be created in the parent directory of your input path.
4.  **Organization Mode**: Select one of the following options:
    *   `1. By Content`
    *   `2. By Date`
    *   `3. By Type`
5.  **Review Proposed Changes**: After processing, the script will display a simulated directory tree showing how your files will be organized.
6.  **Confirmation**: You will be asked to confirm if you want to proceed with the proposed changes.
    *   If you choose `yes`, the file operations will be executed.
    *   If you choose `no`, you can opt to select another sorting method or cancel the operation.
7.  **Organize Another Directory**: After completing an organization task, you can choose to process another directory.

### Example Commands

To start the organizer:

```bash
python Local-File-Organizer.py
```

Follow the interactive prompts:

```
--------------------------------------------------
**NOTE: Silent mode logs all outputs to a text file instead of displaying them in the terminal.
Would you like to enable silent mode? (yes/no): no
--------------------------------------------------
Enter the path of the directory you want to organize: /path/to/your/unorganized_files
Input path successfully uploaded: /path/to/your/unorganized_files
--------------------------------------------------
Enter the path to store organized files and folders (press Enter to use 'organized_folder' in the input directory):
Output path successfully set to: /path/to/organized_folder
--------------------------------------------------
... (prompts for organization mode, confirmation, etc.)
```

## Examples

### Organizing Files by Date

1.  Start the script: `python Local-File-Organizer.py`
2.  Choose `no` for silent mode.
3.  Enter your input directory (e.g., `/Users/username/Downloads`).
4.  Press Enter for the default output directory (e.g., `/Users/username/organized_folder`).
5.  Select `2` for "By Date" organization.
6.  Review the simulated directory tree, which will show files grouped by year, then month, then day (e.g., `/Users/username/organized_folder/2023/10-October/01-Sunday/my_file.txt`).
7.  Confirm to execute the operations.

### Organizing Files by Content (AI-Powered)

1.  Start the script: `python Local-File-Organizer.py`
2.  Choose `no` for silent mode.
3.  Enter your input directory.
4.  Enter your output directory.
5.  Select `1` for "By Content" organization.
6.  **Important**: The script will then initialize the AI models. This may take some time, especially on the first run as models might be downloaded. You will see messages like "Checking if the model is already downloaded. If not, downloading it now."
7.  After models are ready, the script will process files and generate categories based on their content (e.g., `/Users/username/organized_folder/Reports/report_2023.pdf`, `/Users/username/organized_folder/Nature_Photography/sunset.jpg`).
8.  Review the simulated directory tree and confirm to proceed.

## Limitations or Notes

*   **Model Downloads**: The "By Content" mode requires the `nexa` library and specific AI models. The initial setup might involve significant downloads depending on whether these models are already cached locally.
*   **Resource Intensive**: Content-based organization using AI models can be CPU/GPU and memory intensive, potentially taking a longer time for large numbers of files.
*   **Error Handling for Content**: For the "By Content" mode, files with unsupported or unreadable formats will be skipped with a message.
*   **NLTK Data**: The initial NLTK data download requires an active internet connection.
*   **Operating System Dependencies**: Path handling (`os.sep`, `os.path.relpath`) ensures compatibility with the operating system on which the script is run.
