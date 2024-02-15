from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from modules import db, User, Food, FoodCategory, Event
import forms
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
)
import os
from fill_in_database import add_food_categories, add_food

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "kos skirtumas ar čia svarbu?"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "kaffe.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


db.init_app(app)


@login_manager.user_loader
def load_user(vartotojo_id):
    return User.query.get(int(vartotojo_id))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("index"))
        else:
            flash("Login failed. Check e-mail and password.", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = forms.SigninForm()
    if form.validate_on_submit():
        cripted_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=cripted_password,
        )
        db.session.add(user)
        db.session.commit()
        flash("Login successful. Please login.", "success")
        return redirect(url_for("login"))
    return render_template("signin.html", title="Signin", form=form)

@app.route("/menu")
def menu():
    categories = FoodCategory.query.all()
    foods_by_category = {category.category_name: Food.query.filter_by(category=category).all() for category in categories}
    return render_template("menu.html", foods_by_category=foods_by_category)

# @app.route("/setup")
# def setup():
#     add_food_categories()
#     add_food()
#     return render_template("index.html")

@app.route('/calendar')
def calendar_events():
    
    try:
        events = Event.query().all()
        rows = []
        for event in events:
            row = {
                'id': event.id,
                'title': event.title,
                'url': event.url,
                'class': event.class_,
                'start': int(event.start_date.timestamp()) * 1000,
                'end': int(event.end_date.timestamp()) * 1000
            }
            rows.append(row)
        resp = jsonify({'success': 1, 'result': rows})
        resp.status_code = 200
        return render_template("calendar.html", resp=resp)
    except Exception as e:
        print(e)
        resp = jsonify({'success': 0, 'error': str(e)})
        resp.status_code = 500
        return render_template("calendar.html", resp=resp)
    

@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
