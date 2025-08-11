# 🎵 Discord Soundboard Bot

This Discord bot automatically plays a custom sound when a **specific user** joins a voice channel, followed by a final "last sound" clip.

## ✨ Features

* Plays a predefined sound file when a target user joins a voice channel.
* Waits 1.5 seconds before starting playback for better timing.
* Plays a final sound after the first one finishes.
* Automatically joins or moves to the correct channel.
* Adjustable volume for playback.
* Disconnects from the channel after playing sounds.

## 📦 Requirements

* Python 3.8+
* [discord.py](https://pypi.org/project/discord.py/)
* FFmpeg installed and available in system PATH

Install dependencies:

```bash
pip install discord.py
```

Make sure FFmpeg is installed:

* [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.

## ⚙️ Configuration

Edit the following variables in the script:

```python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"          # Your bot token from Discord Developer Portal
SOUND_FILE = "1380208997826695320.ogg"    # First sound file path
LAST_SOUND_FILE = "1342180479289266186.ogg" # Final sound file path
TARGET_USER_ID = 123456789012345678       # Discord user ID to trigger the bot
```

**Important:**

* Enable the **Server Members Intent** in your bot’s settings in the Discord Developer Portal.
* Ensure the sound files are in `.ogg` or `.wav` format.

## 🚀 Usage

1. Invite the bot to your server with **Voice Channel Connect** and **Speak** permissions.
2. Run the bot:

```bash
python bot.py
```

3. When the target user joins a voice channel:

   * Bot connects to that channel
   * Plays the first sound file
   * Plays the last sound file
   * Disconnects automatically

## 🛠 Notes

* If the bot is already in a voice channel, it will move to the target user’s channel instead of reconnecting.
* The bot ignores all other users except the one with the `TARGET_USER_ID`.
