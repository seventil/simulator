# simulator

## based on this article https://testdriven.io/blog/django-and-celery/ and this code base https://github.com/testdrivenio/django-celery/

Build with `docker compose build`

`docker compose exec web python manage.py collectstatic`
`docker compose exec web python manage.py makemigrations`

To debug `docker compose exec web python manage.py shell`.

Run with `docker compose up -d` and check the local at http://localhost:8000/ check flower at http://localhost:5555/
Run with `docker compose up -d --build --scale celery=5` to set up more workers.

To see the web container logs run `docker-compose logs -f`.
To start the migrations run `docker-compose exec web python manage.py migrate --noinput`.

To peek into the postgres db run `docker-compose exec db psql --username=hello_django --dbname=hello_django_dev`.
Or set up a connection in postgres gui app / vscode extension.


Used to be in entrypoint:
python manage.py collectstatic --no-input --clear
python manage.py flush --no-input
