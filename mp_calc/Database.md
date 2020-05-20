# Using SQLAlchemy and Flask In This Mini Project 2

## Pre-Requisite

This notes will explain some of the codes in mini project 2 that interacts with the database using SQLAlchemy and Flask. However, it is useful that you go through these two tutorials:
- [The Flask Mega-Tutorial Part III: Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
- [Flask Mega Tutorial Part IV: Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) 

We will not explain the explanation that is already written in that tutorial.

## Config File and db Object

One change from the previous mini project is the present of `config.py` in the root folder. 

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-secret-key'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or\
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
```

This configuration file is needed by SQLAlchemy. The way it is written is as a class `Config`. This class is imported inside `app/__init__.py`.

```python
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
```

Notice that after we create the Flask application called `application`, we call `application.config.from_object(Config)`. 

After the configuration, we can then create the `SQLAlchemy` instance from `application` and assign the name `db`. We will use this `db` object instance when we interact with the database in our Python code.

The last line is for convenient purpose as we use Flask-Migrate package to migrate the database whenever we change our model or table.

## Model, View, and Controller

Flask allows you to write your project using [Model-View-Controller (MVC)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) software design pattern. 

![](https://www.dropbox.com/s/1akl7cvoejwenpc/400px-MVC-Process.png?raw=1)

In using MVC design pattern, we separate our codes into three main components: 
- Model: is the main component of the pattern containing the data structures. The model should be independent of the user interface.
- View: is what the user sees and represents information to the user.
- Controller: is what manipulates the data based on the user interaction with the user interface.

In our mini project, we have the following files where we write all these components:
- `models.py`: contains our model which defines all the table in our SQL database.
- `templates` folder: contains all the HTML files that provide the views to the users.
- `routes.py`: contains the view controllers. Some view controllers interact with the model.

## Models

Our database tables have the following relationships:

![](https://www.dropbox.com/s/6gb6nvaujsvevab/models_diagram.png?raw=1)

You may want to look into this diagram and open `models.py` at the same time.

## Tables in models.py

The `User` class in `models.py` has `username` and `password_hash` as its attributes. In our code, we name this table with a lowercase name `user` table. The table `user` has one-to-many relationship with the `question` table. Every question has an author of that question. 

```python
class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, 
                   primary_key=True)
	username = db.Column(db.String(64), 
                         index=True, 
                         unique=True)
	password_hash = db.Column(db.String(128))
	questions = db.relationship('Question', 
                                backref='from_user', 
                                lazy='dynamic')
	challenges = db.relationship('Challenge', 
                                 secondary=association_table, 
                                 backref=db.backref('to_user'), 
                                 lazy='dynamic')
	records = db.relationship('TimeRecord', 
                              backref=db.backref('user_challenge'), 
                              lazy='dynamic')

```

The `user` table has many-to-many relationship with the `challenge` table through the `association` table. This means that one user can have many challenges and one challenge can be sent to many users. 

When a user attempt one challenge, it will be recorded inside `timerecord` table. Each entry in `timerecord` table contains information of which challenge and who the user who submitted the answer. It also records the `elapsed_time`. 

When a user creates a question, it has to fill in the `expression` field. The server then calculates the `answer` using your `EvaluateExpression` class which is part of your Exercise 2. Moreover, a user chooses another users to create a challenge for them and so it creates one entry in the `challenge` table. This means that `question` table and `challenge` table has a one-to-one relationship.

For one challenge, different users may attempt to answer and creates different `timerecord` entries. The same user can attempt it several times as well. This means that the `challenge` table has a one-to-many relationship with the `timerecord` table since one challenge can have many records for the submissions.

See `models.py` and refer to the following documentations in the References to understand the rest of the codes.

### References

- [SQLAlchemy Basic Relationship](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html)
- [The Flask Mega-Tutorial Part IV: Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

## Querying the Database

We will explain how we use the `db` object inside `app/routes.py`.

### Users and Hall of Fame Page - Querying All Entries

The controller for the Users page is defined inside `users()` function in `routes.py`. 

```python
def users():
	users = User.query.all()	
	mergesort(users, lambda item: item.username)
	usernames = [u.username for u in users]
	return render_template('users.html', title='Users',
							users=usernames)
