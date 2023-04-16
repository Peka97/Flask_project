from sqlalchemy import Column, Integer, String

from blog.models.database import db
from blog.models.article_tag import article_tag_association_table


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    articles = db.relationship(
        "Article",
        secondary=article_tag_association_table,
        back_populates="tags",
    )
