from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button

from time import sleep

class Input:
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        self.mouse_dist = 500

        self.lpressed = False
        self.rpressed = False

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
            'lpress': 'mouse_lpress',
            'rpress': 'mouse_rpress',
            'scroll': 'mouse_scroll',
        }

    def instruction(self, x):
        s = x.lower().split(' ')[0]
        if s not in self.key_table:
            return
        
        # input s
        s = self.key_table[s]

        # mouse commands
        if 'mouse' in s:
            self.mouse_input(s, x)
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

    def mouse_input(self, s, x):
        dist = self.mouse_dist
        if(len(x.split(' ')) > 1):
            if(x.split(' ')[1].isnumeric()):
                dist = int(x.split(' ')[1])

        print('distance: ', dist)
        if s == 'mouse_up':
            self.mouse.move(0, -dist)
        elif s == 'mouse_left':
            self.mouse.move(-dist, 0)
        elif s == 'mouse_right':
            self.mouse.move(dist, 0)
        elif s == 'mouse_down':
            self.mouse.move(0, dist)
        elif s == 'mouse_lclick':
            self.mouse.release(Button.left)
            self.mouse.click(Button.left, 1)
        elif s == 'mouse_rclick':
            self.mouse.release(Button.right)
            self.mouse.click(Button.right, 1)
        elif s == 'mouse_lpress':
            if self.lpressed:
                self.lpressed = False
                self.mouse.release(Button.left)
            else:
                self.lpressed = True
                self.mouse.press(Button.left)
        elif s == 'mouse_rpress':
            if self.rpressed:
                self.rpressed = False
                self.mouse.release(Button.right)
            else:
                self.rpressed = True
                self.mouse.press(Button.right)
        elif s == 'mouse_scroll':
            self.mouse.scroll(0, 1)