from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)


class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(150), nullable=False)
    food_price = db.Column(db.Float, nullable=False)
    id_categorie = db.Column()

class FoodCategories(db.Model):
    __tablename__ = "food_categories"
    id = db.Column(db.Integer, primary_key=True)
    food_category = db.Column(db.String(150), nullable=False)