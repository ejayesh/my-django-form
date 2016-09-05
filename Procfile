web: gunicorn letsdjango.wsgi --log-file -
worker: celery worker --app=letsdjango.celery.app --loglevel=info
