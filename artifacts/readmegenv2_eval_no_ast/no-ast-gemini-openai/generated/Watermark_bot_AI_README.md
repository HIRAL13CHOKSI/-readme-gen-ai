```markdown
# Telegram Video Watermark Adder Bot

## Overview

This Python script implements a Telegram bot that adds watermarks to videos. Users can send videos to the bot, and it will add a user-specified watermark image at a configurable position and size. The bot offers settings for watermark customization and handles video downloading, watermark application, and uploading the watermarked video back to the user. It also includes basic error handling and logging.

## Features

- **Watermark Addition:** Adds a user-provided image as a watermark to videos.
- **Customizable Watermark:**
    - **Position:** Users can set the watermark position to Top Left, Top Right, Bottom Left, or Bottom Right.
    - **Size:** Users can choose the watermark size as a percentage (5%, 7%, 10%, 15%, 20%, 25%, 30%, 35%, 40%, 45%).
- **Settings Persistence:** Remembers user-defined watermark settings.
- **Video Downloading and Uploading:** Handles downloading videos from Telegram and uploading the watermarked videos.
- **Streamtape Upload (Optional):**  If enabled via config, large files can be uploaded to Streamtape.
- **Basic Error Handling:** Catches common errors during video processing.
- **Logging:** Logs bot activities and errors to a specified channel.
- **Force Subscribe:** Requires users to subscribe to a specified channel before using the bot.
- **Broadcast:** Allows the owner to broadcast messages to all users.
- **Ban User:** Allows banning a user from the updates channel.

## Installation

1.  **Install Dependencies:**

    Since the script relies on external libraries, you must install them before running the bot. A likely set of commands to do so is:

    ```bash
    pip install pyrogram pillow aiohttp
    pip install hachoir_core
    pip install hachoir_parser
    pip install hachoir_metadata
    pip install ffmpeg-python
    ```

2.  **Configuration:**

    You will need to configure the bot with your Telegram API credentials, bot token, and other settings.  These are expected to be set in a `configs.py` file. The following configuration parameters are likely required:

    -   `API_ID`: Your Telegram API ID.
    -   `API_HASH`: Your Telegram API HASH.
    -   `BOT_TOKEN`: Your Telegram bot token.
    -   `BOT_USERNAME`: Your Telegram bot username.
    -   `OWNER_ID`: Your Telegram user ID.
    -   `LOG_CHANNEL`: The Telegram channel ID for logging.
    -   `UPDATES_CHANNEL`: The Telegram channel ID for force subscribe (optional).
    -   `DOWN_PATH`: The directory for downloading files (e.g., "downloads").
    -   `PRESET`: FFmpeg preset (e.g., "ultrafast").
    -   `USAGE_WATERMARK_ADDER`: A formatted string containing instructions for the user
    -   `ALLOW_UPLOAD_TO_STREAMTAPE`: Boolean to enable Streamtape uploads.
    -   `STREAMTAPE_API_USERNAME`: Streamtape API username
    -   `STREAMTAPE_API_PASS`: Streamtape API password

    Create a `configs.py` file with the necessary variables:

    ```python
    class Config(object):
        API_ID = 12345  # Replace with your API ID
        API_HASH = "YOUR_API_HASH"  # Replace with your API HASH
        BOT_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot token
        BOT_USERNAME = "YourBotUsername" # Replace with your bot username
        OWNER_ID = 67890  # Replace with your Telegram user ID
        LOG_CHANNEL = -100123456789  # Replace with your log channel ID
        UPDATES_CHANNEL = -100987654321 # Replace with your updates channel ID
        DOWN_PATH = "downloads"
        PRESET = "ultrafast"
        USAGE_WATERMARK_ADDER = "This is how to use the bot"
        ALLOW_UPLOAD_TO_STREAMTAPE = False
        STREAMTAPE_API_USERNAME = "NoNeed"
        STREAMTAPE_API_PASS = "NoNeed"
    ```

## Usage

1.  **Start the Bot:**

    Run the Python script:

    ```bash
    python Watermark_bot.py
    ```

2.  **Interact with the Bot on Telegram:**

    -   Send the `/start` or `/help` command to the bot to get usage instructions.
    -   Send a JPG or PNG image to set it as the watermark.
    -   Send a video file to the bot.  The bot will add the selected watermark to the video using the current settings.
    -   Use the `/settings` command to adjust watermark position and size.
    -   Use the `/status` command to check bot status.
    -   Use the `/cancel` command (owner only) to cancel the current process.

## Examples

1.  **Setting a Watermark:**

    Send a `.jpg` or `.png` image to the bot.  The bot will confirm that it is saved as the watermark.

2.  **Adding Watermark to a Video:**

    Send a video file to the bot. The bot will process the video and send back the watermarked version.

3.  **Changing Watermark Settings:**

    Send the `/settings` command.  Use the inline keyboard to change the position and size of the watermark.

## Limitations or Notes

- The script requires a correctly configured `configs.py` file with valid API credentials.
-  The script uses `hachoir` for video metadata extraction, so it might fail if the library encounters an unexpected video format.
- Error handling is basic; the bot might fail silently in some cases.
- Streamtape upload is optional and requires a Streamtape account and API credentials.
- The bot stores the watermark image and downloaded video files locally. Consider implementing cleanup mechanisms to manage disk space.
- The bot's performance depends on the server's resources and the video's size and complexity.
- Rate limiting may occur if sending too many requests to Telegram servers.
- The force subscribe feature requires the bot to be an administrator in the updates channel.
```
