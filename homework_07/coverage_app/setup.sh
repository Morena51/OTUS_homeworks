#!/usr/bin/env bash

echo Apply migrations...

python manage.py migrate

echo migrations ok

exec "$@"