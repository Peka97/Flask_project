from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import User
from blog.views.articles import get_random_cat


users_app = Blueprint("users_app", __name__,
                      url_prefix='/users', static_folder='../static')


@users_app.route('/', methods=['GET'], endpoint='list')
def users_list():
    users = User.query.all()
    return render_template("/users/list.html", users=users)


@users_app.route('/index', methods=['GET'], endpoint='index')
def index():
    return render_template("/index.html")


@users_app.route("/<user_id>", methods=['GET'], endpoint='details')
def get_user(user_id: str):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template("/users/details.html", user=user, image=get_random_cat)


@users_app.errorhandler(404)
def handler_404(error):
    return f'<h1>404: Page Not Found<h1><h3>Check your URL<h3>'