```

- The first line uses the class `User` defined in `models.py`. `User` is an instance of `db.Model` which has a `query` object as its attribute. This `query` object has a method `all()`. What this line does is to query the `user` table and retrieve all its entries.
- In the second and third line, we actually use the `username` attribute of the `User` object. Recall in `models.py` that `username` is one of the attributes defined in the class `User`. 

Similarly, we can see a similar code to query all entries in the Hall of Fame page. You can check the function `halloffame()` inside `routes.py`.

```python
def halloffame():
	challenges = Challenge.query.all()
```

- The above line retrieves all the challenges in the `challenge` table.

### Question and Challenge Pages - Adding Entry into Database

Let's go to the controller for the Question page. This allows user to create a question and store it into the database. 

```python
def questions():
	questions = current_user.questions.all()
    ...
	users = User.query.all()
	userlist = [(u.username, u.username) for u in users]
    ...
```

- In the first line, the variable `current_user` contains the `User` object which is logged into the page. If you refer to `User` class definition in `models.py` you will see a `questions` field being defined. Accessing this attribute gives you a query object that allows you to access the `question` table for that user. Since a `query` object has a method `all()` you can use it to get all the questions created by the current user.
- The second and third lines are similar to the Users page where we retrieve all the users and their usernames from the `user` table.

```python
if form.validate_on_submit():
		question = Question(expression=form.expression.data)
		evalans = EvaluateExpression(form.expression.data)
		question.answer = evalans.evaluate()
		question.author = current_user.id 
		challenge = Challenge(question=question)
		username_to = []
		for name in form.assign_to.data:
			username_to.append(User.query.filter_by(username=name).first())

		challenge.to_user = username_to
		db.session.add(question)
		db.session.add(challenge)
		db.session.commit()
```

- When the user submit the question by clicking the submit button, the value of `form.validate_on_submit()` is `True`.
- Upon submission, we want to create a new entry into the `question` table. 
- To create a new entry, we first create a new object instance: `question = Question(expression=form.expression.data)` where we initialize the `expression` with the string entered by the user in the form.
- We then create the object instance for `EvaluateExpression` so that we can call its `evaluate()` method. This will give us the answer which we set here: `question.answer = evalans.evaluate()`. 
- We also want to create another record in the `challenge` table. Therefore, we create the instance: `challenge = Challenge(question=question)`. We set the `question` field in the `challenge` table with the newly created `question`.
- The next few lines reads the names chosen in the field where the challenge is to be sent to and retrieve the `User` object based on the `username`: `User.query.filter_by(username=name).first()`. Note that the `query` object has another method called `filter_by()` which can be used to retrieve the records based on certain filter conditions. The `first()` method returns the first `User` object found by the query that matches the filter condition.
- To modify the database, we have to add a `session` and `commit()` them. This is shown in the last three lines where we add a new entry to the `question` and `challenge` table and call `commit()`.

```python
db.session.add(question)
db.session.add(challenge)
db.session.commit()
```

We can see similar things inside the Challenge page controller in `challenge()` function inside `routes.py`. When a user submit an anwer, the following code will be executed:

```python
	if form.validate_on_submit():
		record = TimeRecord()
		record.elapsed_time = int(form.elapsed_time.data)
		record.challenge_id = int(form.challenge_id.data)
		record.user_id = current_user.id
		answer = form.answer.data
		challenge = Challenge.query.filter_by(id=form.challenge_id.data).first()
		if int(answer) == int(challenge.question.answer):
			db.session.add(record)
			db.session.commit()
```

- The first line creates a `TimeRecord` object after a user submit an answer.
- The second and third lines initialize the `elapsed_time` and `challenge_id` attributes of the `TimeRecord` object from the data in the submitted form. The next line initialize the `user_id` attribute using the `current_user` object's `id`. 
- We then want to check if the answer is correct. So it retrieves the answer submitted by the user, i.e. `answer = form.answer.data`, with the one from the database.
- We get the answer fro the database by first finding the entry in the `challenge` table that matches the `challenge_id`: `Challenge.query.filter_by(id=form.challenge_id.data).first()`.
- Since every entry in `challenge` id table is associated with an entry in the `question` table, we can access the questions' answer using: `challenge.question.answer`.
- The last two lines above add the `TimeRecord` object into the database.

### References

- [Query API](https://docs.sqlalchemy.org/en/13/orm/query.html)
- [Session Basics](https://docs.sqlalchemy.org/en/13/orm/session_basics.html)
- [The Flask Mega-Tutorial Part III: Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
- [Flask MegaTutorial Part IV: Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)


