from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    meals = db.relationship('UserMeal', backref='user', lazy=True)

class UserMeal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    carbs = db.Column(db.Float)
    proteins = db.Column(db.Float)
    fats = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, carbs, proteins, fats, user_id):
        self.name = name
        self.carbs = carbs
        self.proteins = proteins
        self.fats = fats
        self.user_id = user_id
