# from https://stackoverflow.com/questions/13564851/how-to-generate-keyboard-events

import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MOUSEEVENTF_MOVE      = 0x0001
MOUSEEVENTF_LEFTDOWN  = 0x0002
MOUSEEVENTF_LEFTUP    = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP   = 0x0010
MOUSEEVENTF_WHEEL     = 0x0800
MOUSEEVENTF_ABSOLUTE  = 0x8000


MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_A     = 0x41
VK_B     = 0x42
VK_C     = 0x43
VK_D     = 0x44
VK_E     = 0x45
VK_F     = 0x46
VK_G     = 0x47
VK_H     = 0x48
VK_I     = 0x49
VK_J     = 0x4a
VK_K     = 0x4B
VK_L     = 0x4C
VK_M     = 0x4D
VK_N     = 0x4E
VK_O     = 0x4F
VK_P     = 0x50
VK_Q     = 0x51
VK_R     = 0x52
VK_S     = 0x53
VK_T     = 0x54
VK_U     = 0x55
VK_V     = 0x56
VK_W     = 0x57
VK_X     = 0x58
VK_Y     = 0x59
VK_Z     = 0x5A

VK_0     = 0x30
VK_1     = 0x31
VK_2     = 0x32
VK_3     = 0x33
VK_4     = 0x34
VK_5     = 0x35
VK_6     = 0x36
VK_7     = 0x37
VK_8     = 0x38
VK_9     = 0x39

VK_F1    = 0x70
VK_F2    = 0x71
VK_F3    = 0x72
VK_F5    = 0x74
VK_CTRL  = 0x11
VK_SPACE = 0x20
VK_SHIFT = 0xA0

keys = [VK_A, VK_B, VK_C, VK_D, VK_E, VK_F, VK_G, VK_H, VK_I, VK_J, VK_K, VK_L, VK_M, VK_N, VK_O, VK_P, VK_Q, VK_R, VK_S, VK_T, VK_U, VK_V, VK_W, VK_X, VK_Y, VK_Z, VK_0, VK_1, VK_2, VK_3, VK_4, VK_5, VK_6, VK_7, VK_8, VK_9, VK_F1, VK_F2, VK_F3, VK_F5, VK_CTRL, VK_SPACE, VK_SHIFT]

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize


def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def MoveMouse(x, y):
    x = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dx=x,dy=y,dwFlags=MOUSEEVENTF_MOVE))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def MouseAction(action):
    x = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dwFlags=action))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def LeftClick():
    MouseAction(MOUSEEVENTF_LEFTUP)
    MouseAction(MOUSEEVENTF_LEFTDOWN)
    time.sleep(0.05)
    MouseAction(MOUSEEVENTF_LEFTUP)

def LeftDown():
    MouseAction(MOUSEEVENTF_LEFTDOWN)

def RightClick():
    MouseAction(MOUSEEVENTF_RIGHTUP)
    MouseAction(MOUSEEVENTF_RIGHTDOWN)
    time.sleep(0.05)
    MouseAction(MOUSEEVENTF_RIGHTUP)

def RightDown():
    MouseAction(MOUSEEVENTF_RIGHTDOWN)

def press_key(k):
    PressKey(k)
    time.sleep(0.2)
    ReleaseKey(k)