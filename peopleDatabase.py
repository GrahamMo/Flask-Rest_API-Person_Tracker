#Flask-Rest_API-Person_Tracker
#This is a simple REST API that I built using get, post, delete and update methods.
#The program acts as a simple database that can store information of an input. In this simple example, it stores the name, age and country of an input and also assigns them an ID number so their information can be accessed and manipulated / mutated.

from flask import Flask, request, Response
import requests
import json
import random


app = Flask(__name__) #create new rest api

people = [] #mock database, that stores dictionaries of people information

def exists(ID): #function that checks if the id already exists in the list and if they do it returns their index
    count = 0
    for i in people: 
        if i["id"] == ID:
            return [True, i, count]
            count += 1
    return [False, None]


@app.route("/people", methods=["POST"])
def add_person(): #post route that takes the given json of the person's information, assigns them a random unique ID, and adds their information as a python dict to the the master list
    ID = random.randint(1,99999999999999999999999)

    while exists(ID)[0]: #keep generating random IDs until a unique one has been created
        ID = rand.randint(1,999999999999999999999)

    person = request.json #request the json
    name = person["name"] #from the json dictionaries pull out variables
    age = person["age"]
    country = person["country"]

    people.append({"id": ID, "name": name, "age": age, "country": country}) # add it to the master list
    print(people) 

    return str(ID)

@app.route("/people", methods=["GET"]) 
def get_person(): #get route that given an id returns the assoiated user's information and if the ID does not exist then resturns 404. if no id is given then it returns the master list of people

    ID = (request.args.get('id')) #retrieve the id arguement

    if ID == None: #if there is no ID
        status_code = Response(response=json.dumps(people), status=200) 
        return status_code #return the master list and successful status code
    else:
        ID = int(ID) 
        return_exists = exists(ID) 
        if return_exists[0]: #if the id exists in the master list
            resp = Response(response=json.dumps(return_exists[1]), status=200) #return the users info and the successful status code
            return resp
        else:
            status_code = Response(status=404) #if id does not exists return unsuccessful status code
            return status_code
    
@app.route("/people", methods=["DELETE"]) 
def delete():#delete route that removes a given ID
    ID = int(request.args.get('id'))
   
    return_exists = exists(ID) #this returns list of index 0 being a boolean of if it exists, 1 index being the person, and 2nd index being the index of the person in the list
    if return_exists[0]:#if it exists
        del people[return_exists[2]] #delete its index from the master list
        resp = Response(status=200) #return success
        return resp
    else:
        resp = Response(status=404) #if it doesnt exists return that its invalid
        return resp

@app.route("/people", methods=["UPDATE"]) 
def update():#get route that given an id and a json, it updates the the python dict according to the json
    ID = int(request.args.get('id')) 

    return_exists = exists(ID) 
    if return_exists[0]: #if the id exists
        person = json.loads(request.data) #load the json data
 
        for key in person: #for each key in json dict
            people[return_exists[2]][key] = person[key] #access the the given user at the chosen index and change value with associated key in the python dict to the value with the associated key in the json
    else: #if id doesnt exists return error
        resp = Response(status=404)
        return resp










