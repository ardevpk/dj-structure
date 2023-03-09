actv:
	source ../env/bin/activate
run:
	python manage.py runserver
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
static:
	python manage.py collectstatic
reload:
	sudo supervisorctl reload
	sudo systemctl reload nginx
	sudo service nginx restart

