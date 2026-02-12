# Clippy README

## Overview
Clippy is a simple clipboard manager built using Python and Tkinter. It allows users to monitor and manage clipboard content, displaying the latest clippings in a user-friendly interface. Users can easily copy previous clipboard entries back to the clipboard and clear the history when needed.

## Features
- Displays the last 10 clipboard entries.
- Automatically updates the displayed entries when new content is copied to the clipboard.
- Option to keep the application always on top of other windows.
- Clear all clipboard entries except the most recent one.
- User-friendly interface with clickable entries for easy copying.

## Installation
To run Clippy, ensure you have Python installed on your system. You will also need to install the `pyperclip` module, which can be done using pip:

```bash
pip install pyperclip
```

## Usage
1. Clone or download the Clippy script.
2. Run the script using Python:

```bash
python clippy.py
```

3. Use the application to manage your clipboard entries.

### Example Commands
- **Run the application:**
  ```bash
  python clippy.py
  ```

## Examples
- Copy text to your clipboard (e.g., from a document or web page).
- Open Clippy, and the application will display the copied text.
- Click on any entry in the Clippy window to copy it back to your clipboard.
- Use the "Options" menu to clear all entries or toggle the "Always on top" feature.

## Limitations or Notes
- The application currently supports a maximum of 10 clipboard entries.
- The displayed text is truncated to 100 characters for better readability.
- The application may not function correctly if the `pyperclip` module is not installed, leading to a `ModuleNotFoundError`.
- The application is designed for a fixed window size of 600x600 pixels and cannot be resized.
