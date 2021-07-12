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
import pretty_help
import time
import asyncio
import urllib



bot = commands.Bot(command_prefix= commands.when_mentioned_or('.'), description = 'These are all the commands for this bot!', help_command = pretty_help.PrettyHelp(no_category = 'Commands', index_title = 'Commands', show_index = False, sort_commands = True))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="VsCode - destroyTheWorld.rar"))


@bot.command(name = 'about', help = 'About BillyBOB')
async def about(ctx):
    await ctx.send('''
--|__***BillyBOB***__|--    
Owner - Boolean#7588(822513626521927730)  
My Github - https://github.com/Boolean0-0
Get a copy - https://github.com/Boolean0-0/BillyBOB
Written Jul 7, 2021
Version 2.6.33''')

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
    print('Issued command dog with no error')

@bot.command(name = 'eightball', help = 'Let the eightball answer your question')
async def eightball(ctx):
    response = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes, definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful' 
    ]
    choice = random.choice(response)
    await ctx.send(choice)
    print('Issued eightball command without error')


@bot.command(name = 'roll', help = 'Rolls a dice')
async def rolldice(ctx):
    message = await ctx.send("Choose a number:\n**4**, **6**, **8**, **10**, **12**, **20** ")
    
    def check(m):
        return m.author == ctx.author

    try:
        message = await bot.wait_for("message", check = check, timeout = 30.0)
        m = message.content

        if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
            await ctx.send("Sorry, invalid choice.")
            return
        
        coming = await ctx.send("Here it comes...")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.randint(1, int(m))}**")
        print('Issued roll command succesfully')
    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send("Procces has been canceled because you didn't respond in **30** seconds.")

@bot.command(name = 'wouldyourather', help = 'Gives a random wouuld you rather question', aliases = ['rather'])
async def rather(ctx):
    question = [
        'Would you rather go into the past and meet your ancestors or go into the future and meet your great-great-grandchildren?',
        'Would you rather have more time or more money?',
        'Would you rather have a rewind button or a pause button on your life?',
        'Would you rather be able to talk with the animals or speak all foreign languages?',
        'Would you rather win the lottery or live twice as long?',
        'Would you feel worse if no one showed up to your wedding or to your funeral?',
        'Would you rather be without internet for a week, or without your phone?',
        'Would you rather meet George Washington or the current president?',
        'Would you rather lose your vision or your hearing?',
        'Would you rather work more hours per day, but fewer days or work fewer hours per day, but more days?',
        'Would you rather listen to music from the ’70s or music from today?',
        'Would you rather become someone else or just stay you?',
        'Would you rather be Batman or Spiderman?',
        'Would you rather be stuck on a broken ski lift or in a broken elevator?',
        'For your birthday, would you rather receive cash or gifts?',
        'Would you rather go to a movie or to dinner alone?',
        'Would you rather always say everything on your mind or never speak again?',
        'Would you rather make a phone call or send a text?',
        'Would you rather read an awesome book or watch a good movie?',
        'Would you rather be the most popular person at work or school or the smartest?',
        'Would you rather put a stop to war or end world hunger?',
        'Would you rather spend the night in a luxury hotel room or camping surrounded by beautiful scenery?',
        'Would you rather explore space or the ocean?',
        'Would you rather go deep-sea diving or bungee jumping?',
        'Would you rather be a kid your whole life or an adult your whole life?',
        'Would you rather go on a cruise with friends or with your spouse?',
        'Would you rather lose your keys or your cell phone?',
        'Would you rather eat a meal of cow tongue or octopus?',
        'Would you rather have x-ray vision or magnified hearing?',
        'Would you rather work in a group or work alone?',
        'Would you rather be stuck on an island alone or with someone who talks incessantly?',
        'Would you rather be too hot or too cold?',
        'When you’re old, would you rather die before or after your spouse?',
        'Would you rather have a cook or a maid?',
        'Would you rather be the youngest or the oldest sibling?',
        'Would you rather get rich through hard work or through winning the lottery?',
        'Would you rather have a 10-hour dinner with a headstrong politician from an opposing party, or attend a 10-hour concert for a music group you detest?',
        'Would you rather be an Olympic gold medalist or a Nobel Peace Prize winner?',
        'Would you rather have a desk job or an outdoor job?',
        'Would you rather live at the top of a tall NYC apartment building or at the top of a mountain?',
        'Would you rather have Rambo or The Terminator on your side?',
        'Would you rather be proposed to in private or in front of family and friends?',
        'Would you rather have to sew all your clothes or grow your own food?',
        'Would you rather hear the good news or the bad news first?',
        'Would you rather be your own boss or work for someone else?',
        'Would you rather have nosy neighbors or noisy neighbors?',
        'Would you rather be on a survival reality show or dating game show?',
        'Would you rather be too busy or be bored?',
        'Would you rather watch the big game at home or live at the stadium.'
    ]
    await ctx.send(random.choice(question))
    print('Issued command wouldyourather with no error')

