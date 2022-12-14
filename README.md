# Todo_api
This is a simple todo api built with Django and the Django Rest Framework

# Technology
 <img src='https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue'><br>
 <img src='https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green'><br>
 <img src='https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white'>

# Documentation
The documentation for this api can be found here ->

# Database ERD
https://drawsql.app/teams/gabriels-team-1/diagrams/todo-api

# Setup
To set up this project on your local machine,<br>

1. Fork the repo and clone it to your local machine<br>

2. In your terminal, navigate to the project root folder <code>todo_api</code> create a virtual environment <code>python3 -m venv env</code> , then activate it <code>source env/bin/activate</code> (<i>for linux/unix</i>) or <code>env/scripts/activate</code> (<i>for windows</i>)<br>

3. Install the project dependencies <code>pip install -r requirements.txt </code> <br>

4. Make your migrations <code>python manage.py migrate</code> or run makemigrations again if necessary <code>python manage.py makemigrations</code> <br>

5. Start the django development server <code>python manage.py runserver</code> or use the gunicorn server <code>gunicorn todo_project.wsgi</code> <br>

6. Make your api calls
