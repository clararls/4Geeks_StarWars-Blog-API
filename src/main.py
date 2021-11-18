"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
import json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Planets, People, Favorites_planets, Favorites_people
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200
@app.route('/users', methods=['GET'])
def list_Users():
    list_users = Users.query.all()
    return jsonify([users.serialize() for users in list_users]), 200

@app.route('/people', methods=['GET'])
def list_people():
    list_people = People.query.all()
    return jsonify([people.serialize() for people in list_people]), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def peopleId(people_id):
    peopleOne = People.query.get(people_id) 
    return jsonify(peopleOne.serialize())

@app.route('/planets', methods=['GET'])
def planets():
    return jsonify(Planets)

@app.route('/planets/<int:planet_id>', methods=['GET'])
def planetsId(planet_id):
    planetOne = People.query.get(planets_id) 
    return jsonify(peopleOne.serialize())

@app.route('/users/favorites', methods=['GET'])
def listUserFavorites(users_id):
    peopleFavs = People_Fav.query.all()
    planetFavs = Planet_Fav.query.all()
    userFavs = [peopleFavs.query.filter_by(id=users_id) for fav in peopleFavs]
    return jsonify(users.serialize()), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
