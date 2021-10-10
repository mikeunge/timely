#!/usr/local/bin/bash
# build the app

# check if environment file even exists.
if ! [ -f .env ]; then
	printf "Environment file (.env) not found.\n"
	exit 1
fi

# build static files
npm run build

# build docker image(s)
if [ "$1" = "dev" ] || [ "$1" = "debug" ]; then
	docker-compose up
else
	docker-compose up --build --detach
fi