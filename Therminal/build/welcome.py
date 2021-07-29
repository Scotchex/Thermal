import os
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from requests import get
from os import system, name
from time import sleep

def welcome():
    print('\n')
    print('\n')
    f = Figlet(font='banner')
    print(colored(f.renderText('Therminal'), 'yellow'))
    f = Figlet(font='5lineoblique')
    print(colored(f.renderText('By 2b2b2b'), 'red'))
    print('\n')
    print('\n')
