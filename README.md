# DjangoWebsite
# Introduction
This is a Django website that's written using Django, HTML and CSS. Project name is Foodstore.
It is basically a website that allows customers/users to register/login(saves the info to the django admin where admin has access to the data), browse the menu.

## Contents
* Base django project called Foodstore with its default files incl settings.py
* Main app called foodapp inside project directory
* authentication app 'customers' for logins and registrations
* css static files and html template files also included

## Installation and Usage
Ensure django is installed by running the first command and proceed with the other commands if not:

    $ pip install django

activate the virtual environment

    $ pip install virtualenv

    $ pip install virtualenvwrapper-win

    $ mkvirtualenv my_django

To activate the virtual environment, simply type in:

    $ workon my_django

Start the server using the command: 
    $ python manage.py runserver

Admin login credentials for database : create superuser with password

![image](https://github.com/Nkoalem/DjangoWebsite/assets/97555990/70dd42b4-2d0e-473a-a47d-7985d022a4c4)


from there on, users can navigate around the website.







