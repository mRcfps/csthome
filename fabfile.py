from __future__ import with_statement

from fabric.api import *

env.hosts = ['root@60.205.183.134']


def local_run():
    try:
        local("docker-compose -f local.yml up --build")
    except KeyboardInterrupt:
        local("docker-compose -f local.yml down")


def deploy_with_private_key():
    with cd("csthome/"):
        run("git pull")
        run("docker-compose -f production.yml build --no-cache")
        run("docker-compose -f production.yml up --force-recreate")


def deploy():
    local("fab deploy_with_private_key -i pf.pem")
