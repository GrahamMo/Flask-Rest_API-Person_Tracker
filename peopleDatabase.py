from flask import Flask, request, Response
import requests
import json
import random


app = Flask(__name__)

people = []

def exists(ID):
    count = 0
    for i in people:
        if i["id"] == ID:
            return [True, i, count]
            count += 1
    return [False, None]


@app.route("/people", methods=["POST"])
def add_person():
    ID = random.randint(1,99999999999999999999999)

    while exists(ID)[0]:
        ID = rand.randint(1,999999999999999999999) #random thing

    person = request.json
    name = person["name"]
    age = person["age"]
    country = person["country"]

    people.append({"id": ID, "name": name, "age": age, "country": country})
    print(people) 

    return str(ID)

@app.route("/people", methods=["GET"])
def get_person():

    ID = (request.args.get('id'))

    if ID == None:
        status_code = Response(response=json.dumps(people), status=200)
        return status_code
    else:
        ID = int(ID)
        return_exists = exists(ID)
        if return_exists[0]:
            resp = Response(response=json.dumps(return_exists[1]), status=200)
            return resp
        else:
            status_code = Response(status=404)
            return status_code
    
@app.route("/people", methods=["DELETE"])
def delete():
    ID = int(request.args.get('id'))
   
    return_exists = exists(ID)
    if return_exists[0]:
        del people[return_exists[2]]
        resp = Response(status=200)
        return resp
    else:
        resp = Response(status=404)
        return resp

@app.route("/people", methods=["UPDATE"])
def update():
    ID = int(request.args.get('id'))

    return_exists = exists(ID)
    if return_exists[0]:
        person = json.loads(request.data)
 
        for key in person:
            people[return_exists[2]][key] = person[key]
        return "Status Code 200"

    else:
        resp = Response(status=404)
        return resp










