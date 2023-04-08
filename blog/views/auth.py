from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from blog.models import User
from blog.forms.user import UserRegisterForm, UserLoginForm
from blog.models.database import db


class Auth:
    active = ''
    show = ''
    selected = ''


auth_app = Blueprint("auth_app", __name__, url_prefix="/auth")
login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


def switch_flag(login=None, register=None):
    if login:
        login, register = Auth(), Auth()
        login.active = 'active'
        login.show = 'show active'
        login.selected = 'true'
        register.active = ''
        register.show = ''
        register.selected = 'false'
    else:
        login, register = Auth(), Auth()
        login.active = ''
        login.show = ''
        login.selected = 'false'
        register.active = 'active'
        register.show = 'show active'
        register.selected = 'true'
    return login, register


@ auth_app.route("/logout/", endpoint="logout")
@ login_required
def logout():
    logout_user()
    return redirect(url_for("users_app.index"))


@ auth_app.route("/secret/")
@ login_required
def secret_view():
    return "Super secret data"


@auth_app.route("/register/", methods=["GET", "POST"], endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect("users_app.index")
    error = None
    form = UserRegisterForm(request.form)
    login, register = switch_flag(register=True)

    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            print(1)
            form.username.errors.append("username already exists!")
            return render_template("auth/auth.html", form=form, login=login, register=register)

        if User.query.filter_by(email=form.email.data).count():
            print(2)
            form.email.errors.append("email already exists!")
            return render_template("auth/auth.html", form=form, login=login, register=register)
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            is_staff=False,
        )

        user.password = form.password.data
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info("Created user %s", user)
            login_user(user)
            return redirect(url_for("users_app.index"))
    print(3)
    print(error)
    return render_template("auth/auth.html", form=form, error=error, login=login, register=register)


@auth_app.route("/", methods=["GET", "POST"], endpoint="login")
@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("users_app.index"))

    login, register = switch_flag(login=True)
    form = UserLoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        print('POST')
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            print('USER IS NONE')
            return render_template("auth/auth.html", form=form, error="username doesn't exist", login=login, register=register)

        if not user.validate_password(form.password.data):
            print('NOT VALIDATE PASSWORD')
            return render_template("auth/auth.html", form=form, error="invalid username or password", login=login, register=register)

        login_user(user)
        print('LOGIN AND REDIRECT')
        return redirect(url_for("users_app.index"))
    print('JUST RENDER')
    return render_template("auth/auth.html", form=form, login=login, register=register)


__all__ = [
    "login_manager",
    "auth_app",
]
