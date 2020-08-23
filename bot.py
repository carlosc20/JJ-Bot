# bot.py
import os
import random
import json

import discord
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
    print('Logged in as ', bot.user.name, ', id: ', bot.user.id)
    print('-----------------------------------------------------')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.command()
@commands.has_any_role('♕ Sangue Real','Humanos')
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))



@bot.command(name='quote', help='Responds with a random quote')
async def quote(ctx, user: discord.User = None):

    if user is None:
        author, user_quotes = random.choice(list(quotes.items()))
    else:
        author = user.name
        user_quotes = quotes.get(author)
        if user_quotes is None:
            await ctx.send("Esse User não tem citações")
            return

    quote = random.choice(user_quotes)
    response = '"{}"\n- {}'.format(quote, author)
    await ctx.send(response)



@bot.command(name='addquote', help='Adds quote')
async def addquote(ctx, user: discord.User, quote):

    author = user.name

    user_quotes = quotes.get(author)
    if user_quotes is None:
        quotes[author] = [quote]
    else:
        user_quotes.append(quote)

    with open(quotes_path, 'w', encoding='utf-8') as json_file:
        json.dump(quotes, json_file, indent=4, ensure_ascii=False)

    await ctx.send("Quote added.")


bot.run(token)
