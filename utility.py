from imports import *


"""
Student: Dinu Marius
Grupa: A5
Nume Proiect(drive): Connectivity Checker
Nume Proiect: CheckTool
Id: 2
Tip: B
"""


def helper():
    welcome = " Bun venit!\n"
    name = " Eu sunt CheckTool! Sunt un utilitar deci comenzile o sa le scrii tu...\n\n"
    details = "      Ai mai multe variante:\n"
    print(welcome.center(50, " "))
    print(name)
    print(details)
    print("1. a. utility.py urlOne <link-ul> (verificare OneTime)\n")
    print("   b. utility.py url <link> <numar> <unitate timp> (verificare la durata precizata)\n\n")
    print("2. a. utility.py ftpOne <server> <user> <password> (verificare OneTime)\n")
    print("   b. utility.py ftp <server> <user> <password> <numar> <unitate timp> (verificare la durata precizata)\n")
    print("   c. utility.py ftpUriOne <URI> (verificare OneTime) \n")
    print("   d. utility.py ftpUri <URI> <numar> <unitate timp> (verificare la durata precizata) \n\n")
    print("3. a. utility.py mongoOne <server> (verificareOneTime)\n")
    print("   b. utility.py mongo <server> <numar> <unitate timp> (verificare la durata precizata)\n\n")
    print("4. a. utility.py postgreOne <host> <user> <password> <port> <database> (verificareOneTime)\n")
    print(
        "   b. utility.py postgre <host> <user> <password> <port> <database> <numar> <unitate timp> "
        "(verificare la durata precizata)\n")
    print("   c. utility.py postgreUriOne <URI> (verificareOneTime)\n")
    print("   d. utility.py postgreUri <URI> <numar> <unitate timp> (verificare la durata precizata)\n\n")
    print("5. a. utility.py elastic <host> <user> <password> (verificareOneTime)\n")
    print(
        "   b. utility.py elastic <host> <user> <password> <numar> <unitate timo> (verificare la durata precizata)\n\n")
    print(" Numar = este numarul de secunde, ore, minute, zile, etc.")
    print(" Unitati de timp: Sec , Min , Hours , Days , Months ")
    print(" Ex: <numar> <unitate timp> ---> 4 Hours")


# URL
def checkUrl(urlString):
    try:
        r = requests.get(urlString)
        if 199 < r.status_code < 300:
            valid = "Este valid!"
            print(valid.center(50, " "))
        else:
            invalid = "Este invalid!"
            print(invalid.center(50, " "))
    except ConnectionError as errorUrl:
        print(errorUrl)
        print("Eroare,link invalid!")


def url(urlString, timeNumber, timeLetters):
    print(urlString)
    sec = timer(int(timeNumber), timeLetters)
    if sec is None:
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
    if sec == 0:
        ver = stopCicle()
        if ver == 0:
            print("\n\nCheckTool a fost oprit!")
        else:
            print("\n\nCheckTool va incerca peste timpul stabilit inca o conectare!\n\n")
            url(urlString, timeNumber, timeLetters)


def urlOne(urlString):
    print(urlString)
    checkUrl(urlString)


# FTP
def checkFtp(stringFtp, stringUser, stringPassword):
    try:
        ftpObj = FTP(stringFtp, stringUser, stringPassword)
        if ftpObj.getwelcome() is not None:
            print("\n")
            valid = "Conectarea la server se poate realiza!"
            print(valid.center(50, " "))
            print("\n")
    except ConnectionError as errorFtp:
        print(errorFtp)
        print("Eroare la conectare! Serverul nu este valid!")

def ftpUriOne(ftpstringUri):
    d3 = DateFtp(ftpstringUri)
    ftpOne(d3.host,d3.username,d3.password)

def ftpUri(ftpStringUri,timeFtpNumber, timeFtpLetters):
    d4 = DateFtp(ftpStringUri)
    ftp(d4.host, d4.username, d4.password,timeFtpNumber, timeFtpLetters)

