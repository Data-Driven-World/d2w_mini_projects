# Mini Project 3: Tic Tac Toe App

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Mini Project 3: Tic Tac Toe App](#mini-project-3-tic-tac-toe-app)
    - [Learning Objectives](#learning-objectives)
    - [Setup](#setup)
        - [Install Git](#install-git)
        - [Downloading Repository](#downloading-repository)
        - [Go to Mini Project 3 Folder](#go-to-mini-project-3-folder)
    - [Create Virtual Environment (Windows)](#create-virtual-environment-windows)
    - [Create Virtual Environment (MacOS/Linux)](#create-virtual-environment-macoslinux)
    - [Combined (Windows/Mac/Linux)](#combined-windowsmaclinux)
        - [Install Python Packages](#install-python-packages)
    - [Exercise 1](#exercise-1)
        - [Brief Overview of Flask Project Structure](#brief-overview-of-flask-project-structure)
        - [Task 1](#task-1)
        - [Task 2](#task-2)
            - [Windows](#windows)
            - [MacOS](#macos)
    - [Exercise 2](#exercise-2)
        - [Task 1](#task-1-1)
        - [Task 2](#task-2-1)
        - [Task 3](#task-3)
        - [Task 4](#task-4)
            - [Vocareum](#vocareum)
            - [Local Computer](#local-computer)
    - [Exercise 3](#exercise-3)
        - [Task 1](#task-1-2)
        - [Task 2](#task-2-2)
    - [Exercise 4](#exercise-4)
        - [Task 1](#task-1-3)
        - [Task 2](#task-2-3)
        - [Task 3](#task-3-1)
        - [Task 4](#task-4-1)
        - [Task 5](#task-5)
        - [Task 6](#task-6)
        - [Task 7](#task-7)
        - [Task 8](#task-8)
    - [Exercise 5](#exercise-5)
    - [Exercise 6](#exercise-6)
        - [Task 1: Getting Familiar with SocketIO](#task-1-getting-familiar-with-socketio)
        - [Task 2: Handling Click](#task-2-handling-click)
    - [Expected Deliverable](#expected-deliverable)

<!-- markdown-toc end -->

## Learning Objectives
By the end of this mini project, you should be able to:
- write minimax algorithm using recursion

## Setup

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:
- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

### Downloading Repository
Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```shell
$ cd Downloads
$ git clone https://github.com/kurniawano/d2w_mini_projects.git
```

### Go to Mini Project 3 Folder

Once you have downloaded the repository, you can go to the repository and to the folder called `mp_tictactoe` for this mini project.

```shell
$ cd d2w_mini_projects/mp_tictactoe
$ ls
```

The last command should output the following:

```shell
app
application.py
config.py
requirements.txt
```

This handout can be found in the file `Readme.md`.

## Create Virtual Environment (Windows)

**You should open Anaconda Prompt to do the following steps.**

In the following steps, the Windows prompt will be represented by:
```shell
>
```
Go to the root folder `mp_tictactoe`.
```shell
> cd %USERPROFILE%\Downloads\d2w_mini_projects\mp_tictactoe
```
From the root folder, i.e. `mp_tictactoe`, create virtual environment called `virtenv`.

```shell
> python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment.
```shell
> virtenv\Scripts\activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) folder>
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
> deactivate
```

## Create Virtual Environment (MacOS/Linux)


In the following steps, the MacOS/Linux prompt will be represented by:
```shell
$
```

Go to the root folder `mp_tictactoe`. 
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_tictactoe
```

From the root folder, i.e. `mp_tictactoe`, create virtual environment called `virtenv`.

```shell
$ python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment. 

```shell
$ source virtenv/bin/activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) user$
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
$ deactivate
```
## Combined (Windows/Mac/Linux)

### Install Python Packages

Install the necessary packages for this mini project. From the root folder, i.e. `mp_tictactoe`, type the following:

For Windows:
```shell
> python -m pip install --upgrade pip 
> python -m pip install -U --force-reinstall -r requirements.txt
```

For MacOS/Linux: (For Linux, you might need to type pip3 instead)
```shell
$ python -m pip install --upgrade pip
$ python -m pip install -U --force-reinstall -r requirements.txt
```

The above steps will update pip and install the following packages:

- Flask
- Transcrypt 
- Flask-SQLAlchemy
- Flask-Migration
- Flask-Bootstrap4
- and some other packages

## Exercise 1

### Brief Overview of Flask Project Structure

The first file you will need to look at is `application.py`. Open that file using a text editor. You should see *less* lines here as compared to your previous project `mp_calc`. In this file, you see only the following:

```python
from app import application, db
from app.models import User, State

@application.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'State': State}

if __name__ == "__main__":
  application.run(host="0.0.0.0", port=8080, debug=True)
```

Notice the following differences:

- This project only imports `User` and `State` from `app.models` unlike the previous project which imports `User`, `Questions`, `Challenge`, and `TimeRecord`. The reason is that we only use two SQL tables (`User` and `State`) in this project. These tables is defined inside your `models.py` in `app` folder.
- under `make_shell_context()` function definition, we only return `db`, `User`, and `State` object. This is to use these three objects when we work on the flask shell.

Inside the `app` folder, we again have `__init__.py` file. In this file, we have added two lines as follows.

```python
from flask_socketio import SocketIO
.
.
.
socketio = SocketIO(application)
```
Those two lines are used to make use `Flask-SocketIO` which implements `SocketIO` API in Python. This enables you to have realtime, bi-directional communication between web clients and servers. It has two parts: a client-side library that runs in the browser, and a server side library. The code we have inside `__init__.py` is for the server side library. For the client-side library, we find the following codes in `app/templates/base.html`:
```html
<script src="//code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"></script>
```
which are needed to use `Socket.IO` library and JQuery library. More importantly, we can find some codes inside `app/templates/single.html`:
```html
<script type="text/javascript" charset="utf-8">
var socket;
var celldata;
$(document).ready(function(){
    namespace = '/tictactoe';
    socket = io(namespace);
    ...
});
</script>
```
We have written some Javascript codes for you to handle the following *events*:

- `afterconnect`: This custom event is called after the server side is ready and it fills the Tic Tac Toe cells with the data, i.e. either `_` or `X`, or `O`. 
- `computermove`: This custom event is called after computer has chosen its move and it will update the Tic Tac Toe cell with the computer's move. This function will call the function `update_computer(row, col, mark)` inside `clientlibrary.py` to update the HTML with the computer's move. This is part of Exercise 1 you need to do.
- `winning`: This custom event is called when there is a winner. It will call the function `winning(mark, winner)` inside `clientlibrary.py` to update the HTML with the status of the winner. This is part of Exercise 1 you need to do.

  Inside `app/templates/single.html`, just below the table, we have the following HTML code:
  ```html
  <h1><div id="winner" style='text-align:center'></div></h1>
  ```
  Currently, it is empty. There is no text between `<div>` and `</div>`But when the computer or the player wins the game, it should be replaced with either "You Win!" or "You Lose!". The function that is responsible to update this is `winning(mark, winner)` function inside `client_library.py`.

### Task 1

Open the following file: `app/static/clientlibrary.py`. 

- Edit `update_computer(row, col, player)` function by replacing the `None` in the codes. Your code should get the mark of the computer which is the opposite mark of the input argument `player` mark. This means that if the player is `X`, you should assign `O`, and vice versa. This function will be called when the computer has decided its move and is used to update the HTML to draw the computer's move.

  The cell id is in the following format: cellxy
  - where x is the row, and y is the column
  - x and y values are from 0 to 2
  For example, the cell in the middle of the Tic Tac Toe grid is given by 'cell11'.

- Edit `winning(player, winner)` function. This function should update the HTML tag `winner` with either "You Win!" or "You Lose!". Use `document.getElementById(id).innerText` to assign the text. The HTML tag id is "winner". 

- Edit `click_cell(username, row, col, mark)` function. This function is called when a user click a cell in the Tic Tac Toe grid. The first argument is the username. This is used by the server to update the database. The second and the third arguments are the row and the column (0 to 2) index where the user clicked. The last argument is the mark assigned to the user, i.e. either 'X' or 'O'. The function should:
    - create a string for the `cellid` variable which contains the `id` of the HTML tag to be modified.
    - update the Tic Tac Toe corresponding cell given by the row and column with the input argument `mark`. 
    - notify the server that the user has clicked a cell.


### Task 2

In this task, you need to compile the `clientlibrary.py` into a javascript file that will server the HTML files. 

#### Windows

To compile `clientlibrary.py`, first we need to go into the `static` folder.

```shell
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_tictactoe\app\static
> dir
```

The last command will list the file in that folder, and you should see:
```shell
clientlibrary.py
```

Run Transcrypt on `clientlibrary.py`:

```shell
python -m transcrypt -b -n clientlibrary
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. You should see `clientlibrary.js` created inside this folder. 

#### MacOS

To compile `library.py`, first we need to go into the `static` folder.

```shell
$ cd ~/Downloads/d2w_mini_projects/mp_tictactoe/app/static
$ ls
```

The last command will list the file in that folder, and you should see:
```shell
clientlibrary.py
```

Run Transcrypt on `clientlibrary.py`:

```shell
python -m transcrypt -b -n clientlibrary
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. 
You should see `clientlibrary.js` created inside this folder.

## Exercise 2

Now we are going to work with the database. We will use two tables. The first one is to keep a record of the users. The other one is a table to store state of the Tic Tac Toe board.

### Task 1

Let's start with the User table. We specify our tables in the `app/models.py`. Inside you will find the following code:

```python
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
```

The first four attributes are similar to the previous mini project. Your task is to create three more columns for the `winning`, `draw` and `score`:

- `winning`: is an Integer column to store how many times the user wins. Set its default value to 0.
- `draw`: is an Integer column to store how many times the user has a draw when playing against the computer. Set its default value to 0.
- `score`: is an Integer column that store the scores of the user based on the number the player wins and has a draw. 

*Hint:* Use the keyword argument `default=0` to specify the default value of the column. 

### Task 2
Now, we will create the State table. We can create another table that contains the following column:
- `id`, which is the primary key of the table
- `user_id`, which is the user id from `User` table that update the State table
- `time`, which is the time of the update
- `cell`, which is a string of 9 characters to store all the cell in a single string. 
- `mark`, which is to store the mark of the user used in the game

Note that we chose to use a single string to store the state of the Tic Tac Toe board in the database. For example, if we have the following board state:

```
board = [['X', 'O', '_'],
         ['O', 'X', '_'],
         ['X', 'O', '_']]
```
we can store the state of the board as a single string as follows.
```
board = 'XO_OX_XO_'
```

```python
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
```

We use an integer as the primary key for this table. The `user_id` is used to store which user that updates the table. We can use this to find all the updates by a particular user using the id. We also create a column called `time` which is of type `TIMESTAMP` to store the time of the update. The value should be of Python's `DateTime` format. 

Now, your task is to replace the `None`:

- Create a column `cell` which is of the type `String` and has the length of 9 characters. This is used to store the state of the board where each character is one cell in the board.
- Create a column `mark` which is of the type `String` and has the length of 1 character. This is used to store the type of the mark, i.e. either `X` or `O`. 


### Task 3

Now, we are going to create the database using Flask-Migrate tool. First, go to the root directory of your project. For example, if you download the repository to your user's `Download` folder, you can use the following.

Windows:
```dos
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_tictactoe
```
Mac OS:
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_tictactoe
```

Then, run the following command from the terminal:

```shell
flask db init
flask db migrate
flask db upgrade
```

- `init` command will initialize the database using SQLlite.
- `migrate` will create the migration scripts.
- `upgrade` will perform the database operations to create the tables.

### Task 4
You can try to run the web application now. First go to the root directory of your project. For example, 

Windows:
```dos
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_tictactoe
```
Mac OS:
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_tictactoe
```

Now you can run Flask.

#### Vocareum

If you use Vocareum terminal to run your Flask application, you can do so by running the `runflaskvoc.sh` script. Before running this script, make sure the `voc=True` is set true in the following line inside `mp_tictactoe/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)
```

Now, make sure you are inside the `mp_tictactoe` folder  by using the `pwd` command. 

```shell
> pwd
```

Use `ls` to ensure that you see the `runflaskvoc.sh` in the current folder.

```shell
> ls
```

Make sure that the script is executable by running the following command. 

```shell
> chmod a+x ./runflaskvoc.sh
```
The above script is to change the file to be executable for all users, group and owner.

To run the script, type the following.

```shell
> ./runflaskvoc.sh
```

Once it is running, you can open another tab in your browser and type the following url: [`https://myserver.vocareum.com/`](https://myserver.vocareum.com/).

To stop the web app type `CTRL+C`. 

#### Local Computer

If you are using your own computer, make sure to change the flag `voc=False` in the following line inside `mp_tictactoe/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)
```

Now, you can run Flask by typing:

```shell
flask run
```

Then open a web browser located at: `http://127.0.0.1:5000`. You should see an image as shown below.

![Login Page](https://www.dropbox.com/s/qa4ln4whlu320ng/mp3_login.png?raw=1)

You should then try to do the following:

- Register a user by clicking "Click to Register"
- Login using your newly created user account.
- Go to the different pages and makes sure you can browse through the different menu such as Home, Single Player, Records, and Users.
- Stop the web server by pressing `CTRL-C` in the terminal or command prompt.

## Exercise 3

In this exercise you will apply what you learn about Object Oriented to create a class called `Move`. 
### Task 1
Open and edit `mp_tictactoe/app/serverlibrary.py` to edit your `Move` class definition according to the definition below.

The class `Move` represent a move done by either a player or a computer. 

The class should have the following *properties*:

- row
- col

The setter for these properties should allow only integer value between 0 and 2 which represent the row or the column index. Upon initialization, the value of the row and the column's attribute should be initialized to -1. 

### Task 2
Write a test case after the following line:

```python
if __name__ == "__main__":
    ########################
    # Exercise 3
    ########################
    #
    # Test Move class
    # 
    # Write your test case to make sure that 
    # the row and col properties accept only index 
    # between 0 and 2
    #
    ########################
    pass
```

Hint:

- Use `assert` statement in your test.
- Run the file under `mp_tictactoe/app` folder by calling `python serverlibrary.py` from the Terminal or Command Prompt.

## Exercise 4

This is the main class to perform the AI-based TicTacToe game. We will write down the methods one at a time. The initialization method of the class is given as follows:

```python
class TicTacToe:
    def __init__(self, board=None, mark='X'):
        if board == None:
            board = [['_', '_', '_'],
                     ['_', '_', '_'],
                     ['_', '_', '_']]
        if isinstance(board, str):
            board = self.str_to_board(board)
        self.board = board
        self.max_player = 'X'
        self.min_player = 'O'
        self.mark = mark
```

The class has four attributes:

- `self.board` stores the state of the board in a list of list. One can initialize it using the argument when creating the object or if nothing is given will be initalized to an empty board where all tiles are set as `'_'`. 
- the method also checks if `board` is given as a single string. If it is, it calls `str_to_board()` method to change from a single string to a nested list. You need to implement this `str_to_board()` method.
- `self.max_player` is the maximize player. In Minimax algorithm there are two players where one of the players' objective is always to maximize its score and the other player's objective is always to minimize its score.
- `self.min_player` is the minimize player.
- `self.mark` is the current player mark, either X or O.

### Task 1

Do the following tasks:
1. Write a method called `reset()` where it resets the board (attribute `self.board`) to an empty board where all the tiles are set to `'_'`. 

1. Write a method called `str_to_board(boardstr)` which takes in a single argument. The argument is a string of 9 characters representing the state of a TicTacToe's board. The method should return a nested list where each cell is a single element in the nested list.

1. Create a computed property called `board_to_str` which returns a single string representation of the board. This is the reverse of `str_to_board()` method. 

1. Write a method called `update(row, col, mark)` where it set the tile at position `row` and `col` using the `mark`. 

### Task 2

Write a small helper method called `checkwinner(cell)` to check whether the winner is the maximizer or the minimizer by looking into one of the cell in the winning line. Given the input cell:

- the method should return 10 if the cell contains the maximizer's mark 
- or return -10 if the cell contains the minimizer's mark.

You should use the attribute `self.max_player` and/or `self.min_player` to check which mark is the maximizer or the minimizer.

### Task 3

Write a method called `evaluate(board)`. Given a state of the `board` in the input, the method should return:

- 10 if the maximizer wins the game
- -10 if the minimizer wins the game
- or 0 if there is no winner (a draw)

Hint:
- Check at each row for a winning pattern
- Check at each column for a winning pattern
- Check at both diagonals for a winning pattern
- This method may call `checkwinner(cell)` in Task 3 to return the proper scores.

### Task 4

Write a method called `checkwinning()`. This method should call `evaluate(board)` in Task 4. The method `evaluate(board)` returns the scores of the state of the board. Based on that score this method should return the following:

- if the score is 10, return the mark of the maximizer player
- if the score is -10, return the mark of the minimizer player
- if other than the above, return `None` object.

### Task 5

Write a method called `any_moves_left()` to check if there is any possible moves left. There is no input to the method. The method simply check the state of the board and see if there is any cell is still in the state `'_'`. If there is, it returns `True`, otherwise, it returns `False`.

### Task 6

Write a method called `find_best_move(player)`. This method returns the best move for the given input `player`. The input `player` is either X or O and the output is an instance of `Move` object which definition we have defined in Exercise 3. 

The algorithm to find the best move is given as follows:

1. Initialize best move score
1. Initialize best move to be NULL
1. For each move in the board:
    1. If the move is possible (the cell is empty):
        1. Change the board state temporarily with the move
        1. Compute evaluation function using minimax. You need to read Task 8 to see the arguments for `minimax(board, depth, is_max_player)`
        1. Undo the move in the board
        1. If the move evaluation score is the better than the best move score:
            1. Set the best move object to this move
1. return the best move object

Note:
- When calling the `minimax()` method, the role is alternating between the maximizer and the minimizer. So if the current player is a maximizer, you should call `minimax()` as a minimizer and vice versa. 

### Task 7

Write a method called `minimax(board, depth, is_max_player)`. The method takes in the following input arguments:

- `board` which is the state of the board.
- `depth` which is an integer and indicates the level of minimax algorithm.
- `is_max_player` which is a boolean either `True` or `False depending on whether the current move is a maximizer or a minimizer.

The method should return an integer, which is the score of the board at the current level of depth. The algorithm for the minimax evaluation function is as follows:

1. Get the score of the current board
1. If there is a winner, exit and return the score either 10 for maximizer or -10 for minimizer
1. Otherwise, check if there is any available move left
1. If no more move, it's a draw and return 0
1. Otherwise, recurse and call minimax again 

The last step depends on whether the current step is a maximizer or a minimzer. It proceeds as follows:
1. If the current step is a maximizer:
    1. Initalize the best score
    1. For each move in the board:
        1. If there is a possible move (empty cell):
            1. Make temporary move using a maximizer mark
            1. Compute the evaluation function using minimax ensuring:
                1. increase the depth level by 1
                1. change step to minimizer mark
            1. Undo the move
    1. return the best score
    

The step if it is the minimizer is the same. The only difference is in the following:
- The initial value for the best score will be opposite of that for the maximizer
- Use the minimizer mark in making the temporary move
- The best score will the lowest instead of the highest
- In calling the evaluation function, alternate to maximizer mark

### Task 8

Now you should test your `TicTacToe` class.

1. Scroll down to Exercise 4 test cases and comment out the following line `sys.exit(1)`. 
1. Run the file under `mp_tictactoe/app` folder by calling `python serverlibrary.py` from the Terminal or Command Prompt.

1. The rest of the code has been written for you. By now, you should be able to play the Tic Tac Toe with the computer. Try to understand the overall code and every part of the project.  Run the webserver to test.

## Expected Deliverable

The expected output can be found in this video below.

[Mini Project 3 Expected Output](https://web.microsoftstream.com/video/6c5a1ca1-66e3-46ab-aeb3-ae250422ed3d)

# Additional Notes
The following two exercises are meant for you to get familiar with how the whole application works. The solutions have been provided in `routes.py` in the GitHub repository. However, you may want to compare this note and the solution. 

## Exercise 5

Now our task is to updating the Single Player Page using the State table.

1. Open `mp_tictactoe/app/routes.py` in your text editor. This file contains the different handler for your web servers.
1. First, make sure that you have the following two lines in the import statement of `routes.py`.
    ```
    from app.models import User, State
    from app import db
    ```
1. Go to the function `single()`. 
1. Note that the TicTacToe's object instance is stored in `players[user]` variable. Retrieve the mark for the current player by replacing the `None` in the below code:
    ```python
    # get the mark for the current player
    # replace None
    player_mark = None
    ```
    and
    ```python
    # get the mark for the computer player
    # replace None with your code
    computer_mark = None
    ```
1. Create a new `State` object to store the state of the board. You need to replace the `None` in the argument of the object instantiation. We have filled one of the argument to get the time of the update using `datetime.now()` function. 
    - `user_id` should be initalied to the current's user id. 
    - `cell` should be initalized to a single string representing the board's state. You may want to use the computed property `board_to_str` here. 
    - `mark` should be initialized the current user's mark.
    ```python
    data = State(user_id=None,
                 time=datetime.now(),
                 cell=None,
                 mark=None)
    ```
1. Insert the data into the database. First you need to add the data into the session and then commit it. You need two lines of code here.
    ```python
    # add the data to the session
    pass
    # commit the session to the database
    pass
    ```
1. Complete the rest of the code in the `else` block as shown in the section below.
    ```python
        else:
            if user not in players:
                # set player mark randomly
                player_mark = random.choice(marks)

                # create the object instant TicTacToe using the 
                # player's mark
                players[user] = None
                
                # set the computer mark
                # replace None with your code
                computer_mark = None
            else:
                # if user is already in the dictionary, use the mark there
                # the TicTacToe object is stored inside players[user] variable
                player_mark = players[user].mark

                # set the computer mark
                # replace None with your code
                computer_mark = None
            return render_template('single.html', title='Single Player', 
    ```

## Exercise 6

We will use SocketIO to communicate between the client and the server without having to submit any HTML form. SocketIO allows us to emit an event and create a handler when an event is emitted.

### Task 1: Getting Familiar with SocketIO

1. Open `mp_tictactoe/app/routes.py` and go to `handle_connect(message)` function. You will see the following codes:
    ```javascript
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
    ```

Notes:
- The line before the function definition is a decorator by SocketIO to indicate that this is the handler when an event `startconnect` is detected in the `tictactoe` namespace.
- The event `startconnect` is emitted by the client when the page is loaded up. You can see the following code inside `mp_tictactoe/app/templates/single.html` when the HTML page is ready:
    ```javascript
    namespace = '/tictactoe';
    socket = io(namespace);
    socket.emit("startconnect", {"mark": "{{ player }}"});
    ```
- SocketIO allows you to emit an event with messages in the argument of the function. In this case, the `startconnect` has the following message: `{"mark": "{{ player }}"}`, which is a dictionary where the key is `mark` and the value is either X or O. 
- The following lines check if there is any existing data stored in the database in this collection for this particular user. If there is no data, it will create one and add it to the database.
    ```python
    all_data = State.query.filter_by(user_id=current_user.id).all()
    if len(all_data) < 1:
        data = State(user_id=current_user.id,
                     time=datetime.now(),
                     cell='_________',
                     mark=mark)
        db.session.add(data)
        db.session.commit()
    ```
- Recall that `query()` is a method to query the SQL database. In our case we filter the query by the `user_id`. We want to retrieve all the records by the current user using `.all()`. 
- The code simply searches if there is any record of the current user playing the game. If there is, the number of records will not be less than 1 as every click will store a new data into the database. On the other hand, if this is the first time the user play, the code creates a new data by inserting an empty TicTacToe's board. 
- The code then tries to find the last record (see the index `-1`). 
    ```python
    last_data = State.query.filter_by(user_id=current_user.id).all()[-1]
    ```
- Then, the code creates a new instance of `TicTacToe` object using this last data.
    ```python
    players[current_user.username] = TicTacToe(last_data.cell,
                                               last_data.mark)
    ```
- Lastly, the code emit a new signal or event called `afterconnect` using SocketIO and pass on the board's state as the message. 
    ```python
    emit('afterconnect', {'data': last_data.cell})
    ```

### Task 2: Handling Click
In Exercise 1 Task 1, you have encountered the `click_cell()` function inside `mp_tictactoe/app/static/clientlibrary.py` which handle what happens when there is a click. One of the thing that this function does is to emit a SocketIO event:

```python
socket.emit('clicked', {'username': username, 'id': cellid, 'mark': mark})
```

Now, we are going to handle this event `clicked` that is emitted when there is a click.

Open `mp_tictactoe/app/routes.py` and go to `handle_click(message)`. This is the function that handles the `clicked` event as shown by the decorator.
```python
@socketio.on('clicked', namespace='/tictactoe')
def handle_click(message):
    ...
```

1. First, we will initialize a few variables using the argument `message`. To understand the structure of message, you can open `mp_tictactoe/app/static/clientlibrary.py` and look inside the `emit()` function call.  Replace the `None` in the codes below.
    ```python
    # get the user name, mark and the clicked cell from message
    # check clientlibrary.py for the message sent in 
    # event 'clicked'
    # replace the None
    user = message[None]
    mark = message[None]
    
    # set the computer mark to be the opposite of that of player
    computer = None
    
    # get the cell number from 'id' inside message
    # Note that the format for the cell string is 'cellXY'
    # extract only the last two characters
    cell = None
    ```
    
1. In the previous step, we have obtained the row and col that the user clicked inside `cell` variable. Extract the row and the column and call the `update(row, col, mark)` method of TicTacToe's object instance. **Make sure you pass on int objects instead of str objects** in the row and column.
    ```python
    # update TicTacToe's object using the mark at the approriate row and col
    # replace the None
    players[user].update(None, None, None)
    ```
    
1. After updating the board using the `update()` method, now you can check if there is a winner by looking at the board. Call a method to check if there is a winner from one of TicTacToe's methods. **Note: There are two instances where you need to call this method. One is just after you are updating the player's move and the other one is after you update the computer's move.**
    ```python
    # check if there is any winner
    # you can call checkwinning method inside TicTacToe's object
    winner = None
    ```
1. Now, we will handle what happens when there is no winner after the move. First, we will check if the computer can make a move. Replace `None` in the following code with a method call in `TicTacToe` class that tells you if you can still make a move.
    ```python
    # if there is no winner, check if there is any move lefts
    # get the boolean value by calling a method inside TicTacToe
    can_move = None
    ```
1. If the computer can make a move, it will find the best move and update the board. Replace the `None` in the below code to update the `TicTacToe` board.
    ```python
    # update the board with the best move
    # replace the None
    players[user].update(None, None, None)
    ```
1. After we update the board, we again check if there is a winner from the last state of the board. Replace the `None` in the code below.
    ```python
    # check if there is a winner
    # call a method inside TicTacToe
    winner = None
    ```

1. Lastly, we need to update the database. To do that, first you need to create an object instance of `State`. Next you need to add the data and commit it to the database.
    ```python
    # insert a new document to db on the board's status
    # create an object instance of State. Replace the None.
    data = State(user_id=None,
                 time=datetime.now(),
                 cell=None,
                 mark= None)
    # write the code to add the data to the session
    pass
    # write the code to commit the session to the database
    pass
    ```

