
clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

user:
	python manage.py createsuperuser

shell:
	python manage.py shell

test:
	python manage.py test

coverage:
	coverage run manage.py test
	coverage report
install:
	pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt