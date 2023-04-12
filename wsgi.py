from sqlalchemy.exc import InvalidRequestError, IntegrityError
from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.models.database import db
from blog.models.user import User
from blog.models.user import Author
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
        User(
            username="admin",
            password=generate_password_hash('12345'),
            is_staff=True
        ),
        User(
            username="James",
            password=generate_password_hash('12345'),
            email='test@ya.ru'
        ),
        User(username="Ben", password=generate_password_hash('12345')),
        User(username="Anna", password=generate_password_hash('12345'))
    ]

    db.session.query(User).delete()

    for user in users:
        db.session.add(user)
    db.session.commit()

    print("Created users:\n", "\n".join([user.username for user in users]))


@app.cli.command("create-articles")
def create_articles():
    articles = [
        Article(author_id=1, header='This is awesome title!',
                content='Some realy awesome, believe me. True. I\'m not lie.'),
        Article(author_id=2, header='Another one awesome header!',
                content='Wow! Look at this. I\'m seriously.')
    ]

    db.session.query(Article).delete()

    for article in articles:
        db.session.add(article)
    db.session.commit()

    print("Created articles:\n", "\n".join(
        [article.header for article in articles]))


@app.cli.command("create-authors")
def create_authors():
    authors = [
        Author(user_id=2),
        Author(user_id=3)
    ]

    db.session.query(Author).delete()

    for author in authors:
        db.session.add(author)
    db.session.commit()

    print("Created articles:\n", "\n".join(
        [str(author.id) for author in authors]))


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
