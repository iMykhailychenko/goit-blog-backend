#!/bin/bash

docker-compose stop
docker image prune -a -f
docker-compose -f docker-compose.dev.yml --env-file .env.dev up --build --remove-orphans -d