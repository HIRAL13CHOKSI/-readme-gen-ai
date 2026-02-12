```markdown
# Watermark Bot

## Overview
Watermark Bot is a Telegram bot designed to add watermarks to videos. Users can customize the position and size of the watermark and easily manage their settings through a user-friendly interface.

## Features
- Add watermarks to videos sent to the bot.
- Customize watermark position (Top Left, Top Right, Bottom Left, Bottom Right).
- Adjust watermark size (5% to 45%).
- User management and logging.
- Broadcast messages to users.
- Check the bot's status.

## Installation
To run the Watermark Bot, ensure you have Python installed along with the required dependencies. You can install the necessary packages using pip:

```bash
pip install pyrogram hachoir pillow aiohttp
```

Make sure to set up your Telegram bot and replace the configuration values in the `configs.py` file with your bot's credentials.

## Usage
1. Start the bot by sending the `/start` command in a private chat.
2. Send an image to set it as a watermark.
3. Send a video to add the watermark to it.
4. Use the `/settings` command to adjust the watermark position and size.

### Example Commands
- `/start`: Start the bot and receive help.
- `/help`: Get usage instructions.
- `/settings`: Access watermark settings.
- `/cancel`: Stop the current watermarking process (owner only).
- `/broadcast`: Send a message to all users (owner only).
- `/status`: Check the bot's current status.

## Examples
1. **Set Watermark**: Send an image to the bot to set it as a watermark.
2. **Add Watermark to Video**: Send a video file after setting the watermark to add it to the video.
3. **Change Settings**: Use the `/settings` command to change the watermark position or size.

## Limitations or Notes
- The bot requires users to join a specified updates channel to use its features.
- Ensure that the watermark image is in JPG or PNG format.
- The bot may not handle large video files well; consider file size limits when uploading.
- The bot's functionality is dependent on external libraries, ensure they are installed correctly.

For any issues or feature requests, please contact the developer through the support group linked in the bot's messages.
```
