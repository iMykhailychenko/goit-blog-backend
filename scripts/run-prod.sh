#!/bin/bash

docker-compose -f docker-compose.yml --env-file .env up --build --remove-orphans -d