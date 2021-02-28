Provisioning a new site 

======================

## Required packages:
* nginx
* python 3.8
* virtualenv + virtualenvwrapper + pip
* Git

eg, on Ubuntu:

	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install nginx git python3.8 virtualenv virtualenvwrapper

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.superlists.pl

## Systemd service

* see gunicorn=systemd.template.service
* replace DOMAIN with, e.g., staging.superlists.pl

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
