from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, IntegerField, HiddenField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', 
							   validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

class CreateQuestionForm(FlaskForm):
	expression = StringField('Math Expression', validators=[DataRequired()])
	assign_to = SelectMultipleField('Send To', validators=[DataRequired()])
	submit = SubmitField('Submit')


class ChallengeAnswerForm(FlaskForm):
	challenge_id = HiddenField('Challenge ID')
	answer = StringField('Answer', validators=[DataRequired()])
	elapsed_time = HiddenField('Elapsed Time')
	submit = SubmitField('Submit')




	