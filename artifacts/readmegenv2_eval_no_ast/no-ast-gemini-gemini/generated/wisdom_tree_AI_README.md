This document provides a concise overview and usage instructions for the `wisdom_tree.py` utility.

---

# wisdom_tree.py

## Overview

`wisdom_tree.py` is a command-line Text User Interface (TUI) application designed to enhance focus and productivity. It combines a visual "wisdom tree" that grows over time, a Pomodoro timer, and a versatile music player capable of playing local audio files or streaming from YouTube. The application provides an engaging environment to help users concentrate while offering inspirational quotes and customizable sound settings.

## Features

*   **Interactive TUI:** Navigate and interact with the application using keyboard controls in a terminal interface.
*   **Visual Wisdom Tree:** Observe a digital tree that symbolically grows as you spend time with the application.
*   **Pomodoro Timer:** Utilize a configurable Pomodoro timer to structure work and break intervals, promoting focused sessions.
*   **Flexible Music Player:**
    *   Play local `.ogg` audio files for background ambiance.
    *   Stream music directly from YouTube by providing a URL or searching for content.
    *   Includes a dedicated "Concentration Music" option.
    *   Offers media controls such as pause, volume adjustment, seeking, and repeat toggling.
*   **Inspirational Quotes:** Displays random, animated quotes to provide motivation and a pleasant aesthetic.
*   **Customizable Audio:** Adjust separate volume levels for background music and application sound effects.
*   **Persistent Progress:** Saves your tree's age, allowing it to continue growing across sessions.
*   **Notifications:** Provides on-screen notifications for various events and actions.

## Installation

To run `wisdom_tree.py`, you'll need Python 3, a terminal emulator that supports `curses`, and the VLC media player.

1.  **Install Python:** Ensure you have Python 3.x installed on your system.
2.  **Install VLC Media Player:** Download and install the [VLC media player](https://www.videolan.org/vlc/) application. This is a system-wide dependency required for audio playback.
3.  **Install Python Dependencies:** Install the necessary Python packages using pip:
    ```bash
    pip install python-vlc
    ```
    If you are on **Windows**, you will also need the `windows-curses` package:
    ```bash
    pip install windows-curses
    ```
4.  **Application Structure:** This script relies on other local Python modules and a `res` directory for assets. Place `wisdom_tree.py`, the `wisdom_tree` package (containing `audio.py`, `config.py`, `timer.py`, `tree.py`, `ui.py`, `utils.py`), and the `res` directory (containing `.ogg` files and a `treedata` subdirectory) in the same parent directory.

    *Example directory structure:*
    ```
    your_project_folder/
    ├── wisdom_tree.py
    ├── wisdom_tree/
    │   ├── __init__.py
    │   ├── audio.py
    │   ├── config.py
    │   ├── timer.py
    │   ├── tree.py
    │   ├── ui.py
    │   └── utils.py
    └── res/
        ├── treedata/
        │   └── tree_age.json  (created on first run)
        ├── growth_sound.ogg
        ├── timer_start.ogg
        └── music.ogg
    ```

## Usage

Navigate to the directory containing `wisdom_tree.py` in your terminal and run the script:

```bash
python wisdom_tree.py
```

### Controls

The application uses standard keyboard inputs for navigation and control:

| Key                      | Action                                                              |
| :----------------------- | :------------------------------------------------------------------ |
| `↑` / `k`                | Navigate menu up                                                    |
| `↓` / `j`                | Navigate menu down                                                  |
| `←` / `h` / `Esc`        | Navigate menu left / Close submenu                                  |
| `→` / `l`                | Navigate menu right                                                 |
| `Enter`                  | Select current menu item                                            |
| `q`                      | Save tree progress and exit the application                         |
| `Space`                  | Pause/unpause the entire application (including timer and media)    |
| `m`                      | Pause/unpause background music only                                 |
| `[`                      | Decrease media volume                                               |
| `]`                      | Increase media volume                                               |
| `{`                      | Decrease effect sounds volume                                       |
| `}`                      | Increase effect sounds volume                                       |
| `-`                      | Seek media backward by 10 seconds                                   |
| `=`                      | Seek media forward by 10 seconds                                    |
| `0` - `9`                | Jump to a specific percentage of the media (e.g., `5` for 50%)      |
| `r`                      | Toggle repeat/loop for media playback                               |
| `u`                      | Toggle all sound effects on/off                                     |

## Examples

1.  **Start the application:**
    ```bash
    python wisdom_tree.py
    ```
    The tree will appear, and background music (if available in `res`) will start playing.

2.  **Start a Pomodoro session:**
    *   Use `j` or `↓` to navigate to the "POMODORO TIMER" menu option.
    *   Press `Enter`.
    *   Select a timer duration (e.g., "25 MINUTES") using `j` or `↓` and press `Enter`.
    *   The timer will start counting down.

3.  **Play YouTube music:**
    *   Navigate to the "MEDIA" menu option and press `Enter`.
    *   Select "YouTube Music" and press `Enter`.
    *   Type a song title or YouTube URL into the input field that appears and press `Enter`. The application will start streaming the music.

4.  **Adjust volume:**
    *   Press `[` to decrease the current media volume.
    *   Press `}` to increase the application's sound effects volume. A notification will confirm the change.

## Limitations or Notes

*   This script requires a `curses`-compatible terminal environment. On Windows, this typically means using WSL2 or installing `windows-curses`.
*   A working installation of VLC Media Player is essential for all audio functionalities, including local file playback and YouTube streaming.
*   The script expects specific internal modules and a `res` directory with audio assets to be present alongside it for full functionality.
*   Background music starts playing immediately upon launching the application if local OGG files are found in the `res` directory.
