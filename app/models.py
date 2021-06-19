from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin, confirm_login,current_user

@login_manager

def load_user(user_id):
    return User.query.get(int(user_id))


class Quote:
    '''
    Quotes class to define class object
    '''
    def __init__(self, quote, author, id):
        self.quote = quote
        self.author = author
        self.id = id
        
class User(db.Model,UserMixin):
    __tablename__ ='users'
    
    id = Column(db.Integer,primary_key=True)