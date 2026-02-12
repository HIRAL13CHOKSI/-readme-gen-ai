# PDF Merger

## Overview
PDF Merger is a simple Python utility that allows users to merge multiple PDF files into a single PDF document using a graphical user interface (GUI). The application is built with Tkinter for the GUI and utilizes the PyPDF2 library for PDF manipulation.

## Features
- Select multiple PDF files to merge.
- Clear the list of selected files.
- Save the merged PDF to a specified location.
- User-friendly GUI for easy interaction.

## Installation
To use PDF Merger, ensure you have Python installed on your system. You will also need to install the `PyPDF2` library, which can be done using pip:

```bash
pip install PyPDF2
```

## Usage
1. Run the script using Python:
   ```bash
   python pdfmerger.py
   ```
2. Use the "Open Files" button to select the PDF files you want to merge.
3. After selecting the files, they will be listed in the GUI.
4. If you want to remove the selected files, click the "Delete Files" button.
5. Once you are ready to merge, click the "Merge Files" button and choose a location to save the merged PDF.

## Examples
- To merge files, select multiple PDFs from your file system, and then specify the output file name and location when prompted.

## Limitations or Notes
- Ensure that the `PyPDF2` library is installed; otherwise, the script will raise a `ModuleNotFoundError`.
- The application currently does not support merging files with bookmarks or other advanced PDF features.
- The GUI is fixed in size and may not resize based on content.
