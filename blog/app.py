from flask import Flask, render_template
from blog.views import users, articles


def create_app() -> Flask:
    flask_app = Flask(__name__)
    reg_blueprints(flask_app)
    return flask_app


def reg_blueprints(app: Flask) -> None:
    app.register_blueprint(users.users_app)
    app.register_blueprint(articles.articles_app)
