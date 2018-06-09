from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

app.config.from_pyfile('config.py')

client = MongoClient(app.config['MONGO_URI'])
db = client.heroku_c21w9r55


from routes import *

if __name__ == '__main__':
    app.run()