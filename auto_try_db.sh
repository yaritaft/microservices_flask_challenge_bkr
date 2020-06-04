rm -r data
docker-compose down
docker-compose build db
sudo chmod -R 777 ./data
docker-compose up db