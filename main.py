import os
import sys
import serial
from termcolor import colored, cprint
from pyfiglet import Figlet
from requests import get
from os import system, name
from time import sleep
from build.welcome import welcome
from build.options import showOptions
from build.python_idle import launchCLI
from func.getip import getip
from func.cleanup import cliCleanup
from func.serialcommunication import serialCom
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
    
    elif takenOption == '3':
        serialCom()
        
    elif takenOption == 'exit':
        print(colored('\nexiting ...\n', 'yellow'))
        cliCleanup()
        quit()  
    
    elif takenOption == '4':
        launchCLI(0)
        
    else:
        print('that is not ready yet')
    
    f = colored('>> ', 'yellow', attrs = ['blink'])
    takenOption = str(input(f))
