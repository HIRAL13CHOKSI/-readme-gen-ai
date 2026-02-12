# Wisdom Tree Application

## Overview
Wisdom Tree is a terminal-based application designed to enhance productivity through a Pomodoro timer, inspirational quotes, and a media player for concentration music. It utilizes the `curses` library for a text-based user interface and integrates with YouTube for music playback.

## Features
- **Pomodoro Timer**: Manage work sessions and breaks to boost productivity.
- **Inspirational Quotes**: Display random quotes to motivate users.
- **Media Player**: Play concentration music from local files or YouTube.
- **Interactive Menu**: Navigate through options using keyboard shortcuts.
- **Notifications**: Display notifications for various events (e.g., timer updates, media playback).

## Installation
To run the Wisdom Tree application, ensure you have Python installed on your system. You will also need the `curses` library, which is typically included with Python on Unix-like systems but may require additional setup on Windows.

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Install Curses for Windows**: If you are on Windows, you may need to install a compatible version of the `curses` library. You can use the `windows-curses` package:
   ```bash
   pip install windows-curses
   ```

## Usage
To run the application, execute the script from the command line:

```bash
python wisdom_tree.py
```

## Examples
- **Start a Pomodoro session**: Navigate to the "POMODORO TIMER" option in the menu and select it to start a work session.
- **Play YouTube music**: Select the "MEDIA" option and enter a YouTube URL to start playback.
- **Adjust volume**: Use the `[` and `]` keys to decrease or increase the media volume, respectively.

## Limitations or Notes
- The application requires a terminal that supports `curses`, which may not be available on all systems.
- Ensure that your terminal window is sufficiently large to display all elements properly.
- The application may not function correctly if the `curses` library is not installed or configured properly on Windows.

## Conclusion
Wisdom Tree is a versatile tool for enhancing productivity through structured work sessions, motivational quotes, and customizable music playback. Enjoy your journey to better focus and efficiency!
