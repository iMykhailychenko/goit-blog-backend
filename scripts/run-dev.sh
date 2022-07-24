#!/bin/bash

docker-compose -f docker-compose.dev.yml --env-file .env.dev up --build --remove-orphans -d