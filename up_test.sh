docker-compose -f docker-compose.yml -f docker-compose-test.yml build && docker-compose -f docker-compose.yml -f docker-compose-test.yml up --force-recreate
#  --renew-anon-volumes
# Using this flag if db is using anonymous volumes and you have to 
# --renew-anon-volumes alpine and postgres uses anon volumes to persist data.
# Use tmpfs it is even better to avoid using the flag.