```markdown
# PDF Merger
A simple tool to merge PDF files using Python.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue)

## Overview
PDF Merger is a straightforward command-line tool designed to merge multiple PDF files into a single document. It leverages the `PyPDF2` library for PDF manipulation. Notable features include:

- User-friendly interface for selecting files.
- Efficient merging of multiple PDFs.

## Requirements
- **Python Version**: 3.x
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Dependencies
### Standard Library
- `tkinter`

### Third-Party Packages
- `PyPDF2`
- `google-generativeai`
- `groq`
- `openai`

## Installation
To install the required dependencies, you can use the provided `requirements.txt` file:

```bash
pip install -r ../requirements.txt
```

For an editable install, you can run:

```bash
pip install -e .
```

## Usage
To run the PDF Merger, execute the following command:

```bash
python pdfmerger.py
```

## Flags
None

## Environment Variables
| Name | Default | Description |
|------|---------|-------------|
| None specified | - | Controls runtime behavior |

## Examples
1. To merge PDF files, run:
   ```bash
   python pdfmerger.py
   ```

2. If you want to run it in a different environment, ensure all dependencies are installed and execute the same command.

## Input/Output
| Input | Output |
|-------|--------|
| Multiple PDF files | A single merged PDF file |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: The application fails to open.
  - **Solution**: Ensure that all dependencies are installed correctly.
  
- **Issue**: Merging process hangs.
  - **Solution**: Check if the selected PDF files are corrupted or too large.

## Contributing
Coming soon.

## License
Coming soon.
```
