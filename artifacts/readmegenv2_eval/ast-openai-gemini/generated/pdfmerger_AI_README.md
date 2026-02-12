```markdown
# PDF Merger
A simple tool for merging PDF files.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

## Overview
PDF Merger is a straightforward command-line utility designed to merge multiple PDF files into a single document. It leverages the `PyPDF2` library for PDF manipulation. Notable features include:

- User-friendly interface for selecting files.
- Efficient merging of multiple PDF documents.

## Requirements
- **Python Version**: 3.6 or higher
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
1. **Basic Usage**: To merge PDF files, simply run the script:
   ```bash
   python pdfmerger.py
   ```

2. **Using with Docker**: (Note: No Dockerfile is present, but if it were, the command would look like this)
   ```bash
   docker build -t pdfmerger .
   docker run pdfmerger
   ```

## Input/Output
| Input | Output |
|-------|--------|
| Multiple PDF files | Merged PDF file |

## Testing
To run tests, use `pytest`:

```bash
pytest
```

## Troubleshooting
- **Issue**: The application fails to open.
  - **Solution**: Ensure that you have the required dependencies installed.
  
- **Issue**: Merging fails with an error.
  - **Solution**: Check that the input PDF files are not corrupted.

## Contributing
Coming soon.

## License
Coming soon.
```
