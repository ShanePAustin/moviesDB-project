#moviesMongo.py

#This file connects to MongoDB and defines the queries related to the MongoDB
#called from the main movies.py program

#Author: Shane Austin

##########################################################################
##########################################################################

import pymongo

myclient = None

    #DB connect function
def connect():  
    
    global myclient   
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')

##########################################################################
    #Option 5 
    # MongoDB query to search for subtitles from input string
    #Append related _id to an array to pass to mySQL query

def find(language):

    if (not myclient):
        connect()

    films = []

    #Define DB and collection to use
    mydb = myclient["movieScriptsDB"]
    collection = mydb["movieScripts"]

    #MongoDB query with $regex to allow partial string search 
    # option: i to ignore case sensitivity
    query = {"subtitles": { "$regex": "\\b" + language + "\\b", "$options": 'i'}}
    subtitle = collection.find(query)

    #Append related _id to array
    for row in subtitle:
        films.append(row["_id"])

    
    return films 

##########################################################################
    #Option 6
    #Add new inputs to the movieScripts DB from given inputs

def insert(ID, Keyword, Subtitles, filmID):

    if (not myclient):
        connect()

    #Define DB and collection to use
    mydb = myclient["movieScriptsDB"]
    collection = mydb["movieScripts"]

    #MongoDB query with 3 inputs from user
    query = {"_id" : ID, "Keywords" : Keyword, "subtitle" : Subtitles}

    try:
        if ID in filmID:
            collection.insert_one(query) 
            print("MovieScript: {} added to database".format(ID))            
        else:
            print("*** Error ***: Film with id: {} does not exist in moviesDB".format(ID))
            
    #exception handling if ID exists already    
    except pymongo.errors.DuplicateKeyError as e: 
        print("*** ERROR ***: Movie Script with id: {} already exists".format(ID)) 
    except Exception as e: 
        print("Error:", e)
##########################################################################

def main():
    if (not myclient):
        try:
            connect()

        except Exception as e:
            print("Problem connecting to database", e)

if __name__ == "__main__":
    main()
