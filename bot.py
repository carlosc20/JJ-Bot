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


@bot.command(name='piada', help='Responds with a random quote')
async def piada(ctx):
    quotes = [
        'Américo',
        'Sergay',
        'Abatuto'
    ]

    response = random.choice(quotes)
    await ctx.send(response)


@bot.command(name='teste')
@commands.has_role('♕ Sangue Real')
async def teste(ctx):
    await ctx.send('olá membro do sangue real',)



@bot.command(name="abatido",
                description="Quem será abatido?",
                brief="Si sarà abattuto!",
                aliases=["Abatido", "ABATIDO"],
                pass_context=True)
async def abatido(ctx):
    possible_responses = [
        'Abatuto',
        'Cotes',
        'Lotes',
        'Lagastulia',
        'LordEagle',
        'Sergey',
        'Ahhhhmerico'
    ]
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)



bot.run(token)
