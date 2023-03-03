pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn django_markdown_docs.wsgi -b :8099