#!/usr/bin/env bash

USER_ID=$(id -u)
GROUP_ID=$(id -g)

name="$1"

shift

docker-compose run --rm --user="${USER_ID}:${GROUP_ID}" $name "${@}"