from blog.models import User
from flask import Flask

from blog.views import users, articles, auth
from blog.models.database import db
from blog.views.auth import login_manager


def create_app() -> Flask:
    flask_app = Flask(__name__)
    reg_blueprints(flask_app)
    config_and_connect_db(flask_app)
    return flask_app


def config_and_connect_db(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "abcdefg123456"
    db.init_app(app)
    login_manager.init_app(app)


def reg_blueprints(app: Flask) -> None:
    app.register_blueprint(users.users_app)
    app.register_blueprint(articles.articles_app)
    app.register_blueprint(auth.auth_app)
