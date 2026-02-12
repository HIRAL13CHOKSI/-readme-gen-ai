# Wisdom Tree App

## Overview
Wisdom Tree is a Python-based command-line application designed to enhance productivity through a Pomodoro timer, motivational quotes, and background music. It utilizes a text-based user interface to manage tasks and provide notifications, making it an ideal tool for focused work sessions.

## Features
- **Pomodoro Timer**: Manage work and break intervals to enhance productivity.
- **Motivational Quotes**: Display random quotes to inspire and motivate users.
- **Media Player**: Play background music, including YouTube links, with volume control.
- **Interactive Menu**: Navigate through options using keyboard shortcuts.
- **Notifications**: Display notifications for timer updates and media playback.

## Installation
To run the Wisdom Tree app, ensure you have Python installed on your system. You will also need to install the `curses` library, which may require additional steps depending on your operating system.

### Windows Installation
1. Install Windows Subsystem for Linux (WSL) or use a compatible terminal that supports `curses`.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies
- `curses` (available on Unix-like systems; for Windows, consider using WSL)
- Additional libraries may be required based on the `wisdom_tree` package structure.

## Usage
To run the application, execute the script in your terminal:

```bash
python wisdom_tree.py
```

### Key Commands
- `q`: Quit the application.
- `SPACE`: Pause or resume the timer.
- `m`: Pause the media playback.
- `u`: Toggle sound effects on/off.
- `[` / `]`: Decrease/increase media volume.
- `r`: Toggle repeat mode for media playback.
- `1-9`: Seek to specific positions in the media.

## Examples
1. **Starting the Application**: Launch the application using the command:
   ```bash
   python wisdom_tree.py
   ```
2. **Using the Pomodoro Timer**: Select the Pomodoro timer option from the menu and start your work session.
3. **Playing Music**: Navigate to the media section and enter a YouTube URL to play music while you work.

## Limitations or Notes
- The application relies on the `curses` library, which may not be available on all platforms, particularly Windows without WSL.
- Ensure that the required media files and configurations are set up correctly in the `wisdom_tree` package for optimal functionality.
- The application may require additional dependencies based on the specific implementation of the `wisdom_tree` package.

Feel free to explore and modify the code to suit your productivity needs!
