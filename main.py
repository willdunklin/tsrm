import threading
from threading import Thread
import time
import importlib

import input_handler as ih
from chat import Chat

def print_tike():
    print(time.time())

c = Chat()

chat_thread = Thread(target=c.run)
chat_thread.start()

try:
    while True:
        if not c.empty():
            command = c.pop()
            print('executing: ', command.lower())
            execution = Thread(target=ih.instruction, args=(command.lower(),))
            execution.start()
            time.sleep(0.05)
        else:
            time.sleep(0.5)
except KeyboardInterrupt:
    ih.unpress()
    # this doesn't work, i dont know how to kill the thread the bot is in its own infinite loop
    print('unpressed keys, terminating thread')
    exit()