from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button

from time import sleep

class Input:
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        self.mouse_dist = 50

        self.key_table = {
            'a': 'a',
            'b': 'b',
            'c': 'c',
            'd': 'd',
            'e': 'e',
            'f': 'f',
            'g': 'g',
            'h': 'h',
            'i': 'i',
            'j': 'j',
            'k': 'k',
            'l': 'l',
            'm': 'm',
            'n': 'n',
            'o': 'o',
            'p': 'p',
            'q': 'q',
            'r': 'r',
            's': 's',
            't': 't',
            'u': 'u',
            'v': 'v',
            'w': 'w',
            'x': 'x',
            'y': 'y',
            'z': 'z',
            
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '0': '0',

            'f1': '!f1',
            'f2': '!f2',
            'f3': '!f3',
            'f5': '!f5',
            'space': '!space',
            'enter': '!enter',
            'shift': '!shift',

            'up': 'mouse_up',
            'left': 'mouse_left',
            'right': 'mouse_right',
            'down': 'mouse_down',
            'lclick': 'mouse_lclick',
            'rclick': 'mouse_rclick',
            'scroll': 'mouse_scroll',
        }

    def instruction(self, x):
        if x not in self.key_table:
            return
        # input s
        s = self.key_table[x.lower()]
        # mouse commands
        if 'mouse' in s:
            self.mouse_input(s)
        # the rest of keyboard
        else:
            if '!' in s:
                if s == '!f1':
                    self.send_key(Key.f1)
                elif s == '!f2':
                    self.send_key(Key.f2)
                elif s == '!f3':
                    self.send_key(Key.f3)
                elif s == '!f5':
                    self.send_key(Key.f5)
                elif s == '!space':
                    self.send_key(Key.space)
                elif s == '!enter':
                    self.send_key(Key.enter)
                elif s == '!shift':
                    self.send_key(Key.shift)
            else:
                self.send_key(s)

    def send_key(self, k):
        self.keyboard.press(k)
        sleep(0.2)
        self.keyboard.release(k)

    def mouse_input(self, x):
        if x == 'mouse_up':
            self.mouse.move(0, -self.mouse_dist)
        elif x == 'mouse_left':
            self.mouse.move(-self.mouse_dist, 0)
        elif x == 'mouse_right':
            self.mouse.move(self.mouse_dist, 0)
        elif x == 'mouse_down':
            self.mouse.move(0, self.mouse_dist)
        elif x == 'mouse_lclick':
            self.mouse.click(Button.left, 1)
        elif x == 'mouse_rclick':
            self.mouse.click(Button.right, 1)
        elif x == 'mouse_scroll':
            self.mouse.scroll(0, 1)


i = Input()
sleep(4)
for _ in range(10):
    i.instruction('w')
    sleep(1)