from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields


class UserSchema(Schema):
    class Meta:
        type_ = "user"
        self_view = "user_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "user_list"

    id = fields.Integer(as_string=True)
    first_name = fields.String(allow_none=False)
    last_name = fields.String(allow_none=False)
    username = fields.String(allow_none=False)
    email = fields.String(allow_none=False)
    is_staff = fields.Boolean(allow_none=False)

    author = Relationship(
        nested="AuthorSchema",
        attribute="author",
        related_view="author_detail",
        related_view_kwargs={"id": "<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False,
    )


class AuthorSchema(Schema):
    class Meta:
        type_ = "author"
        self_view = "author_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "author_list"

    id = fields.Integer(as_string=True)

    user = Relationship(
        nested="UserSchema",
        attribute="user",
        related_view="user_detail",
        related_view_kwargs={"id": "<id>"},
        schema="UserSchema",
        type_="user",
        many=False,
    )
    articles = Relationship(
        nested="ArticleSchema",
        attribute="articles",
        related_view="article_detail",
        related_view_kwargs={"id": "<id>"},
        schema="ArticleSchema",
        type_="article",
        many=True,
    )
