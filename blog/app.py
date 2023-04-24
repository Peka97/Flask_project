import os

from flask import Flask
from flask_migrate import Migrate

from blog.models.database import db
from blog.views import users, articles, auth, authors
from blog.views.auth import login_manager
from blog.admin.admin import admin
from blog.api import init_api


migrate = Migrate()


def create_app() -> Flask:
    flask_app = Flask(__name__)
    reg_blueprints(flask_app)
    config_and_connect_db(flask_app)
    return flask_app


def config_and_connect_db(app: Flask) -> None:
    cfg_name = os.environ.get("CONFIG_NAME") or "ProdConfig"
    app.config.from_object(f"blog.config.{cfg_name}")

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    admin.init_app(app)
    login_manager.init_app(app)
    api = init_api(app)


def reg_blueprints(app: Flask) -> None:
    app.register_blueprint(users.users_app)
    app.register_blueprint(authors.authors_app)
    app.register_blueprint(articles.articles_app)
    app.register_blueprint(auth.auth_app)
