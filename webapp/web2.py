from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient
#from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'thedb'
#app.config['MONGO_URI'] = MongoClient('mongodb://127.0.0.1:27017/') #added recent
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/thedb"
#app.url_map.strict_slashes = False
#client = MongoClient('MONGO_URI')
#db = client.thedb
#collection = db['gamerz']
#collection = db.gamerz

mongo = PyMongo(app)

@app.route('/')



def home():
    #mydoc = collection.find().sort("name", -1)
    #mydoc=mongo.db.gamerz.find().sort("name",-1)
    #myd=mongo.db.gamerz.find_one({'name':'sim'})
    """" just removed
    myd=mongo.db.gamerz.find_one({'code':'13'})
    return render_template('lead.html',name=myd['s_time'])"""
    """for x in mydoc:
      print(x)"""
    return render_template('efaq.html')      #just added


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