def ftp(ftpString, user, password, timeFtpNumber, timeFtpLetters):
    print("\nNume Host:", ftpString, "\nUser: ", user, "\nPassword: ", password)
    secFtp = timer(int(timeFtpNumber), timeFtpLetters)
    if secFtp is None:
        print("Scrie un timp corect!")
        return 0
    checkFtp(ftpString, user, password)
    print("Apasa orice tasta pentru a opri programul...")
    while secFtp:
        print("Timp ramas: ", secFtp, " secunde", end="\r")
        if msvcrt.kbhit():
            junk = getch()
            if junk:
                return 0
        time.sleep(1)
        secFtp -= 1
    if secFtp == 0:
        ver = stopCicle()
        if ver == 0:
            print("\n\nCheckToolFtp a fost oprit!")
        else:
            print("\n\nCheckToolFtp va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
            ftp(ftpString, user, password, timeFtpNumber, timeFtpLetters)


def ftpOne(ftpString, user, password):
    print("\nNume Host:", ftpString, "\nUser: ", user, "\nPassword: ", password)
    checkFtp(ftpString, user, password)


# MongoDB
def checkMongo(stringMongo):
    try:
        client = pymongo.MongoClient(stringMongo)
        db = client.admin
        info = client.server_info()
        serverStatusResult = db.command("serverStatus")
        if info is not None and serverStatusResult is not None:
            valid = "Conexiune valida!"
            print(valid.center(50, " "))
        client.close()
    except ConnectionError as errorMongo:
        print(errorMongo)
        print("Serverul nu este valid!")


def mongo(stringMongo, timeMongoNumber, timeMongoLetters):
    print("Nume Mongo:", stringMongo)
    secMongo = timer(int(timeMongoNumber), timeMongoLetters)
    if secMongo is None:
        print("Scrie un timp corect!")
        return 0
    checkMongo(stringMongo)
    print("Apasa orice tasta pentru a opri programul...\n")
    while secMongo:
        print("Timp ramas: ", secMongo, " secunde", end="\r")
        if msvcrt.kbhit():
            junk = getch()
            if junk:
                return 0
        time.sleep(1)
        secMongo -= 1
    if secMongo == 0:
        ver = stopCicle()
        if ver == 0:
            print("\n\nCheckToolMongo a fost oprit!")
        else:
            print("\n\nCheckToolMongo va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
            mongo(stringMongo, timeMongoNumber, timeMongoLetters)


def mongoOne(stringMongo):
    print("Nume Mongo:", stringMongo)
    checkMongo(stringMongo)


# PostgreSql


def checkPostgre(stringHost, stringUser, stringPass, stringPort, stringDB):
    try:
        conn = "host=" + stringHost \
               + " dbname=" + stringDB \
               + " user=" + stringUser \
               + " password=" + stringPass \
               + " port=" + stringPort
        connection = psycopg2.connect(conn)
        valid = "Conexiune valida!"
        print(valid.center(50, " "))
        connection.close()
    except psycopg2.OperationalError as errorPost:
        print(errorPost)


def postgreUriOne(stringUri):
    d1=DateConn(stringUri)
    postgreOne(d1.host,d1.username,d1.password,d1.port,d1.path)

def postgreUri(stringUri,timePostNumber,timePostLetters):
    d2 = DateConn(stringUri)
    postgre(d2.host, d2.username, d2.password, d2.port, d2.path,timePostNumber,timePostLetters)

def postgre(stringHost, stringUser, stringPass, stringPort, stringDB, timePostNumber, timePostLetters):
    print("\nHost: ", stringHost, "\nPort: ", stringPort, "\nDB: ", stringDB, "\nUser: ", stringUser, "\nPassword: ",
          stringPass)
    secPost = timer(int(timePostNumber), timePostLetters)
    if secPost is None:
        print("Scrie un timp corect!")
        return 0
    checkPostgre(stringHost, stringUser, stringPass, stringPort, stringDB)
    print("Apasa orice tasta pentru a opri programul...")
    while secPost:
        print("Timp ramas: ", secPost, " secunde", end="\r")
        if msvcrt.kbhit():
            junk = getch()
            if junk:
                print("\n\nCheckToolPostgre a fost oprit!")
                return 0
        time.sleep(1)
        secPost -= 1
    if secPost == 0:
        ver = stopCicle()
        if ver == 0:
            print("\n\nCheckToolPostgre a fost oprit!")
        else:
            print("\n\nCheckToolPostgre va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
            postgre(stringHost, stringUser, stringPass, stringPort, stringDB, timePostNumber, timePostLetters)


def postgreOne(stringHost, stringUser, stringPass, stringPort, stringDB):
    print("\nHost: ", stringHost, "\nPort: ", stringPort, "\nDB: ", stringDB, "\nUser: ", stringUser, "\nPassword: ",
          stringPass)
    checkPostgre(stringHost, stringUser, stringPass, stringPort, stringDB)


# Elastic

def checkElastic(stringCloud, user, secret):
    try:
        es = Elasticsearch(stringCloud, http_auth=(user, secret))
        if es.ping():
            print("Se poate conecta!")
        else:
            print("Nu se poate face conexiunea!")
    except Exception as errorElastic:
        print(errorElastic)


def elasticOne(stringCloud, user, secret):
    print("Host: ", stringCloud[:-5], "\nUser: ", user, "\nSecret: ", secret, "\nPort: ", stringCloud[-4:])
    checkElastic(stringCloud, user, secret)


def elastic(stringCloud, user, secret, timeElasticNumber, timeElasticLetters):
    print("Host: ", stringCloud[:-5], "\nUser: ", user, "\nSecret: ", secret, "\nPort: ", stringCloud[-4:])
    secElastic = timer(int(timeElasticNumber), timeElasticLetters)
    if secElastic is None:
        print("Scrie un timp corect!")
        return 0
    checkElastic(stringCloud, user, secret)
    print("Apasa orice tasta pentru a opri programul...")
    while secElastic != 5:
        print("Timp ramas: ", secElastic, " secunde ", end="\r")
        if msvcrt.kbhit():
            junk = getch()
            if junk:
                print("\n\nCheckToolPostgre a fost oprit!")
                return 0
        time.sleep(1)
        secElastic -= 1
        if secElastic == 0:
            ver = stopCicle()
            if ver == 0:
                print("\n\nCheckToolPostgre a fost oprit!")
            else:
                print("\n\nCheckToolPostgre va incerca inca o conectare!Timpul stabilit a trecut!\n\n")
                elastic(stringCloud, user, secret, timeElasticNumber, timeElasticLetters)


# TIMER
def seconds(numberSeconds):
    return numberSeconds


def minutes(numberSecondsMinutes):
    return numberSecondsMinutes * 60


def hours(numberSecondsHours):
    return numberSecondsHours * 60 * 60


def days(numberSecondsDays):
    return numberSecondsDays * 60 * 60 * 24


def months(numberSecondsDays):
    return numberSecondsDays * 60 * 60 * 24 * 30


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

        if func == 1:
            return seconds(number)
        if func == 2:
            return minutes(number)
        if func == 3:
            return hours(number)
        if func == 4:
            return days(number)
        if func == 5:
            return months(number)
    except Exception as errorTime:
        print(errorTime)
        print("Incearca ceva valid ca timp!")
        return 0


# BREAKER
def stopCicle():
    timeout = 5
    print("Mai ai 5 secunde daca doresti sa opresti verificarea!")
    print("Apasa orice tasta...")

    try:
        while timeout != 0:
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
    except Exception as e:
        print("\n",e)
        print("\n Scrie in consola <utility.py helper> pentru ajutor...")



