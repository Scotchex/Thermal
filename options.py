#this is to be filled with a list of stuff this#
#terminal is capable of (turning on lights etc)#
#for now I am just gonna throw in some place holders#

import os
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from requests import get
from os import system, name
from time import sleep



def showOptions():
    print(colored(
"""
0. Clean the terminal
1. Learn your IP adress    
2. Print 'I love cats'    
3. Start a COM connection
4. To launch the Therminal Python CLI

"""
, 'yellow'))

