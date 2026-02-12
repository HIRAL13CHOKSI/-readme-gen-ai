```markdown
# Wisdom Tree

## Overview

Wisdom Tree is a terminal-based application that combines a Pomodoro timer, a tree growth visualization, quote display, and media player functionality to encourage focus and productivity. The application uses the `curses` library to provide a text-based user interface. Due to the error during analysis, curses may not be available in the users environment. If not please install curses before using.

## Features

-   **Tree Visualization:** Displays a growing tree that symbolizes progress. The tree grows gradually over time and with completed Pomodoro sessions.
-   **Pomodoro Timer:** Integrated Pomodoro timer to help users manage their work and break intervals.
-   **Quote Display:** Shows a randomly selected quote to provide inspiration.
-   **Media Player:** Plays local audio files or streams audio from YouTube. Supports pausing, seeking, and volume control.
-   **Menu System:** Uses a menu-driven interface for easy navigation and control of application features.
-   **Notifications:** Displays on-screen notifications for various events, such as timer updates, volume changes, and repeat status.

## Installation

1.  Ensure you have Python 3 installed.
2.  Due to the error during analysis, curses may not be available in the users environment. If not please install curses before using.

    ```bash
    pip install windows-curses
    ```
3.  No additional steps are required. The script is self-contained.

## Usage

1.  Save the Python script (`wisdom_tree.py`) to a directory.
2.  Run the script from your terminal:

    ```bash
    python wisdom_tree.py
    ```

## Controls

-   **Navigation:** Use the arrow keys (Up, Down, Left, Right) or `k`, `j`, `h`, `l` keys to navigate the menu. `Esc` can also be used for left navigation.
-   **Selection:** Press `Enter` to select a menu item.
-   **Pomodoro Timer:**
    -   Select "POMODORO TIMER" from the menu to start a timer.
    -   Use the sub-menu to select the desired timer length.
-   **Media Player:**
    -   Select "MEDIA" from the menu to control the media player.
    -   `0`: Play YouTube Music.
    -   `1`: Play Concentration Music.
    -   Enter a YouTube URL to play music from YouTube.
-   **Playback Controls:**
    -   `Space`: Pause/Resume.
    -   `m`: Pause music.
    -   `]`: Increase volume.
    -   `[`: Decrease volume.
    -   `=`: Seek forward 10 seconds.
    -   `-`: Seek backward 10 seconds.
    -   `r`: Toggle repeat.
    -   `0-9`: Seek to position (0-100%).
-   **Sound Effects:**
    -   `u`: Toggle sound effects on/off.
    -   `}`: Increase effect volume.
    -   `{`: Decrease effect volume.
-   **Other:**
    -   `q`: Quit the application (saves tree age).

## Examples

1.  **Starting a Pomodoro Timer:**

    -   Run the script: `python wisdom_tree.py`
    -   Use the arrow keys to navigate to "POMODORO TIMER" and press `Enter`.
    -   Select a timer duration and press `Enter`.

2.  **Playing Music from YouTube:**

    -   Run the script: `python wisdom_tree.py`
    -   Use the arrow keys to navigate to "MEDIA" and press `Enter`.
    -   Select `YouTube Music`
    -   Enter a YouTube URL in the input box and press `Enter`.

## Limitations or Notes

-   The application requires a terminal environment that supports `curses`.
-   The application saves tree age data to `RES_FOLDER / "treedata"`.
-   YouTube playback requires a stable internet connection.
-   The application relies on specific files (OGG audio files, quote file) within the `RES_FOLDER`. Ensure these files are present for full functionality. The application assumes RES_FOLDER is structured correctly
-   Error analysis indicates potential issues with the curses library, ensure it is properly installed in your environment.
