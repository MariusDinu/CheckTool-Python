from ftplib import FTP

import keyboard
import sys
import requests as requests

import time
import signal
from msvcrt import getch
import msvcrt


def print_fn():
    print("Hi")

#URL
def checkUrl(urlString):
    try:
        r = requests.get(urlString)
        print(r.status_code)
    except:
        print("Eroare,incearca un link!")

def url(urlString, timeNumber, timeLetters):
    print(urlString)
    sec = timer(int(timeNumber), timeLetters)
    if (sec == None):
        print("Scrie un timp corect!")
        return 0
    checkUrl(urlString)
    while sec:
        print("Timp ramas: ", sec, " secunde", end="\r")
        time.sleep(1)
        sec -= 1
    if (sec == 0):
        ver = stopCicle()
        if (ver == 0):
            print("CheckTool a fost oprit!")
        else:
            print("CheckTool va incerca peste timpul stabilit inca o conectare!", end="\n")
            url(urlString, timeNumber, timeLetters)

#FTP
def checkFtp(stringFtp,stringUser,stringPassword):
  try:
    ftpObj = FTP(stringFtp,stringUser,stringPassword)
    if (ftpObj.getwelcome() != None):
        print("Conectat la ftp server!")
  except:
    print("Eroare la conectare! Serverul nu este valid!")

def ftp(ftpString,user,password, timeFtpNumber, timeFtpLetters):
    print("Nume Host:",ftpString)
    secFtp = timer(int(timeFtpNumber), timeFtpLetters)
    if (secFtp == None):
        print("Scrie un timp corect!")
        return 0
    checkFtp(ftpString,user,password)
    while secFtp:
        print("Timp ramas: ", secFtp, " secunde", end="\r")
        time.sleep(1)
        secFtp -= 1
    if (secFtp == 0):
        ver = stopCicle()
        if (ver == 0):
                print("CheckToolFtp a fost oprit!")
        else:
                print("CheckToolFtp va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
                ftp(ftpString,user,password,timeFtpNumber,timeFtpLetters)


#TIMER
def seconds(numberSeconds):
    return numberSeconds

def minutes(numberSecondsMinutes):
    return numberSecondsMinutes * 60

def hours(numberSecondsHours):
    return numberSecondsHours * 60 * 60;

def days(numberSecondsDays):
    return numberSecondsDays * 60 * 60 * 24;

def months(numberSecondsDays):
    return numberSecondsDays * 60 * 60 * 24 * 30;

def timer(number, letters):
    switcher = {
        "Sec": 1,
        "Min": 2,
        "Hours": 3,
        "Days": 4,
        "Months": 5,
    }

    try:
        func = switcher.get(letters, "Invalid month")

        if (func == 1):
            return seconds(number)
        if (func == 2):
            return minutes(number)
        if (func == 3):
            return hours(number)
        if (func == 4):
            return days(number)
        if (func == 5):
            return months(number)
    except:
        print("Incearca ceva valid ca timp!")
        return 0

#BREAKER
def stopCicle():
    timeout = 5
    print("Ai 5 secunde daca doresti sa opresti verificarea!")
    print("Apasa orice tasta...")

    try:
        while (timeout != 0):
            print("Timp ramas pentru oprire: ", timeout - 1, end="\r")
            timeout -= 1
            time.sleep(1)
            if msvcrt.kbhit():
                junk = getch()
                if junk:
                    return 0
    except KeyboardInterrupt:
        print('Ai oprit verificare!')
        return 0
    return 1


if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
