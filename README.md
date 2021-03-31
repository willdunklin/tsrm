# Twitch Speedruns Minecraft

Windows application to take emulate keypresses taken from twitch chat to play minecraft.

Generally, this is just remote access software controlled by twitch (so use at your own risk), but there are safety measures implented such as:
- Limiting number of emulatable inputs
- Ensuring Minecraft process is running
- Having halt(h) and pause(p) hotkeys


### Features yet to be added
- Democracy mode
- Input display


## To use:
```
pip install pipenv
pipenv install
pipenv run main.py
```

This article is a useful read for twitch bot related stuff: https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8

*Again reminder this will only work on Windows, due to OS specific keyboard emulation.*
