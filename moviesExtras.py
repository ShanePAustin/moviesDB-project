#moviesExtras.py

#This file connects to MySQL and defines the extra queries related to MySQL DB
#called from the main movies.py program

#Author: Shane Austin

import pymysql

conn = None   
    #MySQL connection function
def connect():    
    global conn   
    conn = pymysql.connect( host="localhost", 
                            user="root", 
                            password="root", 
                            db="moviesDB", 
                            cursorclass=pymysql.cursors.DictCursor)

           
##########################################################################
    #Option 7
    #Run extra queries
#film names and dates
def getDate():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(FilmName, 30) as FilmName, DATE(FilmReleaseDate) from film;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Release Date:", row["DATE(FilmReleaseDate)"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 

##########################################################################
#film names and directors
def getDirector():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(f.FilmName,30) as FilmName, d.DirectorName from film f join director d on d.directorID = f.FilmDirectorID;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Director:", row["DirectorName"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################
#film names and film language
def getLanguage():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(f.FilmName,30) as FilmName, l.language, c.CountryName from film f join language l on l.LanguageID = f.FilmLanguageID join country c on c.CountryID = f.FilmCountryID;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Language:", row["language"], "¦","Country:", row["CountryName"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################
#film names and film Genre
def getGenre():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(f.FilmName,30) as FilmName, g.genreName from film f join genre g on g.genreID = f.FilmGenreID;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Genre:", row["genreName"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################
#film names and film Synopsis
def getSynopsis():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(FilmName, 30) as FilmName, FilmSynopsis from film;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Synopsis:", row["FilmSynopsis"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################
#film names and film Run Time
def getRunTime():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(FilmName, 30) as FilmName, FilmRunTimeMinutes from film;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Run Time:",row["FilmRunTimeMinutes"], "mins")
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################
#film names and film certificate
def getCertificate():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(f.FilmName,30) as FilmName, c.Certificate from film f join certificate c on c.certificateID = f.FilmGenreID;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Certificate:", row["Certificate"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################
#film names, film budget and box office earnings
def getBudget():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(FilmName, 30) as FilmName, concat('$', format(FilmBudgetDollars,0)) as Budget, concat('$', format(FilmBoxOfficeDollars,0)) as BoxOffice from film;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" ,"Budget:", row["Budget"], "¦","Box Office:", row["BoxOffice"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################
#film names, oscar nominations and oscar winnings
def getOscars():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT LEFT(FilmName, 30) as FilmName, FilmOscarNominations, FilmOscarWins from film;"

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print('{:^30}'.format(row["FilmName"]), "¦" , "Nominations:", row["FilmOscarNominations"], "¦", "Wins:", row["FilmOscarWins"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break 
##########################################################################

def main():
    if (not conn): 
        try:
            connect()
        except Exception as e:
            print("Problem connecting to database", e)

if __name__ == "__main__":
    main()