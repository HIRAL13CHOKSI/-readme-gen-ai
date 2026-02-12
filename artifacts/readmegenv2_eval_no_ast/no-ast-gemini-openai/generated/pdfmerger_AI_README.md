```markdown
# PDF Merger

## Overview

This Python script provides a simple graphical user interface (GUI) for merging multiple PDF files into a single PDF document. It uses the `PyPDF2` library to perform the merging and `tkinter` for the GUI.

## Features

*   **Graphical User Interface:** Uses `tkinter` for an easy-to-use interface.
*   **File Selection:** Allows users to select multiple PDF files for merging using a file dialog.
*   **File List Display:** Displays the selected PDF files in the GUI.
*   **Clear Selection:** Provides a button to clear the current selection of files.
*   **Save Merged PDF:** Allows users to choose the location and name for the merged PDF file.

## Installation

1.  Make sure you have Python installed.
2.  Install the required packages:

    ```bash
    pip install PyPDF2
    ```

## Usage

1.  Save the script as a `.py` file (e.g., `pdfmerger.py`).
2.  Run the script from the command line:

    ```bash
    python pdfmerger.py
    ```

3.  A window titled "PDF Merger" will appear.
4.  Click the "Open Files" button to select the PDF files you want to merge.
5.  The selected files will be displayed in the window.
6.  If needed, click "Delete Files" to clear the selection and start over.
7.  Click the "Merge Files" button to merge the selected PDF files.
8.  A file dialog will prompt you to choose a location and filename for the merged PDF.
9.  The merged PDF file will be created in the specified location.

## Examples

1.  **Merging three PDF files:**
    *   Run the script.
    *   Click "Open Files" and select `file1.pdf`, `file2.pdf`, and `file3.pdf`.
    *   Click "Merge Files".
    *   Choose a location and name (e.g., `merged.pdf`) for the merged file.
    *   A new file named `merged.pdf` will be created containing the contents of the three input files.

## Limitations or Notes

*   This script requires the `PyPDF2` library to be installed.
*   The script does not handle password-protected PDF files.
*   The script imports all bookmarks which might lead to unexpected result.
