from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))


class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(150), nullable=False)
    food_price = db.Column(db.Float, nullable=False)
    id_categorie = db.Column(db.Integer, db.ForeignKey("food_categories.id"))

class FoodCategories(db.Model):
    __tablename__ = "food_categories"
    id = db.Column(db.Integer, primary_key=True)
    food_category = db.Column(db.String(150), nullable=False)