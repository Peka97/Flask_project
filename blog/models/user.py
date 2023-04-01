from sqlalchemy import Column, Integer, String, Boolean
from flask_login import UserMixin

from blog.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    articles = db.relationship('Article')

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
