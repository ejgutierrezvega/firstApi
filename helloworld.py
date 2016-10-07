from flask import Flask
from repository import mongorepository
from datetime import datetime
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/')
def index():
    document = mongorepository.queryRestaurantByRestaurantId("40356151")
    return dumps(document)

@app.route('/person/')
def person():
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

    mongorepository.insertToRestaurants(item)
    return 'Hi stranger'

@app.route('/person/<personname>')
def personbyname(personname):
    return 'Hi person %s, how are you' % personname

@app.route('/person/<int:personid>')
def personbyId(personid):
    return 'Hi persond %d' % personid

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)