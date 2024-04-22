import discord
import json
import os
from dotenv import load_dotenv
import character_formatter as form
import character_creator as cc


load_dotenv()
TOKEN = os.environ.get("PROJECT_ZOMBOID_BOT_TOKEN")
file_path = os.environ.get("ZOMBOID_BOT_PATH")

negative_array = []
positive_array = []
with open(file_path, 'r') as json_file:
    zomboid = json.load(json_file)





intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Event handler for when the bot has logged in
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!zom_rand'):
        character = cc.character_creator()
        await message.channel.send(f'Hello {message.author.name}! Here is your new random character\'s stats:')
        await message.channel.send(form.format_character_info(character))


client.run(TOKEN)