def fancyHTML(a):
    opener = urllib.request.FancyURLopener({})
    open_url = opener.open(a)
    page = str(open_url.read()).replace('\\n', '\n')
    return page


@bot.command(name = 'ascii', help = 'ascii any of your words. Put the word in the arg. Example: .ascii hey+jo *or* .ascii hey')
async def ascii(ctx, word):
    baseURL = 'https://artii.herokuapp.com/make?text='
    URL = baseURL + word
    data = fancyHTML(URL)
    # response = urllib.request.urlopen(URL)
    # data = response.read()
    await ctx.send(data)
    print('Issued command ascii with no error')

@bot.command(name = 'insult', help = 'Insult anyone')
async def insult(ctx):
    data = urllib.request.urlopen('https://insult.mattbas.org/api/insult')
    response = data.read()
    await ctx.send(response)
    print('Issued command insult with no error')

@bot.command(name = 'bird', help = 'make:bird:a:bird:messege:bird:like:bird:this:bird:one')
async def bird(ctx, *args):
    response = ''
    for arg in args:
        response += ':bird:' + arg
    await ctx.send(response)
    print('Issued command bird with no error')

@bot.command(name = 'frog', help = ':frog:make:frog:a:frog:messege:frog:like:frog:this:frog:one')
async def frog(ctx, *args):
    response = ''
    for arg in args:
        response += ':frog:' + arg
    await ctx.send(response)
    print('Issued command frog with no error')


@bot.command(name = 'clap', help = 'make:clap:a:clap:messege:clap:like:clap:this:clap:one')
async def clap(ctx, *args):
    response = ''
    for arg in args:
        response += ':clap:' + arg
    await ctx.send(response)
    print('Issued command clap with no error')

@bot.command(name = 'kanye', help = 'Gives a quote from kanye, and you all know how smart he is!')
async def kanye(ctx):
    response = requests.get('https://api.kanye.rest/')
    data = response.json()
    await ctx.send(data['quote'])
    print('Issued command kanye with no error')

@bot.command(name = 'lock', help = 'Helps a mod loack the channel if people are being bad')
@commands.has_permissions(manage_channels=True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in lockdown.*** You guys have been very naughty.")

@bot.command(name = 'unlock', help = 'Unlocks a channel')
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.*** I gues the mod thought you guys arent so bad.")


@bot.command(name = 'embedrules', help = 'embeds rules')
async def rules(ctx):
    embed = discord.Embed(title="RULES", description='''
    No blank nicknames.
    No inappropriate nicknames.
    No sexually explicit nicknames.
    No offensive nicknames.
    No nicknames with unusual or unreadable Unicode.
    No blank profile pictures.
    No inappropriate profile pictures.
    No sexually explicit profile pictures.
    No offensive profile pictures.
    No membership granted to minors (under 18 years).
    Moderators reserve the right to change nicknames.
    Moderators reserve the right to use their own discretion regardless of any rule.
    No exploiting loopholes in the rules (please report them).
    No DMing other members of the server.
    Rules apply to DMing other members of the server.
    No inviting unofficial bots.
    No bugs, exploits, glitches, hacks, bugs, etc.
''',colour=discord.Colour.light_gray())
    await ctx.send(embed=embed)





bot.run('#############################################################3')
