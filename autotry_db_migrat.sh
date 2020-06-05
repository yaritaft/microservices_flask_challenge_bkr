rm -r migrations
python manage.py db init
python manage.py db migrate --message 'initial database migration'
python manage.py db upgrade