#!/bin/bash

cd /fan
pip3 install -r requirements.txt
python3 setup.py install

cd /code

fan_register conf.yaml &
./manage.py migrate
./manage.py runserver 0.0.0.0:80
