# book-trading
It is webapp for exchanging books between users or user and markets.
Allows users and markets to publish secondhand books.
Has email and sms services to verify users and notice users about thier requests and activities they get from other users and markets.
Has notification service with firebase.
and i will add chat app too.

for use this app use requirements that written below and in notification app's readme.

create venv:
$ py -m venv env

clone app

$ pip install requirements.txt

read README of notification app

$ py manage.py makemigrations

$ py manage.py migrate

$ py manage.py runserver
