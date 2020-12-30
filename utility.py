from ftplib import FTP
import keyboard
import sys
import requests as requests
import time
import signal
from msvcrt import getch
import msvcrt
import pymongo
import psycopg2

def helper():
    welcome=" Bun venit!\n"
    name=" Eu sunt CheckTool! Sunt un utilitar deci comenzile o sa le scrii tu...\n\n"
    details="      Ai mai multe variante:\n"
    print(welcome.center(50," "))
    print(name)
    print(details)
    print("1. a. utility.py urlOne <link-ul> (verificare OneTime)\n")
    print("   b. utility.py url <link> <numar> <unitate timp> (verificare la durata precizata)\n\n")
    print("2. a. utility.py ftpOne <server> <user> <password> (verificare OneTime)\n")
    print("   b. utility.py ftp <server> <user> <password> <numar> <unitate timp> (verificare la durata precizata)\n\n")
    print("3. a. utility.py mongoOne <server> (verificareOneTime)\n")
    print("   b. utility.py mongo <server> <numar> <unitate timp> (verificare la durata precizata)\n\n")
    print("4. a. utility.py postgreOne <host> <user> <password> <port> <database> (verificareOneTime)\n")
    print("   b. utility.py postgreOne <host> <user> <password> <port> <database> <numar> <unitate timp> (verificare la durata precizata)\n\n")
    print(" Numar = este numarul de secunde, ore, minute, zile, etc.")
    print(" Unitati de timp: Sec , Min , Hours , Days , Months ")
    print(" Ex: <numar> <unitate timp> ---> 4 Hours")

#URL
def checkUrl(urlString):
    try:
        r = requests.get(urlString)
        if(r.status_code>199 and r.status_code<300):
         print("Este valid!")
        else:
         print("Invalid!")
    except:
        print("Eroare,incearca un link!")

def url(urlString, timeNumber, timeLetters):
    print(urlString)
    sec = timer(int(timeNumber), timeLetters)
    if (sec == None):
        print("Scrie un timp corect!")
        return 0
    checkUrl(urlString)
    print("Apasa orice tasta pentru a opri programul...")
    while sec:

        print("Timp ramas: ", sec, " secunde", end="\r")

        if msvcrt.kbhit():
            junk = getch()
            if junk:
                return 0
        time.sleep(1)
        sec -= 1
    if (sec == 0):
        ver = stopCicle()
        if (ver == 0):
            print("CheckTool a fost oprit!")
        else:
            print("CheckTool va incerca peste timpul stabilit inca o conectare!\n\n")
            url(urlString, timeNumber, timeLetters)

def urlOne(urlString):
    print(urlString)
    checkUrl(urlString)


#FTP
def checkFtp(stringFtp,stringUser,stringPassword):
  try:
    ftpObj = FTP(stringFtp,stringUser,stringPassword)
    if (ftpObj.getwelcome() != None):
        print("Conectarea la server se poate realiza!")
  except:
    print("Eroare la conectare! Serverul nu este valid!")

def ftp(ftpString,user,password, timeFtpNumber, timeFtpLetters):
    print("Nume Host:",ftpString)
    secFtp = timer(int(timeFtpNumber), timeFtpLetters)
    if (secFtp == None):
        print("Scrie un timp corect!")
        return 0
    checkFtp(ftpString,user,password)
    print("Apasa orice tasta pentru a opri programul...")
    while secFtp:
        print("Timp ramas: ", secFtp, " secunde", end="\r")
        if msvcrt.kbhit():
            junk = getch()
            if junk:
                return 0
        time.sleep(1)
        secFtp -= 1
    if (secFtp == 0):
        ver = stopCicle()
        if (ver == 0):
                print("CheckToolFtp a fost oprit!")
        else:
                print("CheckToolFtp va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
                ftp(ftpString,user,password,timeFtpNumber,timeFtpLetters)

def ftpOne(ftpString,user,password):
    print("Nume Host:", ftpString)
    checkFtp(ftpString, user, password)


#MongoDB
def checkMongo(stringMongo):
    try:
        client = pymongo.MongoClient(stringMongo)
        db = client.admin
        info = client.server_info()
        serverStatusResult = db.command("serverStatus")
        if (info != None and serverStatusResult != None):
            print("Conexiunea este valida!")
        client.close()
    except:
        print("Serverul nu este valid!")

def mongo(stringMongo,timeMongoNumber,timeMongoLetters):
    print("Nume Mongo:", stringMongo)
    secMongo = timer(int(timeMongoNumber), timeMongoLetters)
    if (secMongo == None):
        print("Scrie un timp corect!")
        return 0
    checkMongo(stringMongo)
    print("Apasa orice tasta pentru a opri programul...")
    while secMongo:
        print("Timp ramas: ", secMongo, " secunde", end="\r")
        if msvcrt.kbhit():
            junk = getch()
            if junk:
                return 0
        time.sleep(1)
        secMongo -= 1
    if (secMongo == 0):
        ver = stopCicle()
        if (ver == 0):
            print("CheckToolMongo a fost oprit!")
        else:
            print("CheckToolMongo va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
            mongo(stringMongo,timeMongoNumber,timeMongoLetters)

def mongoOne(stringMongo):
  print("Nume Mongo:",stringMongo)
  checkMongo(stringMongo)


#PostgreSql
def checkPostgre(stringHost,stringUser,stringPass,stringPort,stringDB):
    try:
        conn = "host=" + stringHost + " dbname=" + stringDB + " user=" + stringUser + " password=" + stringPass + " port=" + stringPort
        connection = psycopg2.connect(conn)
        print("Conexiune valida!")
        connection.close()
    except psycopg2.OperationalError as e:
        print(e)
        return 0

def postgre(stringHost,stringUser,stringPass,stringPort,stringDB,timePostNumber,timePostLetters):
    print("Host: ", stringHost, "\nPort: ", stringPort, "\nDB: ", stringDB, "\nUser: ", stringUser, "\nPassword: ",
          stringPass)
    secPost = timer(int(timePostNumber), timePostLetters)
    if (secPost == None):
        print("Scrie un timp corect!")
        return 0
    checkPostgre(stringHost, stringUser, stringPass, stringPort, stringDB)
    print("Apasa orice tasta pentru a opri programul...")
    while secPost:
        print("Timp ramas: ", secPost, " secunde", end="\r")
        if msvcrt.kbhit():
            junk = getch()
            if junk:
                return 0
        time.sleep(1)
        secPost -= 1
    if (secPost == 0):
        ver = stopCicle()
        if (ver == 0):
            print("CheckToolPostgre a fost oprit!")
        else:
            print("CheckToolPostgre va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
            postgre(stringHost,stringUser,stringPass,stringPort,stringDB,timePostNumber,timePostLetters)
def postgreOne(stringHost,stringUser,stringPass,stringPort,stringDB):
     print("Host: ",stringHost,"\nPort: ",stringPort,"\nDB: ",stringDB,"\nUser: ",stringUser,"\nPassword: ",stringPass)
     checkPostgre(stringHost,stringUser,stringPass,stringPort,stringDB)

#MySql
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
    print("Mai ai 5 secunde daca doresti sa opresti verificarea!")
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
    try:
     globals()[args[1]](*args[2:])
    except:
       helper()