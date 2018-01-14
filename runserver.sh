#!/bin/bash

python manage.py collectstatic --no-input
gunicorn csthome.wsgi -b 0.0.0.0:8000
