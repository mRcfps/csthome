#!/bin/bash

python manage.py collectstatic
python manage.py migrate
gunicorn csthome.wsgi -b 0.0.0.0:8000
