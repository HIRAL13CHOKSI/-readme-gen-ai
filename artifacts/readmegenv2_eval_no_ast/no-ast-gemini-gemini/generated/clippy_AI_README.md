# Clippy: A Simple Clipboard History Manager

`clippy.py` is a lightweight, single-file Python utility that provides a graphical interface for managing your clipboard history. It continuously monitors the system clipboard and keeps a record of recent text clippings, allowing you to easily recall and reuse them.

## Overview

Clippy runs as a small Tkinter application, displaying a list of your most recent text clipboard entries. When you copy new text, it's added to the list. You can then click any item in the history to copy it back to your system clipboard.

## Features

*   **Clipboard Monitoring:** Automatically detects and stores new text copied to your system clipboard.
*   **Clipboard History:** Maintains a list of up to 10 recent text clippings.
*   **Easy Recall:** Click any item in the displayed list to copy it back to your system clipboard.
*   **Truncated Display:** Long clippings are automatically truncated for a cleaner display, while the full content is preserved internally.
*   **Always On Top Option:** Keep the Clippy window visible above other applications.
*   **Clear History:** Option to clear all stored clippings from the application.
*   **Character Filtering:** Automatically removes characters incompatible with Tkinter's text handling (characters with Unicode values greater than 65535).

## Installation

This script requires the `pyperclip` library to interact with the system clipboard.

1.  **Save the script:** Save the provided code as `clippy.py`.
2.  **Install `pyperclip`:** If you don't have it already, install `pyperclip` using pip:

    ```bash
    pip install pyperclip
    ```

## Usage

To run Clippy, simply execute the script from your terminal:

```bash
python clippy.py
```

A small window titled "Clippy" will appear. As you copy text from other applications, new entries will appear in this window.

### Example Commands

```bash
# Start the Clippy application
python clippy.py
```

### Interacting with the Application

*   **Copying History:** Click on any displayed text label to copy that specific clipping back to your system clipboard. The label will momentarily change its appearance to indicate it's been selected.
*   **Options Menu:**
    *   **Always on top:** Toggles whether the Clippy window stays on top of other applications.
    *   **Clear all:** Clears all displayed clippings and empties the internal history.

## Examples

1.  **Start Clippy:**
    ```bash
    python clippy.py
    ```
    (A small empty window appears.)

2.  **Copy Text from another application:**
    *   Copy "Hello, world!" from a browser.
    *   Copy "This is another piece of text." from a document.
    *   Copy "And a third one." from a chat application.

3.  **Observe Clippy:** The Clippy window will now show:
    ```
    Hello, world!
    This is another piece of text.
    And a third one.
    ```
    (Order depends on when they were copied and how many items are already present.)

4.  **Recall a clipping:** Click on "Hello, world!". This text is now copied back to your system clipboard, ready to be pasted into any other application.

## Limitations or Notes

*   **No Persistence:** Clipping history is not saved between application sessions. When you close Clippy, the history is lost.
*   **Maximum Clippings:** Only the 10 most recent/least-used clippings are displayed and stored. Older items are automatically removed to make space for new ones.
*   **Text-Only:** Clippy only manages plain text clippings. Images or other rich content copied to the clipboard are ignored.
*   **Character Compatibility:** Text containing certain high-value Unicode characters (above U+FFFF) might have those characters filtered out due to underlying Tkinter limitations.
