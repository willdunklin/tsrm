import os
from twitchio.ext import commands

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    print(f'{bot.nick} is up')
    # ws = bot._ws
    # await ws.send_privmsg(os.environ['CHANNEL'], f'/me pogu')

@bot.event
async def event_message(context):
    print(context.content)
    await bot.handle_commands(context)
    if context.author.name.lower() == bot.nick.lower():
        return
    await context.channel.send(context.content)

@bot.command(name='test')
async def test(context):
    await context.send('test passed pog')

bot.run()