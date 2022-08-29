# Using Bootstrap In This Mini Project 2

## Pre-Requisite

This notes explains briefly how we use Flask-Bootstrap for our HTML templates in Mini Project 2.  You will need to read the following tutorial:
- [The Flask Mega-Tutorial Part II: Templates](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [The Flask Mega-Tutorial Part XI: Facelift](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift)

We will only explains those relevant to this mini project and more explanations can be found in those tutorials.

## Base HTML

In this mini project, we have one base HTML file inside `app/templates/base.html`.  This HTML file has the following structure following the [documentation](https://bootstrap-flask.readthedocs.io/en/stable/migrate/).

```html
<!doctype html>
<html lang="en">
    <head>
        {% block head %}
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        {% block styles %}
            <!-- Bootstrap CSS -->
            {{ bootstrap.load_css() }}
        {% endblock %}

        <title>Your page title</title>
        {% endblock %}
    </head>
    <body>
        <!-- Your page content -->
        {% block content %}{% endblock %}

        {% block scripts %}
            <!-- Optional JavaScript -->
            {{ bootstrap.load_js() }}
        {% endblock %}
    </body>
</html>
```

In order to use this file, you have to create `Bootstrap5` object in your `app/__init__.py` file. This uses Bootstrap 5 instead of Bootstrap 4. 

```python
from flask_bootstrap import Bootstrap5 
...
bootstrap = Bootstrap5(application)
```

The base HTML also contains the code for the navigation bar on the top:

```html
<nav class="navbar navbar-default">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="{{ url_for('index') }}">Mini Project 2</a>
      </div>
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li><a href="{{ url_for('index') }}">Home</a></li>
          <li><a href="{{ url_for('questions') }}">Questions</a></li>
          <li><a href="{{ url_for('challenges') }}">Challenges</a></li>
          <li><a href="{{ url_for('halloffame') }}">Hall of Fame</a></li>
          <li><a href="{{ url_for('users') }}">Users</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          {% if current_user.is_anonymous %}
          <li><a href="{{ url_for('login') }}">Login</a></li>
          {% else %}
          <li><a href="{{ url_for('logout') }}">Logout</a></li>
          {% endif %}
        </ul>
      </div>
    </div>
  </nav>
```

After the navigation bar, the code describes the content block.

```html
{% block content %}
  <div class="container">
    {% with messages = get_flashed_messages() %}
    {% if messages %}
      {% for message in messages %}
      <div class="alert alert-info" role="alert">{{ message }}</div>
      {% endfor %}
    {% endif %}
    {% endwith %}
  </div>
{% endblock %}
```

The code above is used to display any flashed message. An example for a flash message is when the web application gives an alert or display an error message. In our mini project, we use this several times, for example after we create a new question inside `app/routes.py`, under `questions()` function definition, we can find the following code.

Notice that we use the code `<div class="alert alert-info" role="alert">` to style our alert. You can find more info in [Bootstrap's Alert Documentation](https://getbootstrap.com/docs/5.0/components/alerts/).

```python
def questions():
    ...
    flash('Congratulations, you have created a new question.')
    ...
```

Part of the `content` block is the `app_content` block.

```html
    {% block app_content %}{% endblock %}
```

The above code inside `base.html` leaves the `app_content` block empty. This will be filled in the other HTML files. for example, in the `index.html` file, you will find:

```html
{% extends "base.html" %}

{% block app_content %}

<h1 class="display-1">Hi, {{ current_user.username }}!</h1>
...
{% endblock %}
```

Lastly, the `base.html` contains the code to include any scripts we use.

```html
{% block scripts %}
{{ super() }}
<script type="module">import * as library from '/static/__target__/clientlibrary.js'; window.library = library;</script>
{% endblock %}
```
- The line `{{ super() }}` is to ensure that all the other scripts in the parent HTML files are included.
- The next line is to include our `clientlibrary.js` which is stored inside our `app/static/__target__/` folder. Recall that the `__target__` folder is produced by Transcrypt when we compile our `clientlibrary.py`.

## Display Heading and Paragraph Styles

When you open `index.html` inside the `template` folder, you will see that we use both `display-1` for header and `lead` for paragraph. 

```html
<h1 class="display-1">Hi, {{ current_user.username }}!</h1>

<p class="lead">Welcome ...</p>
```

For more options on typography, check [Bootstrap's Typography Documentation](https://getbootstrap.com/docs/5.0/content/typography/). 

## Table Styles

We use [Bootstrap's Table Style](https://getbootstrap.com/docs/5.0/content/tables/) in several files like `question.html`, `challenge.html`, `users.html`, and `halloffame.html`. 

The code below is from `users.html`.

```html
<table class="table table-striped" >
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">User</th>
    </tr>
  </thead>
  <tbody>
  {% for idx in range(users|length) %}
  	<tr>
      <th scope="row" class="lead">{{ idx+1 }}</th>
      <td class="lead">
      	#Replace Me#
      </td>
    </tr>
  {% endfor %}
  
  </tbody>
</table>
```

We use `table` inside the `class` option for `<table>` to enable Bootstrap's Table style. We also added `table-striped` so that each row is having an alternately light and dark color background. 



## References

- [Bootstrap's Navbar Documentation](https://getbootstrap.com/docs/5.0/components/navbar/)
- [Bootstrap's Alert Documentation](https://getbootstrap.com/docs/5.0/components/alerts/).
- [Bootstrap's Table Documentation](https://getbootstrap.com/docs/5.0/content/tables/)
- [Bootstrap's Typography Documentation](https://getbootstrap.com/docs/5.0/content/typography/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

