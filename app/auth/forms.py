from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    title=StringField('Blog Title',validators=[Required()])
    content= TextAreaField('Make a blog', validators=[Required()])
    SubmitField=SubmitField('submit blog')
    
    
class CommentsForm(FlaskForm):
    comments= TextAreaField(validators=[Required()])
    submit = SubmitField('submit blog')
    
class UpdateProfile(FlaskForm):
    bio= TextAreaField('Create your bio',validators=[Required()])
    submit=SubmitField('submit')