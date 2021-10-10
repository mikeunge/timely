#!/usr/local/bin/bash
environment=$1
if [ -z $environment ]; then
    printf "No arguments provided.\n"
    exit 1
fi
# check if environment file even exists.
if ! [ -f .env.$environment ]; then
	printf "Environment file not found.\n"
	exit 1
else
	if [ -f .env ]; then
		rm .env
	fi
	cp .env.$environment .env
fi

npm run build
docker-compose -d up