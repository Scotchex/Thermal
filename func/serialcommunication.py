import serial
from termcolor import colored
from time import sleep
import os
import sys
from func.cleanup import cliCleanup
from build.options import showOptions
from build.welcome import welcome
def serialCom():
    print('edit the .cpp file under serial commununation DIR')
    print('COM? : ')
    x = str(input('>> '))
    serial_Port = serial.Serial(x, 9600) 
    print('connectting ...\n')
    sleep(2)
    print('connection successful\n')
    while True:
        command = str(input('>> '))
        if command == 'exit':
            print('exiting')
            quit()
        elif command == '0':
            cliCleanup()
            welcome()
            showOptions()
            break
        else :
            b = command.encode()
            serial_Port.write(b)
    #set command values#
