#!/bin/bash

python manage.py makemigrations
python manage.py migrate
git add .
git status
echo Commit Text:
read pushname
git commit -m $pushname
git push