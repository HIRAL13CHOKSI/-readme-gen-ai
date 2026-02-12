# Watermark Bot

## Overview
Watermark Bot is a Telegram bot designed to add watermarks to videos. Users can customize the watermark's position and size, and the bot supports various media formats. The bot operates in a private chat and requires users to subscribe to an updates channel to access its features.

## Features
- Add customizable watermarks to videos.
- Set watermark position (Top Left, Top Right, Bottom Left, Bottom Right).
- Adjust watermark size (5% to 45%).
- User management and logging.
- Support for multiple media formats (images and videos).
- Integration with a logging channel for activity tracking.

## Installation
To run the Watermark Bot, you need to have Python installed along with the required dependencies. Follow these steps:

1. **Clone the repository** (if applicable) or download the script.
2. **Install the required packages**:
   ```bash
   pip install pyrogram hachoir Pillow aiohttp
   ```
3. **Set up your Telegram bot**:
   - Create a new bot using [BotFather](https://t.me/botfather) on Telegram.
   - Obtain your bot token and API credentials (API ID and API Hash).

4. **Configure the bot**:
   - Update the `configs.py` file with your bot token, API ID, API Hash, and other necessary configurations.

## Usage
To start using the Watermark Bot, follow these steps:

1. **Start the bot** by sending the `/start` command in a private chat.
2. **Set your watermark** by sending an image (JPG or PNG) that will be used as the watermark.
3. **Send a video** to the bot to add the watermark.

### Example Commands
- `/start` - Start the bot and get help.
- `/help` - Get usage instructions.
- `/settings` - Configure watermark position and size.
- `/cancel` - Stop the watermarking process (admin only).
- `/broadcast` - Send a message to all users (admin only).
- `/status` - Check the bot's current status.

## Examples
1. **Set Watermark**: Send an image to the bot to set it as the watermark.
2. **Add Watermark to Video**: Send a video file after setting the watermark, and the bot will process it and send back the watermarked video.

## Limitations or Notes
- The bot requires users to join a specified updates channel to access its features.
- Ensure that the watermark image is in JPG or PNG format.
- The bot may experience delays if it is busy processing other requests.
- The bot's functionality is dependent on the correct configuration of the `configs.py` file.
- If you encounter a `ModuleNotFoundError` for `hachoir`, ensure that all required libraries are installed.

## Support
For support or to report issues, please contact the developer or join the support group linked in the bot's responses.
