# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.command(name='quote', help='Responds with a random quote')
async def quote(ctx):
    quotes = [
        '1',
        '2'
    ]

    response = random.choice(quotes)
    await ctx.send(response)


@bot.command(name='teste')
@commands.has_role('♕ Sangue Real')
async def teste(ctx):
    await ctx.send('olá membro do sangue real',)


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


bot.run(token)
