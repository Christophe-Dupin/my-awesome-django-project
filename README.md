Cookiecutter django project
===================

Is it a framework for jumpstarting a production ready Django project

Features
---------

* For Django 3.1
* Works with Python 3.9
* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)
* Customizable PostgreSQL version

Optional Integrations
---------------------
.. _Traefik: https://traefik.io/
.. _LetsEncrypt: https://letsencrypt.org/
.. _pre-commit: https://github.com/pre-commit/pre-commit
.. _docker-compose: https://github.com/docker/compose

Usage
------

Let's pretend you want to create a Django project called "my_awesome_django_project". Rather than using ``startproject``
So you have to use this cookiecutter to start with a clean and quick install.

First you have to install cookiecutter::

    pip install "cookiecutter>=1.7.0"

Now run it again the repo::

    $ cookiecutter https://github.com/christophe-dupin/my-awesome-django-project


You'll be prompted for some values. Provide them, then a Django project will be created for you.

Enter the project and take a look around::

    $ cd my_awesome_django_project/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:christophe-dupin/my_awesome_django_project.git
    $ git push -u origin master

Now take a look at your repo and enjoy the ride.