# JellyStatus

A watch status and DM for your Jellyfin server on Discord.

# Setup

1. Clone this repo with `git clone https://github.com/LiveWaffle/JellyStatus`
2. Copy `.env.example` to `.env`
3. In `.env`, change the variables
    - `TOKEN` should be your [Discord bot token](https://discord.com/developers/applications)
        - You must share a server with this bot; you can invite it on the oauth page (bot scope)
    - `DISCORD_SEND_ID` should be your [Discord ID](https://bit.ly/discordid)
    - `JELLYFIN_ENDPOINT` should be the URL to your Jellyfin server, usually localhost
    - `JELLYFIN_API_KEY` should be a unique API key generated from the Jellyfin dashboard
4. Install requirements with `pip install -r requirements.txt`
5. Start bot with `python main.py`

# Credits

- [LiveWaffle](https://github.com/LiveWaffle) for idea
- [Nebula](https://github.com/itsnebulalol) for most bot code
