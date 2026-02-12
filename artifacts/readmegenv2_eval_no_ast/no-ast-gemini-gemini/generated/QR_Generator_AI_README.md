This README documents the `QR_Generator.py` script, a utility designed to create a custom Discord QR code image that, when scanned by a user, can capture their authentication token.

---

# QR_Generator.py

## Overview

This Python script generates a deceptive Discord gift image containing a live Discord login QR code. The purpose is to entice a user to scan the QR code, which logs them into Discord via the script's controlled browser instance. Once a successful login is detected, the script extracts and displays the user's authentication token.

The script incorporates custom overlay and template images to create a convincing fake Discord gift.

## Features

*   **Discord QR Code Generation**: Fetches a live Discord login QR code from the official Discord website.
*   **Image Manipulation**: Embeds the generated QR code into a predefined template image, adding an overlay logo.
*   **Token Grabbing**: Monitors the browser session for a successful login and extracts the user's authentication token using JavaScript injection.
*   **Automated Browser Interaction**: Uses Selenium to automate browser navigation and page element interaction.

## Installation

1.  **Python**: Ensure you have Python 3.x installed.
2.  **Dependencies**: Install the required Python libraries using pip:
    ```bash
    pip install beautifulsoup4 selenium pillow lxml
    ```
    *(Note: `lxml` is a dependency of `beautifulsoup4` for the `html.parser` or `lxml` features)*
3.  **ChromeDriver**:
    *   Download the appropriate `chromedriver.exe` for your Chrome browser version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
    *   Place `chromedriver.exe` in the same directory as the `QR_Generator.py` script.
4.  **Required Image Assets**:
    *   Create a directory named `temp` in the same location as the script.
    *   Place two image files inside the `temp` directory:
        *   `overlay.png`: A small image (e.g., a Discord logo) to be placed over the QR code.
        *   `template.png`: The background image for the fake Discord gift, onto which the QR code will be pasted.

    Your directory structure should look like this:
    ```
    .
    ├── QR_Generator.py
    ├── chromedriver.exe
    └── temp/
        ├── overlay.png
        └── template.png
    ```

## Usage

1.  **Run the script**:
    ```bash
    python QR_Generator.py
    ```
2.  **Browser Launch**: A Chrome browser window will open automatically, navigating to the Discord login page.
3.  **QR Code Generation**: After a short delay, the script will capture the QR code from the browser, process it with your provided `overlay.png` and `template.png`, and save the final image as `discord_gift.png` in the script's root directory.
4.  **Waiting for Scan**: The script will then print "Send the QR Code to user and scan. Waiting.." and pause. It continuously monitors the opened Chrome window.
5.  **Token Retrieval**: If a user scans the `discord_gift.png` using their Discord mobile app and approves the login, the script's browser window will redirect. Upon detection of this redirection, the script will execute JavaScript to retrieve and display the user's Discord authentication token.
6.  **Completion**: The script will print "Task complete." and exit after retrieving the token.

## Examples

The script will produce a file named `discord_gift.png` that looks like a Discord gift card, containing the QR code.

When a user scans this QR code, and after successful authentication, the console output will resemble:

```
github.com/NightfallGT/Discord-QR-Scam

** QR Code Scam Generator **
- Page loaded.
- QR Code has been generated. > discord_gift.png
Send the QR Code to user and scan. Waiting..
Grabbing token..
---
Token grabbed: <USER_DISCORD_AUTHENTICATION_TOKEN_HERE>
Task complete.
```

## Limitations or Notes

*   **Purpose**: As noted in the source code ("Educational purposes only", "QR Code Scam Generator"), this script demonstrates a method for token theft. It is provided for educational and security awareness purposes.
*   **External Assets**: The script relies on the presence of `chromedriver.exe`, `temp/overlay.png`, and `temp/template.png` for proper functionality. Ensure these are correctly set up as per the Installation section.
*   **Discord UI Changes**: The script uses specific CSS class names (`qrCode-wG6ZgU`) and JavaScript structures (`webpackJsonp`) to interact with Discord's login page and extract the token. Future updates to Discord's website might break these elements, requiring modifications to the script.
*   **Browser Control**: The script maintains control of the opened Chrome browser instance until the token is grabbed or the script is manually terminated.
