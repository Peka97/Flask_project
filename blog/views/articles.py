import requests

from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

from blog.models.database import db
from blog.models.user import User, Author
from blog.models.article import Article
from blog.models.tag import Tag
from blog.forms.article import CreateArticleForm


articles_app = Blueprint("articles_app", __name__,
                         url_prefix='/articles', static_folder='../static')


def get_random_cat():
    return 'http://placekitten.com/200/200'


@articles_app.route("/", methods=['GET'], endpoint='list')
def articles_list():
    authors = Author.query.all()
    articles: Article = Article.query.all()
    for article in articles:
        print(article.author_id)
    return render_template("articles/list.html", articles=articles, authors=authors, image=get_random_cat)


@articles_app.route("/<id>", methods=['GET'], endpoint='details')
def articles_details(id: str):
    article = Article.query.filter(Article.id == id).options(
        joinedload(Article.tags)).one_or_none()
    author = Author.query.filter(Author.id == article.author_id).one_or_none()
    return render_template("articles/details.html", article=article, author=author, image=get_random_cat)


@ articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@ login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.author.choices = [(user.id, user.username)
                           for user in User.query.order_by("username")]
    form.tags.choices = [(tag.id, tag.name)
                         for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        article = Article(header=form.header.data.strip(),
                          content=form.content.data)
        if form.tags.data:  # если в форму были переданы теги (были выбраны)
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            article.tags.extend([tag for tag in selected_tags])
        if current_user.author:
            # use existing author if present
            article.author_id = current_user.author.id
        else:
            # otherwise create author record
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author_id = author.id

        db.session.add(article)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article=article, author=author, image=get_random_cat))
    return render_template("articles/create.html", form=form, error=error)
