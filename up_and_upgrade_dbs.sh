# SETUP Env vars

cp ./.env-copy ./.env

# STOPING AND STARTING DBS IN CASE THEY WERE PREVIOUSLY RUNNING.
docker-compose down

# RUN DB Dev and DB testing
docker-compose up -d db
docker-compose up -d db_testing

# CREATE, GENERATE AND APPLY MIGRATIONS TO DEV DB.

python manage.py db init 
python manage.py db migrate --message 'Initial migration' 
python manage.py db upgrade 
python manage.py load_initial_data

