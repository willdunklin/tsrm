import os
import queue
import threading
from twitchio.ext import commands

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

q = queue.Queue(100)

@bot.event
async def event_ready():
    print(f'{bot.nick} is up')
    # ws = bot._ws
    # await ws.send_privmsg(os.environ['CHANNEL'], f'/me pogu')

@bot.event
async def event_message(context):
    if context.author.name.lower() == bot.nick.lower():
        return
    for x in context.content.split('+')[:10]:
        q.put(x.strip())
    print(context.content)
    await bot.handle_commands(context)

@bot.command(name='keys')
async def keys(context):
    await context.send('valid keys: w, a, s, d, f, l, q, f1, f3, f5, space, ctrl, shift, 0-9')

@bot.command(name='mouse')
async def mouse(context):
    await context.send('mouse commands: up, left, right, down, <direction> <distance>, lclick, rclick, lpress, rpress')

@bot.command(name='info')
async def info(context):
    await context.send('type commands from command lists !mouse and !keys and chain together commands with \'+\'')


class Chat:
    def run(self):
        bot.run()

    def empty(self):
        return q.empty()
    
    def pop(self):
        return q.get()

    # nonfunctional
    def close(self):
        bot._ws.teardown()
        print('teardown?')
        exit(1)