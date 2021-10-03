# StackBuilders

PROJECT DESCRIPTION
--------------------
An API to Initiate Asynchronously A Celery Task And Poll Its Status and Result.

- Uses the default SQLite Database
- Uses REDIS as message broker and result backend for Celery
- Uses Django Database Cache for some Caching

PROJECT REQUIREMENTS (Required Libraries)
-----------------------------------------
All required libraries to run application detailed in requirements.txt in root.

TEST PACKAGE
-------------------
Pytest
```
To run test cases, simple enter 'pytest' in terminal.
```

CI/CD Tool
-------------------
CircleCI 

```
Test result for each commit can be viewed here: https://github.com/tosinolawore/stackbuilders/commits/master
```

To set up CircleCI pipeline for running tests, the yaml file has been added in the following directory (
.circleci/config.yml).

Fork the entire project to your repository and afterwards, create a CircleCI account. The repository will
automatically appear on the list of Projects on circleci, you can then build and run tests.

Endpoints 
-------------------
Add Trailing Slash

```
Start Celery Task with some string - /tasks/ (METHOD: POST, DATA: name, FORMAT: JSON)

Retrieve Task Result and Status - /tasks/<id>/ (METHOD: GET, <id> - unique id or primary key for the tasked. This is returned in the JSON response from above. NOTE: the <id> is not the task_id but the primary key of the Task saved in Database.)

List All Tasks - /tasks/ (METHOD: GET)

Edit or Update Task name - /tasks/<id>/ (METHOD: PUT, <id> - unique id or primary key for the task for which the name is to be edited, DATA: name)

Delete a Task record - /tasks/<id>/ (METHOD: DELETE, <id> - unique id or primary key for the task for which record is to be deleted.)

```

RUN INSTRUCTIONS
-------------------
- Simply install dependencies in requirements.txt
- Run 'python manage.py makemigrations'
- Run 'python manage.py migrate'
- Run 'python manage.py createcachetable' to create DATABASE CACHE TABLE
- Start REDIS Server
- Start Celery using the command 'celery -A stackbuilders worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo'
- Run django server 'python manage.py runserver'


