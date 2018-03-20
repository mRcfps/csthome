#!/bin/sh

set -o errexit
set -o nounset


python /app/manage.py collectstatic --noinput
python /app/manage.py migrate
/usr/local/bin/gunicorn config.wsgi -b 0.0.0.0:5000 --chdir=/app
