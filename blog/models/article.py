from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from blog.models.database import db
from blog.models.user import Author
from blog.models.article_tag import article_tag_association_table


class Article(db.Model):
    """Article Model of Database

    Args:
        id (Integer): ID of article
        author (String): Author of article
        header (String): Header of article
        content (String): Content of article

    Returns:
        None
    """
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
    header = Column(String(80))
    content = Column(String(9999))

    author = db.relationship('Author', back_populates='articles')
    tags = db.relationship(
        "Tag",
        secondary=article_tag_association_table,
        back_populates="articles",
    )

    def __repr__(self):
        return f"<Article #{self.id}>"
