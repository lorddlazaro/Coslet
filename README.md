Coslet
======

Cosplay E-Commerce Site


Installation

1. Install Python 3.4
2. Add python 3.4 path to Environment Variables
  - Restart Command Line
3. Install Pip for python
  - try running pip on command line, if not recognized add C:/python34/scripts to environment variables
4. Make project directory and go to directory
5. install virtualenv by "pip install virtualenv"
6. create virtual environment by "virtualenv env"
- activate virtual environment by going to scripts folder "cd /env/scripts/" then "activate"
  - run "deactivate" to deactivate virtual environment
- install django "pip install django"
- initialize source control "git init"
- add remote repo for git "git remote add origin <link>"
- pull project "git pull origin master"
- install mysql-connector for python https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.0.1.zip
  instructions: http://dev.mysql.com/doc/connector-python/en/connector-python-installation-source-windows.html
- edit coslet/coslet/settings.py and change DATABASE settings 
    DATABASES = {
      'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'dbName',
        'USER': 'dbUser',
        'PASSWORD': 'dbPassword',
        'HOST': 'localhost',
        'PORT': '3306',
      }
    }
- create database in mysql
- to create models to tables from coslet/coslet/models.py "python manage.py migrate"
- run "python manage.py runserver" to run server and access on 127.0.0.1:8000 on browser (IE Sucks)
