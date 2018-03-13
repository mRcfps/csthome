#!/bin/bash

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn csthome.wsgi -b 0.0.0.0:8000
