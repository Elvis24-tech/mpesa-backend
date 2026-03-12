#!/usr/bin/env bash
gunicorn mpesa_project.wsgi:application --bind 0.0.0.0:$PORT