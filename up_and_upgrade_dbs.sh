# CREATE MIGRATION FOLDERS FOR TESTING AND DEVELOPMENT
# python manage.py db init --directory testing_migrations
# python manage.py db init --directory migrations

# CREATE MIGRATIONS FOR TESTING AND DEVELOPMENT
# python manage.py db migrate --message 'initial database migration' --directory testing_migrations
# python manage.py db migrate --message 'initial database migration' --directory migrations

# STOPING AND STARTING DBS IN CASE THEY WERE PREVIOUSLY RUNNING.
docker-compose stop db_testing
docker-compose stop db
docker-compose up -d db
docker-compose up -d db_testing

# APPLY MIGRATIONS FOR TESTING ANDDEVELOPMENT
python manage.py db upgrade --directory testing_migrations
python manage.py db upgrade --directory migrations