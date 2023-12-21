import os, discord, random, asyncio, openai

from dotenv import load_dotenv

import utils.input as input
from classes.ai import AI

load_dotenv()

client = discord.Client()

user_ai_dict = {}

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.guild is None and message.author.name != client.user.name: #Modify this to accept server
        if not user_ai_dict.get(message.author.id):
            ai = AI(message.author.id, input.remove_discord_emote_and_emoji(message.author.name))
            user_ai_dict[message.author.id] = ai

        ai_object = user_ai_dict.get(message.author.id)
        answer = ai_object.chat_with_ai(message.content)

        delay = random.randint(2, 4)
        await asyncio.sleep(delay)

        async with message.channel.typing():
            delay = random.randint(3, 7)
            await asyncio.sleep(delay)
            await message.channel.send(answer)

openai.api_key = os.getenv("OPENAI_API_KEY")
client.run(os.getenv("DISCORD_TOKEN"))