# Mini Project 1: Sorting App

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Mini Project 1: Sorting App](#mini-project-1-sorting-app)
    - [Learning Objectives](#learning-objectives)
    - [Setup](#setup)
        - [Install Git](#install-git)
        - [Downloading Repository](#downloading-repository)
        - [Go to Mini Project 1 Folder](#go-to-mini-project-1-folder)
    - [Create Virtual Environment (Windows)](#create-virtual-environment-windows)
    - [Create Virtual Environment (MacOS/Linux)](#create-virtual-environment-macoslinux)
    - [Combined (Windows/Mac/Linux)](#combined-windowsmaclinux)
        - [Install Python Packages](#install-python-packages)
        - [Exercise 1](#exercise-1)
            - [Brief Overview of Flask Project Structure](#brief-overview-of-flask-project-structure)
        - [HTML for Exercise 1](#html-for-exercise-1)
    - [Windows](#windows)
        - [Using Transcrypt](#using-transcrypt)
        - [Run Flask](#run-flask)
            - [Vocareum](#vocareum)
            - [Local Computer](#local-computer)
    - [MacOS/Linux](#macoslinux)
        - [Using Transcrypt](#using-transcrypt-1)
        - [Run Flask](#run-flask-1)
    - [Combined (Windows/Mac/Linux)](#combined-windowsmaclinux-1)
        - [Assignment for Exercise 1](#assignment-for-exercise-1)
            - [Part 1: Generating Random Integers](#part-1-generating-random-integers)
            - [Part 2: Sorting Numbers](#part-2-sorting-numbers)
        - [Assignment for Exercise 2](#assignment-for-exercise-2)
            - [Part 1: Creating a Text Input](#part-1-creating-a-text-input)
            - [Part 2: Sorting User Input](#part-2-sorting-user-input)
        - [Expected Output](#expected-output)
    - [Optional: Deploying to Amazon Elastic Beanstalk](#optional-deploying-to-amazon-elastic-beanstalk)

<!-- markdown-toc end -->


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

```shell
$ cd Downloads
$ git clone https://github.com/kurniawano/d2w_mini_projects.git
```

### Go to Mini Project 1 Folder

Once you have downloaded the repository, you can go to the repository and to the folder called `mp_sort` for this mini project.

```shell
$ cd d2w_mini_projects/mp_sort
$ ls
```

The last command should output the following:

```shell
Readme.md		
application.py
requirements.txt
app
```

This handout can be found in the file `Readme.md`.

## Create Virtual Environment (Windows)

**You should open Anaconda Prompt to do the following steps.**

In the following steps, the Windows prompt will be represented by:
```shell
>
```
Go to the root folder `mp_sort`.
```shell
> cd %USERPROFILE%\Downloads\d2w_mini_projects\mp_sort
```
From the root folder, i.e. `mp_sort`, create virtual environment called `virtenv`.

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

Go to the root folder `mp_sort`. 
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_sort
```

From the root folder, i.e. `mp_sort`, create virtual environment called `virtenv`.

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

Install the necessary packages for this mini project. From the root folder, i.e. `mp_sort`, type the following:

For Windows:
```shell
> python -m pip install -U --force-reinstall -r requirements.txt
```

For MacOS/Linux: (For Linux, you might need to type pip3 instead)
```shell
$ python -m pip install -U --force-reinstall -r requirements.txt
```

The above steps will install Flask and Transcrypt Python libraries and some other necessary packages.

### Exercise 1

#### Brief Overview of Flask Project Structure

We are using Flask web framework to create this web app. The first file you may notice is `application.py` in the root folder. Open that file using a text editor. You should see the following:

```python
from app import application

if __name__ == "__main__":
	application.run(host="0.0.0.0", port=8080, debug=True)
```

The last two lines runs the `application` object when it is run on the shell. The value will be used when you deploy it to Amazon Elastic Beanstalk. It also enables the debug mode to `True` so that you can see any error messages when they occur. The `application` object is imported in the first line from the `app` package. The `app` package is in a folder called `app`:

```shell
mp_sort/
  app/
    __init__.py
    routes.py
    static/
    templates/
```

The file `__init__.py` contains the line that creates the `application` object as a `Flask` instance.

```python
from flask import Flask

application = Flask(__name__)

from app import routes
```

This file also import the file `routes.py` which defines the URL routing.

```python
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

The first route indicates when a user enter the URL with "/" or "/index" at the end, our web app will serve this request by calling `index()` function. The `index()` function will return a HTML response following a template called `index.html`. This file `index.html` can be found inside the `templates` folder.

```shell
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

```html
<head>
	<title>{{title}}</title>
	<script type="module">import * as library from '/static/__target__/library.js'; window.library = library;</script>
</head>
```

The `<title>` set the title of the page. Inside this tag we found `{{title}}`. The two curly braces is a Jinja template syntax that allow you to change the HTML code. It is a kind of variable that you can set. This variable `title` is actually set when `render_template()` is called in `routes.py`.

```python
@application.route('/ex1')
def exercise1():
    return render_template('ex1.html', title='Mini Project 1 Exercise 1')
```

In this code, the variable `title` is set to `Mini Project 1 Exercise 1`.

The second tag `<script ...>...</script>` is to import our script. We will generate this Javascript file `library.js` from our Python `library.py` file inside the `static` folder. 

```shell
mp_sort/
  app/
    __init__.py
    routes.py
    static/
      library.py
```

All your work for this mini project will be done inside `library.py`.


## Windows

### Using Transcrypt

Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use `Transcrypt` library which can compile and translate Python script into a Javascript file. To compile `library.py`, first we need to go into the `static` folder.

```shell
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_sort\app\static
> dir
```

The last command will list the file in that folder, and you should see:
```shell
library.py
```

Run Transcrypt on `library.py`:

```shell
python -m transcrypt -b -n library
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. To see the content of that folder:

```shell
> dir
> dir __target__
```

```shell
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

```shell
> cd ..\..
```

which means go up the folder two times. Or, simply

```shell
> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_sort
```

You should see `application.py` in this root folder. 

#### Vocareum
If you use Vocareum terminal to run your Flask application, you can do so by running the `runflaskvoc.sh` script. Before running this script, make sure the `voc=True` is set true in the following line inside `mp_sort/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)
```

Now, make sure you are inside the `mp_sort` folder  by using the `pwd` command. 

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

If you are using your own computer, make sure to change the flag `voc=False` in the following line inside `mp_sort/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)
```

Now, you can run Flask by typing:

```shell
> flask run
```

You should see that some output will be thrown out, which one of them would be:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. You should see something like the following:

![](https://www.dropbox.com/s/a2fqx5svvyqtqf9/mp1_home.png?raw=1)

To stop the web app type `CTRL+C`. 


## MacOS/Linux

### Using Transcrypt

Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use `Transcrypt` library which can compile and translate Python script into a Javascript file. To compile `library.py`, first we need to go into the `static` folder.

```shell
$ cd ~/Downloads/d2w_mini_projects/mp_sort/app/static
$ ls
```

The last command will list the file in that folder, and you should see:
```shell
library.py
```

Run Transcrypt on `library.py`:

```shell
python -m transcrypt -b -n library
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. To see the content of that folder:

```shell
$ ls
$ ls __target__
```

```shell
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

```shell
$ cd ../..
```
which means go up the folder two times. Or, simply
```shell
$ cd ~/Downloads/d2w_mini_projects/mp_sort/
```

You should see `application.py` in this root folder. Run Flask by typing:

```shell
$ flask run
```

You should see that some output will be thrown out, which one of them would be:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. You should see something like the following:

![](https://www.dropbox.com/s/a2fqx5svvyqtqf9/mp1_home.png?raw=1)

To stop the web app type `CTRL+C`. 

## Combined (Windows/Mac/Linux)

### Assignment for Exercise 1

#### Part 1: Generating Random Integers 
Open `ex1.html` in your text editor. You should see these few lines of code:

```html
<p>
	<div id="generate">...</div>
	<button onclick="library.generate()">Generate 10 numbers</button>
</p>
```

We have two buttons. The first button is to generate 10 random numbers. The event `onclick` is binded to the function `generate()` in your `library.py`. Fill in this function to do the following:
- generate 10 random integers and store it into the global variable `array`,
- create a single string containing all the numbers. For example,
    `3, 1, 2, 4, 8, 6, 5, 9, 0, 7.`

#### Part 2: Sorting Numbers

In `ex1.html`, you should also find the following lines:
```html
<p>
	<div id="sorted">...</div>
	<button onclick="library.sortnumber1()">Sort</button>
</p>
```

The second button is to sort the generated random numbers. The event `onclick` is binded to the function `sortnumber1()` in your `library.py`. Fill in this function to do the following:
- get the random numbers from `generate` HTML id. *Hint: use `document.getElementById(id).innerHTML`* to get the numbers,
- remove the other characters and create a list of integers called `sortedarray`,
- sort the list using either bubble sort or insertion sort,
- create a single string containing the sorted numbers.

### Assignment for Exercise 2

#### Part 1: Creating a Text Input

In this exercise, instead of randomly generate the numbers, you will ask the user to enter the sequence of numbers using a Text Input.

Open `ex2.html`. You should see the following:

```html
<p>
	<div id="generate">Enter a sequence of numbers separated by a comma (","):</div>
	## Enter the code here to create a Text Input. ##
</p>
```

Search the internet to find out how to create a Text Input field and enter the code in the line indicated. Replace that line with the correct tag and code for Text Input. Name the text input `numbers`.

#### Part 2: Sorting User Input

You should also see the following line:

```html
<p>
	<div id="sorted">...</div>
	<button onclick="library.sortnumber2()">Sort</button>
</p>
```

This button's even `onclick` is binded to `sortnumber2()` function in your `library.py`. Modify that function to do the following:
- get the string from the text input stored in the variable `value`,
- split the string using comma as a separator,
- remove all trailing whitespaces and convert them to numbers,
- sort the list of numbers,
- create a single string containing the sorted numbers and store it to `array_str`.

### Expected Output

The expected output for both exercises 1 and 2 can be found in this video.

[Mini Project 1 Expected Output](https://web.microsoftstream.com/video/fa203d50-c064-48a2-a951-ec0ec3385a48)

## Optional: Deploying to Amazon Elastic Beanstalk

Check [Deploying to Amazon Elastic Beanstalk](DeployEB.md).
