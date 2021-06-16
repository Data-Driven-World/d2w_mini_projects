from app import db
from app import login
from datetime import datetime 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #####################################################
    # Your code here
    # Add winning column as integer, with default value 0
    # Add draw column as integer, with default value 0
    # Add score column as integer, with default value 0
    ######################################################

    winning = None
    draw = None
    score = None

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username:}>'

class State(db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.TIMESTAMP)
    ##########################################################
    # Your code here
    # Add a column for the cell as a 9 character string length
    # Add a column to store for the mark of the player
    #  this should be a single string character
    #########################################################
    cell = None
    mark = None   
