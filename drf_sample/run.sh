#!/bin/bash

cd /fan
# pip3 install -r requirements-dev.txt
# python3 setup.py install

cd /code

python3 /fan/fan/contrib/sync_helper/fan_register.py conf.yaml &
./manage.py migrate
./manage.py runserver 0.0.0.0:80
