#!/bin/bash

cd /fan
python3 setup.py install

cd /code
./manage.py migrate
./manage.py runserver 0.0.0.0:80
