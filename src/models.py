from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    users_name = Column(String(30), nullable=False)
    password = Column(String(250), nullable=False)
    favorites_planets = relationship("Favorites_planets")
    favorites_people = relationship("Favorites_people")

class Planets(db.Model):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(30), nullable=False)
    favorites_planets = relationship("Favorites_planets")

class People(db.Model):
    __tablename__='people'
    id = Column(Integer, primary_key=True)
    people_name = Column(String(30), nullable=False)
    favorites_people = relationship("Favorites_people")

class Favorites_planets(db.Model):
    __tablename__='favorites_planets'
    id = Column(Integer, primary_key=True)
    users_id = Column(String, ForeignKey('users.id'))
    planets_id = Column(String, ForeignKey('planets.id'))

class Favorites_people(db.Model):
    __tablename__='favorites_people'
    id = Column(Integer, primary_key=True)
    users_id = Column(String, ForeignKey('users.id'))
    people_id = Column(String, ForeignKey('people.id'))