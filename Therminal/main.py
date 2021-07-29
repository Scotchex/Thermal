import os
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from requests import get
from os import system, name
from time import sleep
from build.welcome import welcome
from build.options import showOptions
from func.getip import getip
from func.cleanup import cliCleanup

cliCleanup()

welcome()
showOptions()
f = colored('>> ', 'yellow', attrs = ['blink'])
takenOption = str(input(f))

while True:
    
    if takenOption == '0':
        cliCleanup()
        welcome()
        showOptions()
    elif takenOption == '1':
        getip()
        
    elif takenOption == '2':
        print('I love cats \n')
    
    elif takenOption == 'exit':
        print(colored('\n exiting ...', 'yellow \n'))
        quit()        
    else:
        print('that is not ready yet')
    
    f = colored('>> ', 'yellow', attrs = ['blink'])
    takenOption = str(input(f))
