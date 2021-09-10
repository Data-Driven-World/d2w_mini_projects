from app import application
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from flask import request 
from flask_socketio import emit
from app import socketio
import random
from datetime import datetime
from app.serverlibrary import TicTacToe, Move, mergesort
from app.models import User, State
from app import db


########################
# Setup for global data
#######################

marks = ('X', 'O')
players = {}

#############################################
# Put any other helper functions you use here
#############################################

def other_mark(mark):
    return 'X' if mark == 'O' else 'O'

def calculate_score(winning, draw):
    return winning * 10 + draw * 5

def update_score(status):
    if status == 'win':
        if current_user.winning == None:
            current_user.winning = 1
        else:
            current_user.winning += 1
    elif status == 'draw':
        if current_user.draw == None:
            current_user.draw = 1
        else:
            current_user.draw += 1
    score = calculate_score(current_user.winning, current_user.draw)
    current_user.score = score
    db.session.commit()
    
def process_winning(winner=None, status='lose'):
    user = current_user.username
    # if there is a winner, 
    # emit signal 'winning' and pass on the winner as the data
    if winner != None:
        emit('winning', {'data': winner})
        
    # if the status is not lose, update the score
    if status != 'lose':
        update_score(status)
        
    # reset the TicTacToe's board
    players[user].reset()
        
    # update DB with a clean board
    data = State(user_id=current_user.id,
                 time=datetime.now(),
                 cell=players[user].board_to_str,
                 mark=players[user].mark)
    db.session.add(data)
    db.session.commit() 
#######################################
# These are event handler for SocketIO
######################################

################
# Exercise 6
###############

########
# Task 1
########

@socketio.on('startconnect', namespace='/tictactoe')
def handle_connect(message):
    print("Connected")
    mark = message["mark"]

    all_data = State.query.filter_by(user_id=current_user.id).all()
    if len(all_data) < 1:
        data = State(user_id=current_user.id,
                     time=datetime.now(),
                     cell='_________',
                     mark=mark)
        db.session.add(data)
        db.session.commit()
    last_data = State.query.filter_by(user_id=current_user.id).all()[-1]
    players[current_user.username] = TicTacToe(last_data.cell,
                                           last_data.mark)
    emit('afterconnect', {'data': last_data.cell})   

@socketio.on('clicked', namespace='/tictactoe')
def handle_click(message):
    # get the user name, mark and the clicked cell from message
    # check clientlibrary.py for the message sent in 
    # event 'clicked'
    user = message['Username']
    mark = message['mark']
    
    # set the computer mark to be the opposite of that of player
    computer = other_mark(mark)
    
    # get the cell number from 'id' inside message
    # Note that the format for the cell string is 'cellXY'
    # extract only the last two characters
    cell = message['id'][-2:]
    
    # update TicTacToe's object using the mark at the approriate row and col
    players[user].update(int(cell[0]), int(cell[1]), mark)
    
    # check if there is any winner
    # you can call checkwinning method inside TicTacToe's object
    winner = players[user].checkwinning()
    
    # if there is a winner
    if winner != None:
        # process the winning state, and update the score
        process_winning(winner, status='win')
        
        # exit the function
        return

    # if there is no winner, check if there is any move lefts
    # get the boolean value by calling a method inside TicTacToe
    can_move = players[user].any_moves_left()
    # if the computer can make a move
    if can_move:
        # find the best move for the computer
        next_move = players[user].find_best_move(computer)
        
        # update the board with the best move
        players[user].update(next_move.row, next_move.col, computer)
        
        # check if there is a winner
        # call a method inside TicTacToe
        winner = players[user].checkwinning()
        
        # emit signal 'computer_move' to update the page
        emit('computer_move', {'data': {'row':next_move.row, 'col':next_move.col}})
        
        # insert a new document to db on the board's status
        # create an object instance of State. Replace the None.
        data = State(user_id=current_user.id,
                     time=datetime.now(),
                     cell=players[user].board_to_str,
                     mark=mark)
        # write the code to add the data to the session
	    db.session.add(data)
        # write the code to commit the session to the database
	    db.session.commit()

        # check if there is a winner
        if winner != None:
            # process winning state, 
            # but do not update the score since computer wins
            process_winning(winner, status='lose')
            
            # exit the function
            return

    else:
        # if there is no winner
        # update the score as draw
        process_winning(winner=None, status='draw')
        return

#######################
# Flask route handlers
######################

#####################
# Exercise 5
####################

@application.route('/single', methods=['GET', 'POST'])
@login_required
def single():
    user = current_user.username
    if request.method == 'POST':
        # reset the tictactoe board to the original state
        # the TicTacToe's object is stored in players[user] variable
        players[user].reset()
        
        # get the mark for the current player
        player_mark = players[user].mark
        
        # get the mark for the computer player
        computer_mark = other_mark(player_mark)
        
        # update database
        # the 'cell' should be the state of the board
        #  which can be obtained from the tictactoe object
        data = State(user_id=current_user.id,
                     time=datetime.now(),
                     cell=players[user].board_to_str,
                     mark=player_mark)
        # add the data to the session
	    db.session.add(data)
        # commit the session to the database
	    db.session.commit()
        return render_template('single.html', title='Single Player', player=player_mark, computer=computer_mark)
    else:
        if user not in players:
            # set player mark randomly
            player_mark = random.choice(marks)
            
            # create the object instant TicTacToe using
            # the player's mark
            players[user] = TicTacToe(mark=player_mark)

            # set the computer mark
            computer_mark = other_mark(player_mark)
        else:
            # if user is already in the dictionary, use the mark there
            # the TicTacToe object is stored inside players[user] variable
            player_mark = players[user].mark
            
            # set the computer mark
            computer_mark = other_mark(player_mark)
        return render_template('single.html', title='Single Player', player=player_mark, computer=computer_mark)


@application.route('/records')
def records():
    users = User.query.order_by(User.score).all()[::-1]
    return render_template('records.html', title="Your Records", records=users
)


@application.route('/users')
@login_required
def users():
    users = User.query.all()
    mergesort(users, lambda item: item.username)
    usernames = [u.username for u in users]
    return render_template('users.html', title='Users',
           users=usernames)

@application.route('/')
@application.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

