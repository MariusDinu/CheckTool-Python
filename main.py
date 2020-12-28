import keyboard
import sys

import requests as requests
import ftplib
import time
import signal
from msvcrt import getch
import msvcrt

def print_fn():
    print("Hi")

def week(i):
        switcher = {
            'Sunday': 'Sunday',
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday'
        }
        func=switcher.get(i, lambda :'Invalid')
        print(func)

def kill_input():
    pass

def stopCicle():
    timeout = 5
    print("Ai 5 secunde daca doresti sa opresti verificarea!")
    print("Apasa orice tasta")


    try:
        while (timeout!=0):
            print(timeout - 1)
            timeout -= 1
            time.sleep(1)
            if msvcrt.kbhit():
                junk = getch()
                if junk:
                    return 0
    except KeyboardInterrupt:
        print('Ai oprit verificare!')
        return 0
    #return 1


def check(urlString):
    try:
        r =requests.get(urlString)
        print(r.status_code)
    except:
        print("Eroare,incearca un link!")

def url(urlString,timeNumber,timeLetters):
    print(urlString)
    sec=timer(int(timeNumber),timeLetters)
    check(urlString)
    print("Timp ramas:")
    while sec:
        print(sec, end="\r")
        time.sleep(1)
        sec -= 1
    if(sec==0):
        ver=stopCicle()
        if(ver==0):
         print("CheckTool a fost oprit!")
        else:
            print("CheckTool va incerca peste timpul stabilit inca o conectare!")
            url(urlString,timeNumber,timeLetters)

def seconds(numberSeconds):
    return numberSeconds

def minutes(numberSecondsMinutes):
    return numberSecondsMinutes*60

def timer(number,letters):
    switcher = {
         "Sec": 1,
         "Min": 2,
         "H": 3,
         "D": 4,
         "M": 5,
    }
    func=switcher.get(letters, "Invalid month")
    if(func==1):
        return seconds(number)
    if(func==2):
        return minutes(number)



def ftp(ftpString,time):
    print(ftpString)
    ftp = FTP(ftpString)
    print(ftp.login())
    print(time)

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])