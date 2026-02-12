This README provides an overview and instructions for the `Watermark_bot.py` script, a Telegram bot designed to add custom watermarks to videos.

# Telegram Video Watermark Adder Bot

## Overview
This Python script implements a Telegram bot that allows users to apply custom image watermarks to their videos. Users can upload an image to be used as a watermark, configure its position and size, and then send videos to the bot for watermarking. The bot processes the videos, adds the watermark, and sends the watermarked video back to the user. It also includes administrative features and support for uploading large files to Streamtape.

## Features
*   **Custom Watermarks**: Users can upload any JPG or PNG image to set as their personalized watermark.
*   **Video Watermarking**: Automatically adds the set watermark to videos sent by users.
*   **Configurable Watermark Settings**:
    *   **Position**: Choose from Top Left, Top Right, Bottom Left, or Bottom Right corners.
    *   **Size**: Adjust the watermark size as a percentage (from 5% to 45%) relative to the video dimensions.
*   **Progress Updates**: Provides real-time download and processing progress within Telegram.
*   **Large File Support**: Configurable to upload large watermarked videos (over 2GB) to Streamtape.
*   **User Management**: Tracks new users and logs bot activity.
*   **Force Subscribe**: Can be configured to require users to join a specific Telegram channel before using the bot.
*   **Admin Controls**: Includes commands for broadcasting messages to all users, checking bot status, and cancelling ongoing watermarking tasks (owner-specific).

## Installation

### Prerequisites
*   **Python 3.x**: Ensure Python 3.6 or higher is installed.
*   **ffmpeg**: An external video processing tool is required. Install `ffmpeg` on your system and ensure it's accessible in your system's PATH. This is crucial for video processing and watermarking.

### Python Dependencies
Install the necessary Python libraries using pip:
```bash
pip install pyrogram Pillow aiohttp hachoir
```

### Configuration
The bot requires several configuration values to operate, which are typically loaded from environment variables or a `configs.py` file (not included in this script). You will need to set up the following:

*   **Telegram Bot API Credentials**:
    *   `BOT_TOKEN`: Obtain this from [@BotFather](https://t.me/BotFather).
    *   `API_ID`: Get your API ID from [my.telegram.org](https://my.telegram.org/).
    *   `API_HASH`: Get your API Hash from [my.telegram.org](https://my.telegram.org/).
    *   `BOT_USERNAME`: Your bot's username (without the '@').
*   **Admin & Channel IDs**:
    *   `OWNER_ID`: Your Telegram User ID (a numerical ID) for administrative commands.
    *   `LOG_CHANNEL`: The Telegram channel ID (e.g., `-1001234567890`) where the bot will send logs and activity updates.
    *   `UPDATES_CHANNEL`: (Optional) The Telegram channel ID for the force-subscribe feature. If set, users must join this channel to use the bot.
*   **File Paths & FFmpeg Settings**:
    *   `DOWN_PATH`: A path on your server where the bot can store temporary files, downloads, and watermarks (e.g., `./downloads`).
    *   `PRESET`: FFmpeg preset for video encoding quality (e.g., `ultrafast`, `superfast`, `fast`, `medium`, `slow`).
*   **Streamtape Integration (Optional)**:
    *   `ALLOW_UPLOAD_TO_STREAMTAPE`: Set to `True` or `False`. If `True`, enables uploading large files to Streamtape.
    *   `STREAMTAPE_API_USERNAME`: Your Streamtape API username.
    *   `STREAMTAPE_API_PASS`: Your Streamtape API password.

### Running the Bot
Once all dependencies are installed and configuration variables are set, you can start the bot:
```bash
python Watermark_bot.py
```

## Usage

Interact with the bot on Telegram using the following commands and workflow:

1.  **Start the Bot**:
    Send `/start` or `/help` to your bot to receive a welcome message and initial instructions.

2.  **Set Your Watermark Image**:
    Send a **JPG** or **PNG** image file directly to the bot. This image will be saved as your personal watermark for all subsequent video processing.

3.  **Configure Watermark Settings**:
    Use the `/settings` command to open an interactive menu with inline buttons:
    *   **Position**: Choose one of the four corners: `Top Left`, `Top Right`, `Bottom Left`, `Bottom Right`.
    *   **Size**: Select a percentage value (5%, 7%, 10%, 15%, 20%, 25%, 30%, 35%, 40%, 45%) to control the watermark's size relative to the video.

4.  **Add Watermark to a Video**:
    After setting your watermark image and configuring its position/size, simply send any video file to the bot. The bot will download the video, apply your customized watermark, and then upload the watermarked video back to you.

### Admin Commands (for the `OWNER_ID` only)
*   `/cancel`: Stops any currently ongoing video watermarking or processing tasks.
*   `/broadcast [reply to message]`: To broadcast a message, reply to any message with `/broadcast`. The bot will forward that message to all its users.
*   `/status`: Checks the bot's current operational status and displays the total number of users in its database.

## Examples

1.  **Setting a Watermark Image**:
    Send your preferred `.jpg` or `.png` logo directly to the bot. The bot will confirm that it has saved your watermark.

2.  **Changing Watermark Position**:
    Type `/settings`, then click the "Set Bottom Right" button in the menu. The bot will update your preference.

3.  **Watermarking a Video**:
    Send a video file to the bot. The bot will respond with progress messages ("Downloading Video...", "Trying to Add Watermark...", "Watermark Added Successfully! Trying to Upload..."), and then deliver the watermarked video.

## Notes
*   Ensure that `ffmpeg` is correctly installed and its executable is found in your system's PATH for the bot to function properly.
*   This bot heavily relies on Telegram API. Ensure your `API_ID`, `API_HASH`, and `BOT_TOKEN` are correct.
*   If `ALLOW_UPLOAD_TO_STREAMTAPE` is `True`, ensure your Streamtape API credentials are valid, as this is used for uploading videos larger than Telegram's 2GB limit.
