**Discord QR Code Scam Generator**
=====================================

**Description**
---------------

This Python script is designed to generate a Discord QR code scam, which can be used to steal a user's Discord token. The script uses Selenium to navigate to the Discord login page, extract the QR code, and then use OpenCV to generate a new image with the QR code embedded. The script then waits for the user to scan the QR code, at which point it will execute JavaScript to grab the user's token.

**Usage**
---------

1. Make sure you have the following dependencies installed:
	* `beautifulsoup4`
	* `selenium`
	* `Pillow`
	* `base64`
	* `chromedriver` (for Selenium)
2. Place the `chromedriver.exe` file in the same directory as the script.
3. Run the script using Python (e.g. `python discord_qr_scam.py`).
4. The script will open a Chrome browser window and navigate to the Discord login page.
5. The script will wait for the user to scan the QR code, at which point it will grab the user's token.

**Dependencies**
----------------

* `beautifulsoup4` (for parsing HTML)
* `selenium` (for automating Chrome browser)
* `Pillow` (for image processing)
* `base64` (for base64 decoding)
* `chromedriver` (for Selenium)

**Note**
--------

This script is for educational purposes only and should not be used to steal Discord tokens without the user's consent.