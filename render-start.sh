#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=mpesa_project.settings
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn mpesa_project.wsgi:application --bind 0.0.0.0:$PORT