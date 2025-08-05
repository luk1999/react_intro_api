# React Intro REST API
REST API for React intro traning

## Setup project

### Clone repository
* Clone repository:
  ```bash
  mkdir react_intro_api
  git clone https://github.com/luk1999/react_intro_api.git react_intro_api

### Create virtual env
* Using `venv` (Linux):
  ```bash
  cd react_intro_api
  python3 -m venv .venv
  source .venv/bin/activate
  pip3 install -r requirements.txt
  ```
* Using `venv` (Windows):
  ```powershell
  cd react_intro_api
  C:\python3\python -m venv .venv
  .venv\scripts\activate
  pip install -r requirements.txt
  ```
* Using [pipenv](https://pipenv.pypa.io/en/latest/):
  ```bash
  cd react_intro_api
  pipenv --python 3.12
  pipenv shell
  pipenv install --dev

### Init database
* Migrate database schema:
  ```bash
  make migrate
  ```
* Add new admin user that will have an access to `Admin Panel`:
  ```bash
  make add_admin
  ```
* Type required information:
  ```bash
  (react_intro_api) ls-admin:~/react_intro_api$ make add_admin
  Username (leave blank to use 'ls-admin'): lukasz
  Email address: lukasz@test.com
  Password:
  Password (again):
  This password is too common.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  ```
* Copy file [metacritic_games.csv](https://github.com/prasertcbs/basic-dataset/blob/master/metacritic_games.csv) into
  root project dir and init database:
  ```bash
  wget https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/metacritic_games.csv
  make init_db
  ```

## Test application
* Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and ensure that you see message `It works`.
  If not then maybe you need to redirect port 8000.

## Manage content
* Open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and enter credentials
* You'll be redirected to main page of Admin Panel, where you can manage content.

## Browse API
Open [http://127.0.0.1:8000/api/v1/swagger-ui/](http://127.0.0.1:8000/api/v1/swagger-ui/) to see all available endpoints.
