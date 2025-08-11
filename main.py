import discord
from discord.ext import commands
import asyncio

TOKEN = ""          # Replace with your bot token
SOUND_FILE = "1380208997826695320.ogg"         # or .wav
LAST_SOUND_FILE = "1342180479289266186.ogg"
TARGET_USER_ID = 0  # <-- Only this user triggers the bot

intents = discord.Intents.default()
intents.voice_states = True        # needed for voice updates
intents.guilds = True
intents.members = True             # make sure "Server Members Intent" is enabled in Dev Portal

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    # Only react for the target user (and ignore bots)
    if member.bot or member.id != TARGET_USER_ID:
        return

    # Trigger only when they actually join or move to a new channel
    if after.channel is not None and before.channel != after.channel:
        channel = after.channel
        print(f"{member} joined {channel.name}")

        # Wait 1.5 seconds before playing
        await asyncio.sleep(1.5)

        vc = member.guild.voice_client
        try:
            if vc and vc.is_connected():
                if vc.channel.id != channel.id:
                    await vc.move_to(channel)
            else:
                vc = await channel.connect()

            # Play the sound for each user in the channel (excluding bots)
            for user in channel.members:
                if user.bot:
                    continue
                # Play sound at 50% volume
                audio = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(SOUND_FILE), volume=0.5)
                if vc.is_connected():
                    vc.play(audio)
                    while vc.is_playing():
                        await asyncio.sleep(0.5)

            # Play last sound if still connected
            if vc.is_connected():
                audio = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(LAST_SOUND_FILE), volume=0.5)
                vc.play(audio)
                while vc.is_playing():
                    await asyncio.sleep(0.5)

        except discord.errors.ClientException as e:
            print(f"Voice client error: {e}")
        finally:
            if member.guild.voice_client and member.guild.voice_client.is_connected():
                await member.guild.voice_client.disconnect()

bot.run(TOKEN)
