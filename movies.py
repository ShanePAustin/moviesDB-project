#movies.py

#This is the main file of a program the manipulates MySQL and Mongo databases to retrieve movie info
#This file sets the program menu and the individual options available
#It also calls the functions defined to run the specific DB requests and set the output
#Most of the code was adapted from the lecture notes of the Applied Databases module

#Author: Shane Austin

##########################################################################
##########################################################################

#import the MySQL functions file
#import the MongoDB functions file
import moviesMySQL
import moviesMongo
import moviesExtras

#Stored dict for Option 3 
studiosMain = {}

def main():
    menu()
    while True:

        operation = input("Choice:")
#############################################################
        #Option 1
        #Retrieve Filmname and Actor names from mySQL
        if operation == '1':
            print("")
            print("Films")
            print("------")
        
        #run getFilms function from moviesMySQL
            moviesMySQL.getFilms()

            menu()
#############################################################
        #Option 2
        #Input DOB and gender of Actors into mySQL query
        elif operation == '2':

            print("")
            print("Actors")
            print("------")

        #Continue input request until a valid integer is entered
            while True:
                try:
                    year = int(input("Year of Birth : "))
                    break
                except:
                    continue
        
        #Continue input request until Male/Female or nothing is entered
            while True:
                try:
                    gender = input("Male/Female: ")
                    if gender == "Male" or gender == "Female" or gender == "":
                        break
                except:
                    continue


        #defining what gets passed to the query based on the 3 possible inputs              
            if gender == "Male":
                male = "Male"
                female = ""
            if gender == "Female":
                male = ""
                female = "Female"
            if gender == "":
                male = "Male"
                female = "Female"

            print("")
            print("Actors")
            print("------")

        #run get actors query with user inputs as variables
            actors = moviesMySQL.getActors(year, male, female)

        #print query return row by row
            for actor in actors:
                print(actor["ActorName"], "¦", actor["MONTHNAME(ActorDOB)"], "¦", actor["ActorGender"])

            menu()
##############################################################
        #Option 3
        #Retrieve studios from MySQL query
        #Store the output to retrieve the data on the second request
        elif operation == '3':
            print("")
            print("Studios")
            print("------")


        #Stored dict from first query run        
            global studiosMain
            
        #if studiosMain is empty do getStudio
            if not studiosMain:
                studiosSQL = moviesMySQL.getStudio()

                #print("mySQL Output")
                for row in studiosSQL:
                    print(row, "¦", studiosSQL[row])
   
                studiosMain = studiosSQL

        #if studiosMain is not empty print stored Array
            else: 
                #print("Stored Array")
                for row in studiosMain:
                    print(row, "¦", studiosMain[row])
       
            menu()
################################################################
        #Option 4
        #Add a new Country with ID to the mySQL DB
        elif operation == '4':

            print("")
            print("Add New Country")
            print("---------------")

        #Continue input request until a valid integer is entered
            while True:
                try:
                    id = int(input("ID: "))
                    break
                except:
                    continue

        #Continue input request until a string is entered
            while True:
                try:
                    country = str(input("Country: "))
                    if len(country) > 0: 
                        break
                except:
                    continue
        
        #Run query with 2 inputs
            moviesMySQL.addCountry(id, country)   
            menu()

###################################################################
        #Option 5
        #Lookup Subtitles from moviesScriptsDB using MongoDB
        #and pass into mySQL query
        #Allow for partial string search to allow for data entry inconsistency

        elif operation == '5':

            print("")
            print("Movies with Subtitles")
            print("---------------------")

        #Continue input request until a string is entered
            while True:
                try:
                    language = input("Enter subtitle Language : ")
                    if len(language) > 0: 
                        break
                except:
                    continue           

        #Run MongoDB query with input  
            films = moviesMongo.find(language)

        #Convert output into a tuple and run getSubtitles
            films = tuple(films)
            moviesMySQL.getSubtitles(films)
           
            menu()           

#####################################################################            
        #Option 6
        #Add new Keywords and Subtitles assinged to a movie ID
        elif operation == '6':

            print("")
            print("Add New Movie Script")
            print("--------------------")

        #Continue input request until a valid integer is entered
            while True:
                try:
                    ID = int(input("ID: "))
                    break
                except:
                    continue

        #Array to store keyword input
            keyArray = []
            
        #Continue input request of multiple strings until -1 is entered
            while True:
                try:
                    Keyword = input("Keyword (-1 to end): ")
                    if Keyword == "-1":
                        break
                    keyArray.append(Keyword)
                    
                except:
                    continue

        #Array to store keyword input          
            subArray = []

            #Continue input request of multiple strings until -1 is entered
            while True:
                try:
                    Subtitles = input("Subtitles Language (-1 to end):  ")
                    if Subtitles == "-1":
                        break
                    subArray.append(Subtitles)
                    
                except:
                    continue

            filmID = moviesMySQL.getFilmID()

        #Run MongoDB query input arrays
            moviesMongo.insert(ID, keyArray, subArray, filmID)
            
            menu()
#####################################################################
        #Option 7
        #Retrieve additional Film details from mySQL
        elif operation == '7':
            extrasMenu()
            while True:

                operation = input("Choice:")
            
            #run extra functions based on option choice
                if operation == "1":
                    moviesExtras.getDate()
                    extrasMenu()

                elif operation == "2":
                    moviesExtras.getDirector()
                    extrasMenu()

                elif operation == "3":
                    moviesExtras.getLanguage()
                    extrasMenu()

                elif operation == "4":
                    moviesExtras.getGenre()
                    extrasMenu()

                elif operation == "5":
                    moviesExtras.getSynopsis()
                    extrasMenu()

                elif operation == "6":
                    moviesExtras.getRunTime()
                    extrasMenu()

                elif operation == "7":
                    moviesExtras.getCertificate()
                    extrasMenu()    

                elif operation == "8":
                    moviesExtras.getBudget()
                    extrasMenu()                 

                elif operation == "9":
                    moviesExtras.getOscars()
                    extrasMenu()  

                elif operation == 'x':
                    break                                 

                else:
                    print("Invalid choice. Please try again.")
                    extrasMenu()

            menu()

#####################################################################
        #Exit the program if x is entered
        elif operation == 'x':
            break

        #Exception handling for any other menu input
        else:
            print("Invalid choice. Please try again.")
            menu()
######################################################################


#Program main options menu

def menu():
    print('''
    Movies DB
    ---------

    MENU:
    ====
    1 - View Films
    2 - View Actors by Year of Birth and Gender
    3 - View Studios
    4 - Add New Country
    5 - View Movie with Subtitles
    6 - Add New MovieScript
    7 - Extra Features
    x - Exit Application
    ''')

#Program extras menu

def extrasMenu():
    print('''
    Movies DB 
    ---------
    Select an option for extra queries
    ==================================
    1 - Release Dates
    2 - Directors
    3 - Film Language and Country
    4 - Genre
    5 - Synopsis
    6 - Run Times
    7 - Certificate
    8 - Budget and Box Office
    9 - Oscars
    x - Return to Main Menu
    ''')


if __name__ == "__main__":
    main()
 