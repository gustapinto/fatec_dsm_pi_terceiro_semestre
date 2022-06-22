#!/bin/sh
python ./consumidor/main.py mongodb://consumidor:consumidor@mongo:27017 &
python ./site/manage.py migrate && python ./site/manage.py runserver 0.0.0.0:8000
