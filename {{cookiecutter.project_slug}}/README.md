{{cookiecutter.project_name}} {{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}

{%- if cookiecutter.open_source_license != "Not open source" %}

:License: {{cookiecutter.open_source_license}}
{%- endif %}

Basic Commands
--------------

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

{%- if cookiecutter.use_docker == 'y' %}

* To build you container use this command::
    docker-compose build

* To run you container use this command::
    docker-compose up -d
    
{%- endif %}
