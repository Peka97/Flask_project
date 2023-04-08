from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import check_password_hash
from flask_login import UserMixin

from blog.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, default="", server_default="")

    first_name = Column(String(255), default=None)
    last_name = Column(String(255), default=None)
    is_staff = Column(Boolean, nullable=False, default=False)
    articles = db.relationship('Article')

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

    def validate_password(self, password):
        return check_password_hash(self.password, password)
