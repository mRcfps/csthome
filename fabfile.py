from __future__ import with_statement

from fabric.api import *

env.hosts = ['root@60.205.183.134']


def deploy_with_private_key():
    with cd("csthome/"):
        run("git pull")
        run("docker-compose down")
        run("docker-compose up --build -d")

        # Keep trying until db is ready
        while True:
            with settings(warn_only=True):
                result = run("docker exec csthome_web_1 python manage.py makemigrations")
            if not result.failed:
                # db is ready, so migrate and exit the loop
                run("docker exec csthome_web_1 python manage.py migrate")
                break
            else:
                # Sleep for a while and try again
                run("sleep 3")


def deploy():
    local("fab deploy_with_private_key -i pf.pem")
