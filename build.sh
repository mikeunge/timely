#!/usr/bin/bash
environment=$1
if [ -z $environment ]; then
    printf "No arguments provided.\n"
    exit 1
fi

# check what the user wants to build.
# if dev (developmnent) or prod (production).
if [[ $environment == "dev" ]]; then
    sudo docker-compose -d --env-file .env.dev up
else
    sudo docker-compose -d --env-file .env.prod up
fi
