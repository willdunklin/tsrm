import keyboard

def halt():
    keyboard.wait('h')
    print('halted')

def pause():
    keyboard.wait('p')
    print('paused')