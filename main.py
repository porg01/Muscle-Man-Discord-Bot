import discord
import random
from verbs import verb_check
import os

token = os.environ.get('TOKEN')

if not token:
    raise ValueError("TOKEN environment variable not set")

intents = discord.Intents.default()
intents.messages = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} in da house bois')


@client.event
async def on_message(message):
    if message.author != client.user:
        content = message.content
        check, output = verb_check(content)
        if random.choice([check, 0]):                  # 1 in 2 chance of occurring
            if check:
                await message.channel.send(f"you know who else {output}? MY MOM!")

client.run(token)
