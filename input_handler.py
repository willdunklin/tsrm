import hardware

from time import sleep

mouse_dist = 500

ctrl = False
shift = False

key_table = {
    'a': hardware.VK_A,
    'd': hardware.VK_D,
    'e': hardware.VK_E,
    'f': hardware.VK_F,
    'l': hardware.VK_L,
    'q': hardware.VK_Q,
    's': hardware.VK_S,
    'w': hardware.VK_W,
    
    '1': hardware.VK_1,
    '2': hardware.VK_2,
    '3': hardware.VK_3,
    '4': hardware.VK_4,
    '5': hardware.VK_5,
    '6': hardware.VK_6,
    '7': hardware.VK_7,
    '8': hardware.VK_8,
    '9': hardware.VK_9,
    '0': hardware.VK_0,

    'f1': hardware.VK_F1,
    'f3': hardware.VK_F3,
    'f5': hardware.VK_F5,
    'space': hardware.VK_SPACE,
    'ctrl': 'ctrl',
    'shift': 'shift',

    'up': 'up',
    'left': 'left',
    'right': 'right',
    'down': 'down',
    'lclick': 'lclick',
    'rclick': 'rclick',
    'lpress': 'lpress',
    'rpress': 'rpress',
}

def unpress():
    for key in hardware.keys:
        hardware.ReleaseKey(key)
    hardware.MouseAction(hardware.MOUSEEVENTF_LEFTUP)
    hardware.MouseAction(hardware.MOUSEEVENTF_RIGHTUP)

def instruction(x):
    s = x.lower().split(' ')[0]
    if s not in key_table:
        return
    
    # input k
    k = key_table[s]

    # keyboard commands
    if type(k) == int:
        hardware.press_key(k)
    # mouse commands
    else:
        special_input(k, x)

def special_input(s, x):
    global shift, ctrl

    dist = mouse_dist
    if(len(x.split(' ')) > 1):
        if(x.split(' ')[1].isnumeric()):
            dist = int(x.split(' ')[1])

    if s == 'up':
        hardware.MoveMouse(0, -dist)
    elif s == 'left':
        hardware.MoveMouse(-dist, 0)
    elif s == 'right':
        hardware.MoveMouse(dist, 0)
    elif s == 'down':
        hardware.MoveMouse(0, dist)
    elif s == 'lclick':
        hardware.LeftClick()
    elif s == 'rclick':
        hardware.RightClick()
    elif s == 'lpress':
        hardware.LeftDown()
    elif s == 'rpress':
        hardware.RightDown()
    # shift + control toggles
    elif s == 'ctrl':
        if ctrl:
            hardware.ReleaseKey(hardware.VK_CTRL)
        else:
            hardware.PressKey(hardware.VK_CTRL)
        ctrl = not ctrl
    elif s == 'shift':
        if shift:
            hardware.ReleaseKey(hardware.VK_SHIFT)
        else:
            hardware.PressKey(hardware.VK_SHIFT)
        shift = not shift


# for _ in range(30):
#     instruction('left')
#     instruction('w')
#     sleep(.1)

# instruction('lpress')
# sleep(5)
# instruction('lclick')

# instruction('e')
# instruction('up 40')
