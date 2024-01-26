from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # Incripts cocies data config
    app.config["SECRET_KEY"] = "jokio skirtumo kolkas"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    login_manager = LoginManager()
    login_manager.login_view = (
        "auth.login"  # Set the login view to your authentication route
    )
    login_manager.init_app(app)

    from .db_models import User, Food, FoodCategories

    return app


def create_database(app):
    with app.app_context():
        db.create_all()
        print("Created Database!")
