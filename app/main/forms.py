from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Required
from app.models import Blog,Comment

class NewblogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    blog = TextAreaField('Blog', validators=[DataRequired()])
    submit = SubmitField('Add Blog', validators=[DataRequired()])

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment something',validators = [Required()])
    submit = SubmitField('Post Comments')
