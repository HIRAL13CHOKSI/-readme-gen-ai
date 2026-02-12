# Clippy

## Overview
Clippy is a simple clipboard manager application built using Python and Tkinter. It allows users to monitor clipboard content, display recent clippings, and easily copy them back to the clipboard. The application provides a user-friendly interface and supports multiple clipboard entries.

## Features
- Monitors clipboard content in real-time.
- Displays up to 10 recent clipboard entries.
- Option to keep the application always on top.
- Clear all clipboard entries except the last one.
- Clickable entries to copy them back to the clipboard.
- User-friendly graphical interface.

## Installation
To run Clippy, ensure you have Python installed on your system. You will also need to install the `pyperclip` library for clipboard functionality. You can install it using pip:

```bash
pip install pyperclip
```

## Usage
1. Clone or download the Clippy script.
2. Run the script using Python:

```bash
python clippy.py
```

3. The Clippy application window will appear, monitoring your clipboard.

## Examples
- **Copying Text**: Simply copy any text to your clipboard. Clippy will display it in the application window.
- **Clicking Entries**: Click on any entry in the Clippy window to copy it back to your clipboard.
- **Clearing Entries**: Use the "Clear all (except last)" option from the menu to reset the clipboard history.

## Limitations or Notes
- The application currently supports a maximum of 10 clipboard entries.
- Clipboard entries are truncated to a maximum length of 100 characters for display purposes.
- The application may not function correctly if the `pyperclip` module is not installed.
- The application does not persist clipboard history after it is closed; all entries are lost upon exit.
