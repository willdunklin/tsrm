import threading
from threading import Thread
import time
import importlib

from input_handler import Input
from chat import Chat

def print_tike():
    print(time.time())


i = Input()
c = Chat()

chat_thread = Thread(target=c.run)
chat_thread.start()

while True:
    if not c.q_empty():
        command = c.pop_q()
        print('executing: ', command.lower())
        i.instruction(command.lower())
    else:
        time.sleep(0.5)

chat_thread.exit()