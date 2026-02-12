# PDF Merger GUI

A simple GUI tool for merging multiple PDF files into a single document.

---

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/your-org/your-repo/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/your-repo/actions/workflows/ci.yml)

## Overview

`pdfmerger.py` provides a user-friendly graphical interface built with `tkinter` to effortlessly combine multiple PDF documents. Users can select various PDF files from their system, arrange them as needed, and merge them into one consolidated PDF output file.

Notable features include:
*   Intuitive GUI for file selection and management.
*   Ability to add and clear selected PDF files.
*   Efficient merging of documents using `PyPDF2`.

## Requirements

*   **Python**: Version 3.7 or higher
*   **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies

This project relies on the following modules:

### Standard Library
*   `tkinter`: Python's standard GUI (Graphical User Interface) package.

### Third-Party Packages
*   `PyPDF2`: A free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.
*   `google-generativeai`: (Project-level dependency)
*   `groq`: (Project-level dependency)
*   `openai`: (Project-level dependency)

### External Tools
None specified.

## Installation

To get started, clone the repository (if applicable) and install the required dependencies.

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/your-org/your-repo.git
    cd your-repo
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r ..\requirements.txt
    ```

3.  **For local development (optional):**
    If you're developing the tool, you might want to install it in editable mode:
    ```bash
    pip install -e .
    ```

## Usage

To launch the PDF Merger GUI, simply run the Python script:

```bash
python pdfmerger.py
```

This will open a new window where you can interact with the tool.

## Flags

None. This script is designed to be run without command-line arguments, operating entirely through its graphical user interface.

## Environment Variables

None specified.

## Examples

### 1. Launching the GUI and Merging PDFs

To start the application and merge a series of PDF files:

```bash
python pdfmerger.py
```

1.  **Launch the application** by running the command above.
2.  In the GUI, click the "Open Files" button to select multiple PDF documents from your file system.
3.  The selected file paths will appear in the listbox. You can remove files using the "Clear Files" button if needed (though the current interface only clears all, not individual files).
4.  Click the "Merge Files" button. A save dialog will appear, prompting you to choose a location and filename for the merged PDF.
5.  After selecting a save path, the application will combine the selected PDFs into a single output file.

### 2. Basic Workflow Description

The primary use case is interactive:

*   **Select Files**: Use the "Open Files" button to browse and select all the PDF documents you wish to combine. The order of selection often determines the merging order.
*   **Review/Clear**: The selected files will be listed. If you need to start over, the "Clear Files" button can reset the list.
*   **Merge and Save**: Click "Merge Files", choose your desired output filename and location, and the application will create a new, consolidated PDF.

## Input/Output

| Type   | Description                                   |
| :----- | :-------------------------------------------- |
| Input  | Multiple PDF files (selected via GUI)         |
| Output | A single merged PDF file (saved to disk)      |

## Testing

This project includes tests to ensure reliability. To run them, navigate to the project root and execute `pytest`:

```bash
pytest
```

## Troubleshooting

1.  **GUI Window Not Appearing**:
    *   **Issue**: After running `python pdfmerger.py`, no window appears.
    *   **Solution**: Ensure `tkinter` is correctly installed with your Python distribution. It usually comes bundled with standard Python installations. If you're using a minimal Python setup, you might need to install `python-tk` or similar packages via your system's package manager (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu, `brew install python-tk` on macOS). Check your Python installation for `_tkinter` module presence.

2.  **File Permissions Errors**:
    *   **Issue**: When trying to open or save files, you encounter "Permission Denied" errors.
    *   **Solution**: Ensure that the user running the script has read permissions for the input PDF files and write permissions for the directory where the merged output PDF is intended to be saved. Try running the script from a directory where you have full read/write access, or adjust file/directory permissions as necessary.

## Contributing

Coming soon.

## License

Coming soon.
