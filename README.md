# Task

Write a CRUD REST API using Python for a single resource type. You may use a framework (we use Tornado, but that is not required for this assessment).

The application must satisfy these requirements:

1. Written in Python 3.8 or later.
2. Endpoints to create, read, list, update, and delete objects called "Widgets"
3. Widget objects include the following properties (at least):

    1. Name (utf8 string, limited to 64 chars)
    2. Number of parts (integer)
    3. Created date (date, automatically set)
    4. Updated date (date, automatically set)

4. Widgets are persisted to and retrieved from a SQLite file database.
5. Include a README that describes how to setup and run the application.

Ideas to make the project even better:

- Include unit or functional test coverage
- Include an OpenAPI spec
- PEP8 compliance
- Pass standard lint tests (ie: flake8 or similar)
- Pass bandit security analysis
- Use Python type annotations

# How to run

1. Prepare a python environment of choice to run the app (e.g. system interpreter, virtual environment, docker, etc)
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`
