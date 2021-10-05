#moviesMySQl.py

#This file connects to MySQL and defines the queries related to MySQL DB
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
    #Option 1:
    #Run mySQL query and return in pages of 5 rows, 'q' to quit

def getFilms():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = '''(select f.filmname, a.actorname
	            from film f
                join filmcast fc
		            on fc.castfilmid = f.filmid
                join actor a
                    on fc.castactorid = a.actorid
                order by f.filmname, a.actorname) 
                '''

    #connect to DB ping to re-establish connection after disconnect errors
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)

    #print query result 5 rows at a time until 'q' is entered
        while True:
            output = cursor.fetchmany(5)
            for row in output:
                print(row["filmname"], "¦" , row["actorname"])
            print("----------")
            print("Press any key for next page")    
            quit = input("-- (q) to Quit--")

            if quit =="q":
                break

##########################################################################
    #Option 2
    #Run mySQL query on given year and gender inputs

def getActors(year, male, female):
    #Connect to Db
    if (not conn):
        connect()

    #Db query with user inputs added to placeholders    
    query = "SELECT ActorName, MONTHNAME(ActorDOB), ActorGender FROM Actor WHERE YEAR(ActorDOB) = %s and (ActorGender = %s or ActorGender = %s)"

    #Query execution
    with conn:
        try:
            conn.ping()
            cursor = conn.cursor()
            cursor.execute(query, (year, male, female))
            return cursor.fetchall()


        except pymysql.err.IntegrityError as e:
            print(e)  
        except pymysql.err.InternalError as e:
            print(e)       
            
##########################################################################
    #Option 3
    #Run studio MySQL query

def getStudio():
    #Connect to Db
    if (not conn):
        connect()

    #Db query
    query = "SELECT * FROM Studio order by StudioID"   
    
    #Query execution
    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)
        output = cursor.fetchall()

    #Creating an array of the query
        studioID = []
        studioName = []

        for row in output:
            studioID.append(row["StudioID"])
            studioName.append(row["StudioName"])

    #Merge 2 arrays into 1 dict
    studiosSQL = dict(zip(studioID,studioName))

    return studiosSQL
  
##########################################################################
    #Option 4
    #Add new country and ID from user input to DB

def addCountry(id, country):
    #Connect to Db
    if (not conn):
        connect()

    #Db query with user inputs added to placeholders
    query = "INSERT into Country (CountryID, CountryName) VALUES (%s, %s)"    

    #Query execution
    with conn:
        try:
            conn.ping()
            cursor = conn.cursor()
            cursor.execute(query, (id, country)) 
            conn.commit()  

    #Exception handling   
        except pymysql.err.IntegrityError as e: 
            print("ERROR!!!:", country, "or", id, "already exists")  
        except pymysql.err.InternalError as e:
            print(e)    

##########################################################################
    #Option 5
    #Use tuple from MongoDB query to retieve Filmname and Synopsis from mySQL


def getSubtitles(films):
    #Connect to Db
    if (not conn):
        connect()

    #Query execution
    with conn:
        try:

            conn.ping()
            cursor = conn.cursor()

    #Db query with tuple added into query
            query = "SELECT filmname, LEFT(filmsynopsis, 30) as Synopsis FROM FILM f where f.filmID in {};".format(films)

            cursor.execute(query)
    #Output length can vary so fetches as many as outputted             
            #output = cursor.fetchmany(len(films))
            output = cursor.fetchall()
            print("")
            print("Movies with Subtitles")
            print("---------------------")

    #Print output for all rows
            while True:                
                for row in output:
                    print(row["filmname"], "¦" , row["Synopsis"])
                break

    #Exception handling
        except pymysql.err.IntegrityError as e:
            print(e)  
        except pymysql.err.InternalError as e:
            print(e) 
        except:
            print("No Matches!!!")
##########################################################################
    #Option 6
    #Lookup mySQLmovie IDs

def getFilmID():
    #Connect to Db
    if (not conn):
        connect()

    #Query execution
    with conn:
        try:
            conn.ping()
            cursor = conn.cursor()

    #Db query
            query = "SELECT FilmID from film;"

            cursor.execute(query)
            output = cursor.fetchall()

            filmID = []
            #print(output)
            for row in output:
                filmID.append(row["FilmID"])

            return filmID

    #Exception handling
        except pymysql.err.IntegrityError as e:
            print(e)  

##########################################################################

def main():
    if (not conn): 
        try:
            connect()
        except Exception as e:
            print("Problem connecting to database", e)

if __name__ == "__main__":
    main()
