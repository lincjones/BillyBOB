#Discord bot
#v 0.1.6
#written Jul 7, 2021
#by boolean#7588

#import discord
import discord
from discord.ext import commands
#import api's used for some commands
import pyjokes as joke
import random
import pyrandmeme
import randfacts
#other imports
import os
import requests
import json



bot = commands.Bot(command_prefix= 'bob ', help_command = None)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="VsCode - destroyTheWorld.rar"))


@bot.command(name = 'meme', help = 'This command sends a meme using the pyrandmeme API')
async def pyRandMeme(ctx):
    await ctx.send(embed=await pyrandmeme.pyrandmeme())
    print('Issued command meme with no error')

@bot.command(name='joke', help = 'This command sends a random joke using the pyjokes API')
async def randJoke(ctx):
    response = joke.get_joke()
    await ctx.send(response)
    print('Issued command joke with no error')

@bot.command(name = 'hello', help = 'This command lets me say hi', aliases = ['hi', 'hey', 'hola', 'HI', 'Hi', 'Hello', 'Hey', 'Hola'])
async def randGreeting(ctx):

    greeting = [
        'Hello there, bud',
        'Cant talk now',
        'Heyheyhey',
        'Hello',
        'Hi👋',
        'こんにちは',
        '👋',
        'Ewwwwwww look at your avatarrrr!!!',
        '👋 greetings earthling',
        'Hello will you be my firend, I have none and can\'t figure out why.',
        '👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋'
    ]

    response = random.choice(greeting)
    await ctx.send(response)
    print('Issued command hello with no error')


@bot.command(name = 'ping', help = 'The classic ping command')
async def pingpong(ctx):
    await ctx.send('PONG🏓')
    print('Issued command pong with no error')

@bot.command(name = 'coinflip', help = 'A command to simulate a random coinflip', aliases = ['heads', 'headsortails', 'tails', 'flip', 'coin'])
async def coinflip(ctx):
    response = [
        'Heads🪙',
        'Tails🪙'
    ]
    await ctx.send(random.choice(response))
    print('Issued command coinflip with no error')

@bot.command(name='create-channel', help = 'If your an admin you get to create a channellll! yay ig', aliases = ['create'])
async def create_channel(ctx, channel_name='BillyBob-playhouse'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
    print('Issued command create with no error')


#banhammer
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send('I brought down the BANHAMMERRR!!!!!!!!')
    print('Issued command ban with no error')

#The below code unbans player.
@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
    print('Issued command unban with no error')

@bot.command(help = "Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"I was waiting for {member.mention} to shut up! He was finnally muted!", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
    print('Issued command mute with no error')


@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention} you better watch you back!",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)
   print('Issued command unmute with no error')

@bot.command(name = 'fact', help = 'Displays a random fact using the python api randfacts', aliases = ['randomfact', 'Randfact', 'Fact'])
async def randfact(ctx):
    await ctx.send(randfacts.getFact())
    print('Issued command fact with no error')


@bot.command(name = 'say', help = 'Stop putting words in my mouth!', aliases = ['Say', 'saythis'])
async def say(ctx, *args):
    response = ''
    for arg in args:
        response += ' ' + arg
    await ctx.send(response)
    print('Issued command say with no error')

@bot.command(name = 'Dababy', help = 'Dababys anything you tell me too', aliases = ['dababyit', 'dababy', 'da'])
async def dababy(ctx, args):
    await ctx.send('da\'' + args)
    print('Issued command dababy with no error')


@bot.command(name = 'epicness', help = 'Ranks how epic you are!', aliases = ['epic', 'epicrate', 'howepic', 'howepicami'])
async def epicness(ctx):
    epicLevel = random.randint(1,101)
    await ctx.send(f'Epicness level: ***__{epicLevel}' + chr(37) + '__***')
    print('Issued command epicness with no error')

@bot.command(name = 'gamerrank', help = 'Ranks how good of a gamer you are', aliases = ['gamer', 'skilz', 'skils', 'rankmyskils'])
async def gamerrank(ctx):
    gamerpercent = random.randint(1,101)
    await ctx.send(f'Gamer level: ***__{gamerpercent}' + chr(37) + '__***')
    print('Issued command gamerrank with no error')


@bot.command(name = 'cat', help = 'Generates a random image of a cat')
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.send(data['file'])
    print('Issued command cat with no error')


@bot.command(name = 'dog', help = 'Generates a random image of a dog')
async def dog(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    await ctx.send(data['message'])
    print('Issued command cat with no error')

@bot.command()
async def help(ctx):
    await ctx.send('''
    `----------------------------------------------------------------------- |
                         --|BillyBOB|--                                 |
    |BillyBOB is a bot    |Owner - Boolean#7588(822513626521927730)     |
    |written in python by |My Github - https://github.com/Boolean0-0    |
    |Boolean#7588.        |Written Jul 7, 2021                          |
    |---------------------|Version 0.1.6                                |
    |     Commands        |**Utility commands included                  |
    |Fact, meme, joke,    |**This message may look different            |
    |hello, coinflip,     |if you are on mobile                         |
    |createchannel, ping, |                                             |
    |gamerrank, cat,      |                                             |
    |say, epic, dababy,   |                                             |
                                                                        |
------------------------------------------------------------------------|`
    ''')
    embed = discord.Embed()
    embed.description = "Click [here](https://github.com/Boolean0-0) to go to my Github page."
    await ctx.send(embed=embed)
    print('Issued command help with no error')




bot.run('#########################################')
