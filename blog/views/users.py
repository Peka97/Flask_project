from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound


from ..models.models import get_users, get_articles


users_app = Blueprint("users_app", __name__,
                      url_prefix='/users', static_folder='../static')


@users_app.route('/', methods=['GET'], endpoint='list')
def users_list():
    return render_template("/users/list.html", users=get_users())


@users_app.route("/<pk>", methods=['GET'], endpoint='details')
def get_user(pk: str):
    try:
        user = get_users()[pk]
        user['articles'].extend(
            [id for id, item in get_articles().items() if item['author'] == pk])
        return render_template("/users/details.html", user=user, articles=get_articles())
    except KeyError as err:
        return NotFound(f"User with ID {pk} doesn't exist!")


@users_app.errorhandler(404)
def handler_404(error):
    return f'<h1>404: Page Not Found<h1><h3>Check your URL<h3>'
