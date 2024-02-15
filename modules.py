from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table = db.Table(
    "association",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("table_id", db.Integer, db.ForeignKey("tables.id")),
)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String(20), unique=False, nullable=False)
    email = db.Column("email", db.String(120), unique=True, nullable=False)
    password = db.Column("password", db.String(60), unique=True, nullable=False)
    users = db.relationship(
        "Tables", secondary=association_table, back_populates="tables"
    )

class Tables(db.Model):
    __tablename__ = "tables"
    id = db.Column(db.Integer, primary_key=True)
    table_capacity = db.Column(
        "table_capacity", db.Integer)
    tables = db.relationship(
        "User", secondary=association_table, back_populates="users"
    )


class TableReservation(db.Model):
    __tablename__ = "table_reservation"
    id = db.Column(db.Integer, primary_key=True)
    association_id = db.Column(db.Integer, db.ForeignKey("association.id"))
    reservation_date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    guest_number = db.Column(db.Integer)

class FoodCategory(db.Model):
    __tablename__ = "food_category"
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column("category_name", db.String(20), unique=True)


class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column("food_name", db.String(20), unique=True, nullable=True)
    food_price = db.Column("food_price", db.String(20), unique=True, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("food_category.id"))
    category = db.relationship("FoodCategory")


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("title", db.String(255), nullable=True)
    url = db.Column("url", db.String(255), nullable=True)
    clas = db.Column("clas", db.String(255), nullable=True)
    start_date = db.Column(db.Time)
    end_date = db.Column(db.Time)