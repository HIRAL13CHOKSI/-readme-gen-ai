```markdown
# PDF Merger

A simple tool to merge PDF files using a Tkinter-based GUI.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen)

## Overview

`pdfmerger.py` is a Python script that provides a graphical user interface (GUI) for merging multiple PDF files into a single PDF document. It leverages the Tkinter library for the GUI and PyPDF2 for PDF manipulation.

Key features:

-   User-friendly Tkinter GUI for selecting and merging PDF files.
-   Ability to add, remove, and clear files from the merge list.
-   Cross-platform compatibility (runs on any OS supported by Python and Tkinter).

## Requirements

-   Python 3.7+
-   Operating System: Any OS that supports Python and Tkinter (Windows, macOS, Linux)

## Dependencies

### Standard Library

-   `tkinter`

### Third-Party Packages

-   `PyPDF2`
-   `google-generativeai`
-   `groq`
-   `openai`

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r ..\requirements.txt
```

Alternatively, you can install the package and its dependencies in editable mode:

```bash
pip install -e .
```

## Usage

To run the PDF Merger GUI, execute the script:

```bash
python pdfmerger.py
```

This will launch the Tkinter-based GUI, allowing you to select, merge, and save PDF files.

## Flags

None

## Examples

1.  Run the PDF Merger GUI:

    ```bash
    python pdfmerger.py
    ```

    This command starts the application, presenting the graphical interface for PDF merging.
2.  After running the application, use the "Add Files" button to select PDF files. Reorder them as needed, and then click "Merge Files" to create a single PDF.

## Input/Output

| Input       | Output                                 |
| ----------- | -------------------------------------- |
| PDF files   | Merged PDF file                        |

## Testing

To run tests, use pytest:

```bash
pytest
```

## Troubleshooting

1.  **Missing Dependencies:** If you encounter import errors, ensure that you have installed all the required dependencies using `pip install -r ..\requirements.txt`.
2.  **Tkinter Issues:** If the GUI does not launch, verify that Tkinter is properly installed and configured on your system.  Tkinter usually comes pre-packaged with most Python installations.

## Contributing

Coming soon

## License

Coming soon
```
