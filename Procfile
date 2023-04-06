release: python manage.py migrate --noinput
release: python manage.py makemigrations --noinput
web: gunicorn api.wsgi --log-file -