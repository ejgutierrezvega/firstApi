from flask import Flask
from flask import request
from flask import json
from flask import Response
from flask import jsonify
from repository import mongorepository
from datetime import datetime
from bson.json_util import dumps
from customexception import myexception
import logging

file_handler = logging.FileHandler('apiLog.log')

app = Flask(__name__)
app.config['DEBUG'] = True
app.logger.addHandler(file_handler)
#app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    if request.method == 'GET':
        repo = mongorepository.MongoRepository('test', 'restaurants')
        try:
            document = repo.FindCollectionById("40356151")
        except myexception.MyException, e:
            resp = Response(e.valuetojson(), status=500, mimetype='application/json')
        else:
            data = dumps(document)
            resp = Response(data, status=200, mimetype='application/json')
        return resp

@app.route('/person/', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_person():
    app.logger.info('trace for api person')
    app.logger.error('this is an error')
    repo = mongorepository.MongoRepository('test', 'restaurants')
    if request.method == 'GET':
        document = repo.FindCollectionById("40356151")
        data = dumps(document)
        #js = json.dumps(data)
        resp = Response(data, status=200, mimetype='application/json')
        #resp = jsonify(data)
        #resp.status_code = 200
        return resp
        #return dumps(document)
    
    elif request.method == 'POST':
        item = {
            "address": {
                "street": "2 Avenue",
                "zipcode": "10075",
                "building": "1480",
                "coord": [-73.9557413, 40.7720266]
            },
            "borough": "Manhattan",
            "cuisine": "Italian",
            "grades": [
                {
                    "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                    "grade": "A",
                    "score": 11
                },
                {
                    "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                    "grade": "B",
                    "score": 17
                }
            ],
            "name": "Vella",
            "restaurant_id": "41704620"
        }

        mongorepository.InsertItem(item)
        return 'Hi stranger'
        
    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

@app.route('/person/<personname>')
def personbyname(personname):
    return 'Hi person %s, how are you' % personname

@app.route('/person/<int:personid>')
def personbyId(personid):
    return 'Hi persond %d' % personid

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)