import os
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from requests import get
from os import system, name
from time import sleep
def getip():
    ip = get('https://api.ipify.org').text
    print(ip)
    return ip