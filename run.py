import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI_BAKING_HOT")
app.config["MONGO_DBNAME"] = "baking_hot"

mongo = PyMongo(app)

@app.route('/')
def index():

#    return render_template("index.html", recipe=mongo.db.recipes.find_one())
    return render_template("index.html", recipe=mongo.db.recipes.find_one({'popular_recipe': True}))

#    return render_template("index.html", recipe=mongo.db.recipes.find_one({'type': 'Bread'}))

@app.route('/list_recipes')
def list_recipes():
    return render_template("recipes_list.html", recipes=list(mongo.db.recipes.find()))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)