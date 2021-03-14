from threading import Thread
import time

import input_handler as ih
from chat import Chat
import process_test

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
            if not process_test.exists():
                break
            time.sleep(0.05)
        else:
            time.sleep(0.5)

    print('minecraft not running, exiting')
    ih.unpress()

except KeyboardInterrupt:
    ih.unpress()
    # this doesn't work, i dont know how to kill the thread the bot is in its own infinite loop
    print('unpressed keys, terminating thread')
    exit()