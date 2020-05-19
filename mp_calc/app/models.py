from app import db
from app import login
from datetime import datetime 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


association_table = db.Table('association', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	questions = db.relationship('Question', backref='from_user', 
								lazy='dynamic')
	challenges = db.relationship('Challenge', secondary=association_table,
								backref=db.backref('to_user'),
								lazy='dynamic')
	records = db.relationship('TimeRecord', 
								backref=db.backref('user_challenge'),
								lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f'<User {self.username:}>'


class Question(db.Model):
	__tablename__ = 'question'
	id = db.Column(db.Integer, primary_key=True)
	expression = db.Column(db.String(255))
	answer = db.Column(db.Integer)

	author = db.Column(db.Integer, db.ForeignKey('user.id'))
	challenge = db.relationship("Challenge", uselist=False, back_populates="question")
	
	def __repr__(self):
		return f'<Question {self.expression:}>'	

	
class Challenge(db.Model):
	__tablename__ = 'challenge'
	id = db.Column(db.Integer, primary_key=True)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
	question = db.relationship("Question", back_populates="challenge")
	records = db.relationship("TimeRecord")
	
	def __repr__(self):
		return f'<Question {self.question.expression:} for {self.to_user:} from {self.question.from_user:}>'	


class TimeRecord(db.Model):
	__tablename__ = 'timerecord'
	id = db.Column(db.Integer, primary_key=True)
	elapsed_time = db.Column(db.Integer)
	challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#db.create_all()
