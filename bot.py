# bot.py
import os
import random
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

quotes_path = os.getenv('QUOTES_PATH')

with open(quotes_path, encoding='utf-8') as f:
    quotes = json.load(f)



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


@bot.command()
@commands.has_any_role('♕ Sangue Real','Humanos')
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))



@bot.command(name='quote', help='Responds with a random quote')
async def quote(ctx):

    author, quote = random.choice(list(quotes.items()))

    response = '"{}"\n- {}'.format(quote, author)
    await ctx.send(response)



@bot.command(name='addquote', help='Adds quote')
async def addquote(ctx):

    # TODO juntar quote

    with open(quotes_path, 'w', encoding='utf-8') as json_file:
        json.dump(quotes, json_file)

    response = '"{}"\n- {}'.format(quote, author)
    await ctx.send(response)




bot.run(token)
