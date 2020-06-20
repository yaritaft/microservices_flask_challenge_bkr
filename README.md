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
[![Coverage Status](https://coveralls.io/repos/github/yaritaft/microservices_flask_challenge_bkr/badge.svg?branch=master)](https://coveralls.io/github/yaritaft/microservices_flask_challenge_bkr?branch=master)

## Table of contents

- [Technology](#Technology)
- [Routes](#Routes)
- [PreRequisites](#Pre-requisites)
- [Run APP](#Run-APP)
- [Preload data](#Preload-data)
- [Run tests](#Run-tests)
- [Standards applied](#Standards-applied)
- [Deployment](#Deployment)

## Technology

- Programming languaje: Python 3
- APP Framework: Flask
- API Framework: Flask Rest Plus
- Containers: Docker, Docker-compose
- Web-server: Uwsgi
- Deployment: Coveralls and Travis

## Routes

- API swagger: http://127.0.0.1:5000/
- API users: http://127.0.0.1:5000/users/
- API states: http://127.0.0.1:5000/states/

## Pre-requisites

- Docker and docker compose installed.
- Linux/Mac terminal (Or emulated linux on Windows)
- No services running on localhost port 5432 or 5000.

### Run APP

1) Execute script to run migrations and create db.
```
chmod 777 ./up_dev.sh
./up_dev.sh
```

2) Go to the swagger and test the app or consume api through curl or postman.

3) Press Control + C to stop the app.

### Preload data

If states table in db is empty, it is automatically populated with seed
data from states.csv.

### Run tests

Being at the same point before last step type:

```
chmod 777 ./up_test.sh
./up_test.sh
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

### Deployment

There is a build in a remote environment in Travis. That platform checks that
the build is valid and that none of the tests are failing. If everything is
okay, then the code coverage is sent to coveralls and in that site the test
coverage can be reviewed in detail.