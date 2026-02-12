This README provides a concise overview of the `pdfmerger.py` script, its features, installation steps, and usage instructions based solely on the provided source code and runtime error.

---

# PDF Merger Utility

## Overview
`pdfmerger.py` is a simple, standalone Python utility that provides a graphical user interface (GUI) for merging multiple PDF files into a single combined document. It's designed for quick and straightforward concatenation of PDF files through an easy-to-use interface.

## Features
*   **Merge PDF Files:** Combine any number of selected PDF documents into one unified file.
*   **Intuitive GUI:** User-friendly graphical interface built with Python's Tkinter library.
*   **Multiple File Selection:** Select multiple input PDF files simultaneously using a standard file dialog.
*   **Clear Selection:** Easily remove all currently selected files from the list to start over.
*   **Save Merged PDF:** Choose a custom location and filename for the output merged PDF via a save dialog.
*   **Display Selected Files:** Shows the base names of the chosen PDF files within the application window.

## Installation
This script requires the `PyPDF2` library to handle PDF operations. Tkinter, used for the GUI, is typically included with standard Python installations.

1.  **Install `PyPDF2`:**
    Open your terminal or command prompt and install the required library:
    ```bash
    pip install PyPDF2
    ```
2.  **Save the script:**
    Save the provided source code into a file named `pdfmerger.py` (or any other `.py` extension).

## Usage
To use the PDF Merger, simply run the Python script. All interactions are performed through the launched graphical interface.

1.  **Launch the application:**
    Open your terminal or command prompt, navigate to the directory where you saved `pdfmerger.py`, and run:
    ```bash
    python pdfmerger.py
    ```
    A "PDF Merger" window will appear.

2.  **Open Files:**
    Click the "Open Files" button. A file selection dialog will open, allowing you to browse and select one or more PDF files you wish to merge. The names of the selected files will be displayed in the application window.

3.  **Merge Files:**
    Once you have selected all the desired PDF files, click the "Merge Files" button. A save dialog will then appear, prompting you to choose a destination and provide a name for your new, merged PDF file.

4.  **Clear Files (Optional):**
    If you need to remove all currently selected files from the list (e.g., to select a new set of files), click the "Delete Files" button.

## Examples
Let's assume you have a set of PDF documents like `chapter1.pdf`, `chapter2.pdf`, and `appendix.pdf` that you want to combine into a single book.

1.  **Run the script:**
    ```bash
    python pdfmerger.py
    ```
2.  **Select files:**
    In the launched "PDF Merger" GUI, click the "Open Files" button. Navigate to your documents and select `chapter1.pdf`, `chapter2.pdf`, and `appendix.pdf`. Click "Open" in the file dialog. The selected files will be listed in the application window.
3.  **Merge and save:**
    Click the "Merge Files" button. A save dialog will appear. Choose your desired output directory and enter `MyBook.pdf` as the filename. Click "Save".
4.  A new PDF file named `MyBook.pdf` will be created at your specified location, containing the content of `chapter1.pdf`, `chapter2.pdf`, and `appendix.pdf` in the order they were selected.

## Limitations or Notes
*   **GUI Only:** This utility is designed exclusively for GUI interaction and does not support command-line arguments for file input or output.
*   **Bookmark Handling:** When merging, existing bookmarks from the individual input PDF files are explicitly not imported into the final merged document.
*   **Merge Order:** Files are merged in the sequential order they were selected in the "Open Files" dialog.
