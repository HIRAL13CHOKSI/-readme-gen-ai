```markdown
# Discord QR Code Generator

## Overview

This script automates the process of generating a Discord login QR code, overlaying it with a logo, and placing it on a template image. The script uses Selenium to navigate to the Discord login page, extracts the QR code, and then monitors the page for a successful login to extract the user's token.

**Warning:** This script is intended for educational purposes only. Using it to generate QR codes for malicious purposes is unethical and potentially illegal.

## Features

- Generates a Discord login QR code using Selenium.
- Overlays a logo onto the QR code.
- Pastes the modified QR code onto a template image.
- Automatically extracts the Discord token after the QR code is scanned and login is complete.

## Installation

1.  **Install Python:** Ensure you have Python 3 installed on your system.
2.  **Install required libraries:**
    ```bash
    pip install beautifulsoup4 selenium Pillow
    ```
3.  **Download ChromeDriver:** Download the ChromeDriver executable that is compatible with your Chrome browser version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and place it in the same directory as the script, or ensure it's accessible via your system's PATH environment variable. Rename it to `chromedriver.exe` if necessary.
4.  **Prepare images:** Place `overlay.png` and `template.png` in a newly created `temp` folder in the script's directory.

## Usage

1.  **Run the script:**
    ```bash
    python QR_Generator.py
    ```
2.  The script will open a Chrome window and navigate to the Discord login page.
3.  It will generate `discord_gift.png` in the script's directory, which contains the QR code.
4.  Send the `discord_gift.png` image to the target user.
5.  Once the QR code is scanned and the user logs in, the script will automatically extract and print the Discord token. The Chrome window will remain open. You can close it once the script is finished.

## Examples

After running the script, the `discord_gift.png` file will be generated. This file contains the QR code that can be sent to a user.  The script will output the user's token to the console upon successful login.

## Limitations or Notes

-   The script requires ChromeDriver to be installed and accessible.  Ensure the `chromedriver.exe` path in the script is correct.
-   The script relies on specific HTML elements and JavaScript code on the Discord login page.  Changes to the Discord website may break the script.
-   The `overlay.png` and `template.png` files are expected to be in a `temp` folder within the script's directory. These files are not included and must be provided separately.
-   Error handling is minimal. The script might crash if it encounters unexpected issues.
-   The script uses a `time.sleep(5)` to wait for the page to load. This delay may need to be adjusted based on your internet connection speed.
```
