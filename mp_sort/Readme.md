# Mini Project 1: Sorting App

## Learning Objectives
In this mini project, you will develop a web app to sort numbers. By the end of this assignment, you should be able to:
- Create a simple web app using Flask web framework
- Use Transcrypt Python library to create front-end web script with Python
- Run a localhost web server 
- Deploy web app to Amazon Elastic Beanstalk

## Setup

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:
- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

### Downloading Repository
Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```
$ cd Downloads
$ git clone https://github.com/kurniawano/d2w_mini_projects.git
```

### Go to Mini Project 1 Folder

Once you have downloaded the repository, you can go to the repository and to the folder called `mp_sort` for this mini project.

```
$ cd d2w_mini_projects/mp_sort
$ ls
```

The last command should output the following:

```
Readme.md		
application.py
requirements.txt
app
```

This handout can be found in the file `Readme.md`.

### Create Virtual Environment

**If you are using Windows, you should open Anaconda Prompt to do the following steps.**
In the following steps, the MacOS prompt will be represented by:
```
$
```
while Windows prompt will be represnted by:
```
>
```

Go to the root folder `mp_sort`. For MacOS:
```
$ cd ~/Downloads/d2w_mini_projects/mp_sort
```

For Windows:
```
> cd %USERPROFILE%\Downloads\d2w_mini_projects\mp_sort
```
From the root folder, i.e. `mp_sort`, create virtual environment called `virtenv`.

```
$ python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment. For MacOS:

```
$ source virtenv/bin/activate
```

For Windows:
```
> virtenv\Scripts\activate
```

You should see the word `virtenv` in your prompt something like:
```
(virtenv) user$
```
or
```
(virtenv) folder>
```

_To exit the virtual enviroment at the end of this mini project, simply type:_
```
$ deactivate
```
or
```
> deactivate
```

### Install Python Packages

Install the necessary packages for this mini project. From the root folder, i.e. `mp_sort`, type the following:

For MacOS:
```
$ pip install -r requirements.txt
```

For Windows:
```
> pip install -r requirements.txt
```

The above steps will install Flask and Transcrypt Python libraries and some other necessary packages.

## Exercise 1

### Brief Overview of Flask Project Structure

We are using Flask web framework to create this web app. The first file you may notice is `application.py` in the root folder. Open that file using a text editor. You should see the following:

```
from app import application

if __name__ == "__main__":
	application.run(host="0.0.0.0", port=8080, debug=True)
```

The last two lines runs the `application` object when it is run on the shell. The value will be used when you deploy it to Amazon Elastic Beanstalk. It also enables the debug mode to `True` so that you can see any error messages when they occur. The `application` object is imported in the first line from the `app` package. The `app` package is in a folder called `app`:

```
mp_sort/
  app/
    __init__.py
    routes.py
    static/
    templates/
```

The file `__init__.py` contains the line that creates the `application` object as a `Flask` instance.

```
from flask import Flask

application = Flask(__name__)

from app import routes
```

This file also import the file `routes.py` which defines the URL routing.

```
from flask import render_template
from app import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Mini Project 1 Home')

@application.route('/ex1')
def exercise1():
    return render_template('ex1.html', title='Mini Project 1 Exercise 1')

@application.route('/ex2')
def exercise2():
    return render_template('ex2.html', title='Mini Project 1 Exercise 2')
```

The first route indicates then a user enter the URL with "/" or "/index" at the end, our web app will serve this request by calling `index()` function. The `index()` function will return a HTML response following a template called `index.html`. This file `index.html` can be found inside the `templates` folder.

```
mp_sort/
  app/
    __init__.py
    routes.py
    static/
    templates/
      index.html
      ex1.html
      ex2.html
```

The other two routes does the same by serving any request to "/ex1" and "/ex2". The templates for these two are provided inside the `template` folder. 

For Exercise 1, you may want to look into the file `ex1.html`. Open this file in a text editor.

### HTML for Exercise 1

HTML code normally contains of two section, the header and the body. Each of the elements can be identified by their tags. The header element for `ex1.html` is as below:

```
    <head>
        <title>{{title}}</title>
        <script type="module">import * as library from '/static/__target__/library.js'; window.library = library;</script>
    </head>
```

The `<title>` set the title of the page. Inside this tag we found `{{title}}`. The two curly braces is a Jinja template syntax that allow you to change the HTML code. It is a kind of variable that you can set. This variable `title` is actually set when `render_template()` is called in `routes.py`.

```
@application.route('/ex1')
def exercise1():
    return render_template('ex1.html', title='Mini Project 1 Exercise 1')
```

In this code, the variable `title` is set to `Mini Project 1 Exercise 1`.

The second tag `<script ...>...</script>` is to import our script. We will generate this Javascript file `library.js` from our Python `library.py` file inside the `static` folder. 

```
mp_sort/
  app/
    __init__.py
    routes.py
    static/
      library.py
```

All your work for this mini project will be done inside `library.py`.

### Using Transcrypt

Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use `Transcrypt` library which can compile and translate Python script into a Javascript file. To compile `library.py`, first we need to go into the `static` folder.

For MacOS:
```
$ cd ~/Downloads/d2w_mini_projects/mp_sort/app/static
$ ls
```

For Windows:
```
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_sort\app\static
> dir
```

The last command will list the file in that folder, and you should see:
```
library.py
```

Run Transcrypt on `library.py`:

```
transcrypt -b library.py
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. To see the content of that folder:

For MacOS:
```
$ ls
$ ls __target__
```

For Windows:
```
> dir
> dir __target__
```

```
__target__/
  library.js
  library.project
  math.js
  org.transcrypt.__runtime__.js
  random.js
```

You should see `library.js` created inside this folder.

### Run Flask

Now you are ready to run your web app in your local computer. To do so, you need to go back to the root directory. This can be done with the following:

For MacOS:
```
$ cd ../..
```
which means go up the folder two times. Or, simply
```
$ cd ~/Downloads/d2w_mini_projects/mp_sort/
```

For Windows:
```
> cd ..\..
```
or
```
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_sort
```

You should see `application.py` in this root folder. Run Flask by typing:

```
$ flask run
```
or
```
> flask run
```

You should see that some output will be thrown out, which one of them would be:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. You should see something like the following:

![](https://www.dropbox.com/s/a2fqx5svvyqtqf9/mp1_home.png?raw=1)

To stop the web app type `CTRL+C`. 

### Assignment for Exercise 1

#### Part 1: Generating Random Integers 
Open `ex1.html` in your text editor. You should see these few lines of code:

```
		<p>
        	<div id="generate">...</div>
        	<button onclick="library.generate()">Generate 10 numbers</button>
        </p>
        <p>
        	<div id="sorted">...</div>
        	<button onclick="library.sortnumber1()">Sort</button>
        </p>
```

We have two buttons. The first button is to generate 10 random numbers. The event `onclick` is binded to the function `generate()` in your `library.py`. Fill in this function to generate 10 random integers and store it into