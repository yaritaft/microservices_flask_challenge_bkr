# CREATE, GENERATE AND APPLY MIGRATIONS TO DEV DB.

python manage.py db init 
python manage.py db migrate --message 'Initial migration' 
python manage.py db upgrade 
python manage.py load_initial_data

