#!/bin/bash

rm db.sqlite3
rm -rf ./homesapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations homesapi
python3 manage.py migrate homesapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata listing_agents
python3 manage.py loaddata home_types
python3 manage.py loaddata homes

