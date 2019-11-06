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


