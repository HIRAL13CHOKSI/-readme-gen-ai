```markdown
# Clippy

A simple clipboard manager using Tkinter.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads)
![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen)

## Overview

Clippy is a basic clipboard manager built with Tkinter. It allows users to store and retrieve clipboard history within a simple GUI.  Notable features include:

*   Simple Tkinter-based GUI
*   Clipboard history management
*   Easy copy/paste functionality via the GUI

## Requirements

*   Python 3.7+
*   Operating System:  Platform independent

## Dependencies

### Standard Library

*   `tkinter`

### Third-Party Packages

*   `google-generativeai`
*   `groq`
*   `openai`
*   `pyperclip`

## Installation

Install the required dependencies using `pip`:

```bash
pip install -r ../requirements.txt
```

Alternatively, for an editable install:

```bash
pip install -e .
```

## Usage

To run Clippy:

```bash
python clippy.py
```

## Flags

None

## Examples

Run the application:

```bash
python clippy.py
```

This will launch the Clippy GUI.

## Input/Output

| Input       | Output                  |
| ----------- | ----------------------- |
| User clicks | Content copied to clipboard |
| System clipboard | Content is logged in GUI |

## Testing

Tests are included with this project. To run the tests, use `pytest`:

```bash
pytest
```

## Troubleshooting

*   **Issue:**  The GUI does not appear.
    *   **Possible Solution:** Ensure you have a compatible version of Tkinter installed.  On some systems, you may need to install `python3-tk`.

*   **Issue:**  Copy/paste functionality is not working.
    *   **Possible Solution:**  Verify that `pyperclip` is installed correctly and that your system supports its clipboard access methods.

## Contributing

Coming soon

## License

Coming soon
```
