#!/bin/bash

for file in app/migrations/*
do
    PGPASSWORD="$POSTGRES_PASSWORD" psql "$POSTGRES_USER" -h "$POSTGRES_HOST" -d "$POSTGRES_DB" -f "$(pwd)/$file" -a
done

