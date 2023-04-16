from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, validators


class CreateArticleForm(FlaskForm):
    header = StringField('Header', [validators.DataRequired()],)
    content = TextAreaField('Content', [validators.DataRequired()],)
    author = SelectMultipleField("Users", coerce=int)
    tags = SelectMultipleField("Tags", coerce=int)

    submit = SubmitField("Publish")
