#!/usr/bin/env bash

echo Apply migrations...

python manage.py migrate
python manage.py createsuperuser --noinput

echo migrations ok

exec "$@"