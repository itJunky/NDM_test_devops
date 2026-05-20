## start

`docker compose -f ./docker-compose.yml up`

## check

`curl -H "X-Forwarded-For: 1.1.1.1 2.2.2.2" http://localhost:8081/`
