import os
import sys
from os import system, name
from termcolor import colored, cprint
from pyfiglet import Figlet
from build.welcome import welcome
from build.options import showOptions

def launchCLI(arg):
    _ = system('clear')
    f = Figlet(font = 'banner')
    print(colored(f.renderText('Therminal\n IDLE\n\n'), 'red'))
    while True:
        a = str(input('>> '))
        if a == 'exit':
            quit()
        elif a == '0':
            _ = system('clear')
            welcome()
            showOptions()
            break
        else:
            exec(a)
            