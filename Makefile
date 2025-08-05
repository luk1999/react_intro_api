add_admin:
	python manage.py createsuperuser

format:
	black --line-length 119 --target-version py312 config/ games/ manage.py

init_db:
	python manage.py init_db_games

migrate:
	python manage.py migrate

run:
	python manage.py runserver
