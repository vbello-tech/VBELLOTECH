web: gunicorn vbello.wsgi
heroku ps:scale web=1
python manage.py collectstatic --noinput