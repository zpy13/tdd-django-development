Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc

## Notes
###1.
When you need to import listed methods after django 2.0, do

    from django.urls import reverse
    from django.contrib.auth.views import logout_then_login
Instead, do

    from django.core.urlresolvers import reverse
    from django.contrib.auth.views import logout
###2.
You need to delete migrations, collect static files and restart gunicorn 
service manually for deployment.
###3.
In accounts.views.send_mail, qq email's name cannot be changed.
###4.
In accounts.authentication.PasswordlessAuthenticationBackend.authenticate(),
add request to definition after django 2.1.

https://stackoverflow.com/questions/53020872/django-2-1-2-backend-authentication-fails/54708703
###5.
Clean migrations and database.

https://stackoverflow.com/questions/33086444/django-1-8-migrate-is-not-creating-tables
