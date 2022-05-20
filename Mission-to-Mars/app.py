## import dependendencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping



## set up Flask
app = Flask(__name__)
mongo = PyMongo(app)
## use flask_pymongo to set pymongo connection
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_app"

## define html route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

## run the Flask
if __name__ == "__main__":
    app.run()
