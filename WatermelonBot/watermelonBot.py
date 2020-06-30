import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

def randomImage():
    folder = "C:/Users/Owner/Desktop/WatermelonBot"
    x = random.choice(os.listdir(folder))
    if str(x)[0] != 'w':
        x = 'watermelon1.jpg'
    return str(x)


@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "watermelon" in message.content:
        picture = randomImage()
        await message.channel.send(file = discord.File(picture))

client.run('your bot token here')



