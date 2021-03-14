from threading import Thread
import time

from input_handler import instruction, unpress
from chat import Chat
import process_test
from halt import halt, pause

c = Chat()
chat_thread = Thread(target=c.run)
chat_thread.start()

halt_thread = Thread(target=halt)
halt_thread.start()

pause_thread = Thread(target=pause)
pause_thread.start()

try:
    while halt_thread.is_alive():
        if not c.empty():
            command = c.pop()
            print('executing: ', command.lower())
            execution = Thread(target=instruction, args=(command.lower(),))
            execution.start()
            if not process_test.exists():
                break
            time.sleep(0.05)
        else:
            time.sleep(0.5)
        if not pause_thread.is_alive():
                input('waiting for input...')
                pause_thread.join()
                pause_thread = Thread(target=pause)
                pause_thread.start()

    print('exiting')
    unpress()

except KeyboardInterrupt:
    unpress()
    # this doesn't work, i dont know how to kill the thread the bot is in its own infinite loop
    print('unpressed keys, terminating thread')
    exit()