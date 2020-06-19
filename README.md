# Flask microservice challenge

You have to build a microservice that exposes a REST api with two different
tables, users and states. Both tables should be open to creation, deletion,
or update. Every request must only accept this `Content-type: application/json`.

### Features
- [] Create `users` and `states` tables.
- [] Import data from csv file called `stats.csv` and load it in `states` table.
- [] CRUD REST API to interface with `users` table.
- [] CRUD REST API to interface with `states` table.

## Tables


### Users

Column | Type
------ | ----
id | int sequence ( PK )
name | string
age | int
state | int (FK states)
updated_at | datetime
created_at | datetime

### States
Column | Type
------ | ----
id | int sequence ( PK )
code | int
name | string
updated_at | datetime
created_at | datetime

### Author

Yari Ivan Taft

- GitHub: https://github.com/yaritaft
- Website: http://yaritaft.com
- LinkedIn: https://www.linkedin.com/in/yari-ivan-taft-4122a7153/

### Badges
[![Build Status](https://travis-ci.org/yaritaft/microservices_flask_challenge_bkr.svg?branch=master)](https://travis-ci.org/yaritaft/microservices_flask_challenge_bkr)
[![Coverage Status](https://coveralls.io/repos/github/yaritaft/microservices_flask_challenge_bkr/badge.svg?branch=master)](https://coveralls.io/github/yaritaft/microservices_flask_challenge_bkr?branch=master)

## Table of contents

- [Technology](#Technology)
- [Routes](#Routes)
- [PreRequisites](#Pre-requisites)
- [Run APP](#Run-APP)
- [Preload data](#Preload-data)
- [Run tests](#Run-tests)
- [Standards applied](#Standards-applied)

## Technology

- Programming languaje: Python 3
- APP Framework: Flask
- API Framework: Flask Rest Plus
- Containers: Docker, Docker-compose
- Web-server: Uwsgi

## Routes

- API swagger: http://127.0.0.1:5000/
- API users: http://127.0.0.1:5000/users/
- API states: http://127.0.0.1:5000/states/

## Pre-requisites

- Docker and docker compose installed.
- Docker and docker compose working without sudo.
- Python3 installed
- Pip3 installed
- Linux/Mac terminal (Or emulated linux on Windows)
- No services running on localhost port 5432/5434 or 5000.

### Run APP

You have two way of running the App:
- Using docker-compose.
- Using your local python interpreter.

#### Docker

0) Execute script to run migrations and create db.
```
chmod 777 up_and_upgrade_dbs.sh
./up_and_upgrade_dbs.sh
```

Warning: If you want to execute this and the database has previous alembic 
versions it will raise an error. The only thing you have to do in that case is
to access the database and drop table called alembic version.

1) Open terminal in repository's root folder. And type:
```
docker-compose build
docker-compose up api
```

2) Go to the swagger and test the app or consume api through curl or postman.

3) Press Control + C and then type:
```
docker-compose down
```

#### Local python interpreter
0) Up and migrate db and testing. Open terminal in root folder and type:
```
chmod 777 up_and_upgrade_dbs.sh
./up_and_upgrade_dbs.sh
```

1) First go with a terminal to root folder type this:
```
python3 -m virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Last step:
```
uwsgi --thunder-lock --ini uwsgi.ini
```
Optional:

If you want more flexibility instead of using uwsgi you can use manage.py
by pressing:
```
python manage.py run
```

2) To shutdown the app press control + C on terminal.

### Preload data

Preload data in db from states.csv file.

Being at the same point before last step type:

```
python manage.py load_initial_data
```

### Run tests

Being at the same point before last step type:

```
python manage.py test
```

### Precommit hooks

If you want to join the project you should add pre-commit hook to repository.
You can do that by typing inside the virtual environment:

```
precommit install
```

This will trigger black formatter and flake8 linter. If code is not allign with
flake8 standard then the commit will fail.

### Standards applied

- PEP8
- PEP257
- Appnexus (google import order style)
- Flake8
- Flake8 Docstrings
- Flake8 Import Order
- Black formatting
