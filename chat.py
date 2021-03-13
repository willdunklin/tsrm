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

q = queue.Queue(10)

@bot.event
async def event_ready():
    print(f'{bot.nick} is up')
    # ws = bot._ws
    # await ws.send_privmsg(os.environ['CHANNEL'], f'/me pogu')

@bot.event
async def event_message(context):
    if context.author.name.lower() == bot.nick.lower():
        return
    q.put(context.content)
    print(context.content)
    await bot.handle_commands(context)

@bot.command(name='exit')
async def exit(context):
    exit(1)

class Chat:
    def run(self):
        bot.run()

    def q_empty(self):
        return q.empty()
    
    def pop_q(self):
        return q.get()