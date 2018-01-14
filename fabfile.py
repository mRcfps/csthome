from __future__ import with_statement

from fabric.api import *

env.hosts = ['root@60.205.183.134']


def deploy_with_private_key():
    with cd("csthome/"):
        run("git pull")
        run("docker-compose down")
        run("docker-compose up --build -d")
        run("docker exec csthome_web_1 python manage.py makemigrations")
        run("docker exec csthome_web_1 python manage.py migrate")


def deploy():
    local("fab deploy_with_private_key -i pf.pem")
