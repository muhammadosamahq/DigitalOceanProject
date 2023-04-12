#!/bin/sh

docker compose --profile main-app-service up --build -d
#sleep 80
docker compose --profile app-py up  --build -d