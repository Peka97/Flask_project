import requests

from flask import Blueprint, render_template

from blog.models.user import User
from blog.models.article import Article


articles_app = Blueprint("articles_app", __name__,
                         url_prefix='/articles', static_folder='../static')


def get_random_cat():
    return 'http://placekitten.com/200/200'


@articles_app.route("/", methods=['GET'], endpoint='list')
def articles_list():
    users = User.query.all()
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles, users=users, image=get_random_cat)


@articles_app.route("/<id>", methods=['GET'], endpoint='details')
def articles_details(id: str):
    article = Article.query.filter(Article.id == id).all()[0]
    user = User.query.filter(User.id == article.author_id).all()[0]
    return render_template("articles/details.html", article=article, user=user, image=get_random_cat)
