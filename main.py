import discord
import json
import aiohttp
import asyncio
import os

from pathlib import Path
from dotenv import load_dotenv

if Path(".env").exists():
    load_dotenv()
else:
    print("[!] .env doesn't exist! Please read the readme!")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

jellyfin = os.environ.get("JELLYFIN_ENDPOINT")
api_key = os.environ.get("JELLYFIN_API_KEY")


@client.event
async def on_ready():
    print(f'[*] JellyStatus')
    print(f'[*] Logged in as {client.user}!')

    async with aiohttp.ClientSession() as session:
        old_arr = {"Id": -1}
        send_id = os.environ.get("DISCORD_SEND_ID")

        while True:
            async with session.get(f'{jellyfin}/System/ActivityLog/Entries?api_key={api_key}') as res:
                j = await res.json()
                item = j['Items'][0]

                if item['Id'] != old_arr["Id"]:
                    if item['Type'] in ("VideoPlayback", "VideoPlaybackStopped"):
                        print(item)
                        user = client.get_user(send_id)
                        await user.send(item['Name'])

                    if item['Type'] == "VideoPlayback":
                        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=item['Name'].split(' is playing ')[1]))
                    elif item['Type'] == "VideoPlaybackStopped":
                        await client.change_presence(activity=None)

                old_arr = item
                await asyncio.sleep(2)

client.run(os.environ.get("TOKEN"))