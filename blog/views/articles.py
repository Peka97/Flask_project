from flask import Blueprint, render_template

from ..models.models import get_users, get_articles

articles_app = Blueprint("articles_app", __name__,
                         url_prefix='/articles', static_folder='../static')


@articles_app.route("/", methods=['GET'], endpoint='list')
def articles_list():
    users = get_users()
    articles = get_articles()
    return render_template("articles/list.html", articles=articles, users=users)


@articles_app.route("/<pk>", methods=['GET'], endpoint='details')
def articles_details(pk: str):
    article = get_articles()[pk]
    user_id = article['author']
    user = get_users()[user_id]
    return render_template("articles/details.html", article=article, user=user)
