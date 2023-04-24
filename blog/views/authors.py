from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models.user import Author
from blog.models.article import Article
from blog.views.articles import get_random_cat


authors_app = Blueprint("authors_app", __name__,
                        url_prefix='/authors', static_folder='../static')


@authors_app.route('/', methods=['GET'], endpoint='list')
def authors_list():
    authors = Author.query.all()
    return render_template("/authors/list.html", authors=authors)


@authors_app.route("/<author_id>", methods=['GET'], endpoint='details')
def author_details(author_id: str):
    author: Author = Author.query.filter_by(id=author_id).one_or_none()
    if author is None:
        raise NotFound(f"Author #{author_id} doesn't exist!")
    return render_template("/authors/details.html", author=author, image=get_random_cat)


@authors_app.errorhandler(404)
def handler_404(error):
    return f'<h1>404: Page Not Found<h1><h3>Check your URL<h3>'
