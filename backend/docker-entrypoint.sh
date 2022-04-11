#!/bin/bash

python3 manage.py collectstatic --noinput

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser \
      --noinput \
      --username admin \
      --email admin@admin.com \

exec "$@"