from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
import app


class SigninForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    email = StringField("E-mail", [Email()])
    password = PasswordField("Password", [DataRequired()])
    confirm_password = PasswordField(
        "Repeat password to confirm", [EqualTo("Password", "Password must match.")]
    )
    submit = SubmitField("Sign In")

    def validate_email(self, email):
        user = app.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email already has been used")


class LoginForm(FlaskForm):
    email = StringField("E-mail", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log In")