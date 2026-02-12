# QR Code Scam Generator

## Overview
The QR Code Scam Generator is a Python script designed to automate the process of generating a QR code for Discord login. It utilizes Selenium for web automation and BeautifulSoup for HTML parsing. The generated QR code is then overlaid with a logo and combined with a template to create a final image.

**Developer:** NightfallGT  
**Note:** This script is intended for educational purposes only.

## Features
- Automatically retrieves a QR code from the Discord login page.
- Overlays a logo onto the QR code.
- Combines the QR code with a predefined template.
- Outputs a final image named `discord_gift.png`.
- Captures the Discord authentication token upon scanning the QR code.

## Installation
To run this script, you need to have Python installed along with the following packages:
- `selenium`
- `beautifulsoup4`
- `Pillow`

You can install the required packages using pip:

```bash
pip install selenium beautifulsoup4 Pillow
```

Additionally, ensure you have the Chrome WebDriver (`chromedriver.exe`) in the same directory as the script or specify its path in the code.

## Usage
1. Clone or download the script.
2. Create a `temp` directory in the same location as the script to store temporary images.
3. Place your overlay image in the `temp` directory and name it `overlay.png`.
4. Run the script:

```bash
python QR_Generator.py
```

## Examples
After running the script, you will see output indicating the progress:
```
- Page loaded.
- QR Code has been generated. > discord_gift.png
Send the QR Code to user and scan. Waiting..
Grabbing token..
Token grabbed: <token_value>
Task complete.
```

The final QR code image will be saved as `discord_gift.png` in the current directory.

## Limitations or Notes
- Ensure that you have the correct version of Chrome installed that matches your ChromeDriver version.
- The script requires a stable internet connection to access the Discord login page.
- The script may not work if Discord changes its HTML structure or QR code generation process.
- Use responsibly and ethically; unauthorized access to accounts is illegal.
