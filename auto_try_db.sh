rm -r data
docker-compose down
docker-compose build db
docker-compose up db