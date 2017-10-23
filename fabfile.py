from fabric.api import *

env.hosts = ['root@60.205.183.134']


def deploy_with_private_key():
    run("git pull")
    run("docker-compose down")
    run("docker-compose up --build -d")


def deploy():
    local("fab deploy_with_private_key -i pf.pem")
