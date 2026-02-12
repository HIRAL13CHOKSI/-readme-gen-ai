# PDF Merger

## Overview
PDF Merger is a simple Python utility that allows users to merge multiple PDF files into a single PDF document using a graphical user interface (GUI). The application leverages the `PyPDF2` library for handling PDF files and provides an easy way to select, manage, and merge PDFs.

## Features
- Select multiple PDF files to merge.
- Clear the list of selected files.
- Save the merged PDF to a specified location.
- User-friendly GUI built with Tkinter.

## Installation
To use PDF Merger, ensure you have Python installed on your system. You will also need to install the `PyPDF2` library. You can install it using pip:

```bash
pip install PyPDF2
```

## Usage
1. Run the script using Python:
   ```bash
   python pdfmerger.py
   ```
2. Use the "Open Files" button to select the PDF files you want to merge.
3. The selected files will be displayed in the GUI.
4. If you want to remove the selected files, click the "Delete Files" button.
5. Click the "Merge Files" button to combine the selected PDFs into a single file. You will be prompted to choose a location to save the merged PDF.

## Examples
- To merge files named `file1.pdf`, `file2.pdf`, and `file3.pdf`, simply select them using the "Open Files" button, then click "Merge Files" to save the combined document.

## Limitations or Notes
- Ensure that the `PyPDF2` library is installed; otherwise, the script will raise a `ModuleNotFoundError`.
- The GUI is designed to be simple and may not handle very large files or a large number of files efficiently.
- The script currently does not support merging files with bookmarks from the original PDFs.
