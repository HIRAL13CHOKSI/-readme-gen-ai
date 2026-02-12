# QR Code Scam Generator

## Overview
The QR Code Scam Generator is a Python script designed to generate a QR code for Discord login and overlay it with a custom template. This tool is intended for educational purposes only.

## Features
- Generates a QR code for Discord login.
- Overlays a custom logo on the generated QR code.
- Combines the QR code with a template image to create a final output.
- Extracts the Discord token from the user's session after scanning the QR code.

## Installation
To run this script, you need to have Python installed on your machine along with the following packages:
- `selenium`
- `Pillow`
- `beautifulsoup4`

You can install the required packages using pip:

```bash
pip install selenium Pillow beautifulsoup4
```

Additionally, ensure that you have the Chrome WebDriver (`chromedriver.exe`) in the same directory as the script or specify its path in the script.

## Usage
1. Clone or download the repository containing the script.
2. Ensure you have the necessary images:
   - `temp/qr_code.png` (will be generated)
   - `temp/overlay.png` (your custom logo)
   - `temp/template.png` (your template image)
3. Run the script:

```bash
python QR_Generator.py
```

## Examples
1. **Running the Script**: 
   After executing the script, it will automatically open Discord's login page in a Chrome browser window. 

2. **Output**: 
   Once the QR code is generated and the user scans it, the script will wait for the user to log in and will then extract the Discord token.

## Limitations or Notes
- This script is intended for educational purposes only and should not be used for malicious activities.
- Ensure that you have the necessary permissions to use the images and that you comply with Discord's terms of service.
- The script requires a stable internet connection to load the Discord login page.
- The script may not work if Discord changes its web structure or if the QR code element's class name changes.
