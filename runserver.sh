#!/bin/bash

python manage.py collectstatic
gunicorn csthome.wsgi -b 0.0.0.0:8000
