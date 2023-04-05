from sqlalchemy.exc import InvalidRequestError, IntegrityError

from blog.app import create_app
from blog.models.database import db
from blog.models.user import User
from blog.models.article import Article


app = create_app()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("DB was created")


@app.cli.command("drop-db")
def init_db():
    db.drop_all()
    print("DB was dropped")


@app.cli.command("create-users")
def create_users():

    users = [
        User(username="admin", is_staff=True),
        User(username="James", email='test@ya.ru'),
        User(username="Ben"),
        User(username="Anna")
    ]

    db.session.query(User).delete()

    for user in users:
        db.session.add(user)
    db.session.commit()

    print("Created users:\n", "\n".join([user.username for user in users]))


@app.cli.command("create-articles")
def create_articles():
    articles = [
        Article(author_id=2, header='This is awesome title!',
                content='Some realy awesome, believe me. True. I\'m not lie.'),
        Article(author_id=3, header='Another one awesome header!',
                content='Wow! Look at this. I\'m seriously.')
    ]

    db.session.query(Article).delete()

    for article in articles:
        db.session.add(article)
    db.session.commit()

    print("Created articles:\n", "\n".join(
        [article.header for article in articles]))


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
