from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '{ hello:"Hellow world", main:__main__ }'

@app.route('/person')
def person():
    return 'Hi stranger'

@app.route('/person/<personname>')
def personbyname(personname):
    return 'Hi person %s, how are you' % personname

@app.route('/person/<int:personid>')
def personbyId(personid):
    return 'Hi persond %d' % personid

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)