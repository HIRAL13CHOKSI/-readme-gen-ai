```markdown
# Clippy

## Overview

Clippy is a simple clipboard manager application written in Python using the Tkinter GUI toolkit. It monitors the clipboard for changes and displays a history of recent clippings in the application window.  Clicking on a clipping copies it back to the clipboard.

## Features

- Monitors the system clipboard for new content.
- Displays a history of clipboard entries in a list.
- Clicking an entry copies it back to the clipboard.
- "Always on top" option.
- Clear all clippings option.

## Installation

1.  Ensure you have Python 3 installed.
2.  Install the `pyperclip` package:

    ```bash
    pip install pyperclip
    ```

## Usage

1.  Save the script (`clippy.py`).
2.  Run the script from the command line:

    ```bash
    python clippy.py
    ```

The Clippy window will appear, displaying the most recent clipboard entries.

## Examples

1.  Copy some text to your clipboard. It will appear in the Clippy window.
2.  Copy different text. The Clippy window will update with the new entry, pushing older entries down the list.
3.  Click on a displayed clipping in the Clippy window. The clicked clipping will be copied back to your clipboard.
4.  From the "Options" menu, select "Always on top" to keep the Clippy window visible above other windows.
5.  From the "Options" menu, select "Clear all (except last)" to clear all clippings from the application.

## Limitations or Notes

-   The application displays a truncated version of the clipboard content to maintain readability. The full content is copied back to the clipboard when an item is clicked.
-   The number of clippings displayed is limited to 10. This can be changed by modifying the `maxClippingsOnApp` variable in the script.
-   The script requires the `pyperclip` library. Ensure it is installed before running the script.
```
