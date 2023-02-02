import discord
import json
import aiohttp
import asyncio


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

jellyfin = 'https://localhost:8096'
api_key = ''#input your apikey here


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    async with aiohttp.ClientSession() as session:
        old_arr = {"Id": -1}
        send_id = #put id here

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


@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run(
    '') #put your discord token here




    #Made by Waffle with help from nebula#5555