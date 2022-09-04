library - A Django library application
======================================

.. toctree::
   :hidden:
   :maxdepth: 1

   license

This repository runs a Django 4.1 lending library application.

Features
--------

 * Add, update, and delete authors and books
 * Borrow, renew, and return books
 * User registration with email verification & social(GitHub) login
 * Bootstrap4 & crispy-forms decorations
 * Customizable user profiles with bio, profile picture & country flags
 * Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)

Installation
------------

To install the library project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/library.git
   $ cd library

Local install:
--------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser


Docker install:
---------------

.. code-block:: console

   $ docker-compose up --build
   $ docker-compose python manage.py migrate
   $ docker-compose python manage.py createsuperuser


Usage
-----

To run library, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/admin/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker-compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -rs lint-3.11
   $ nox -s tests

Live Application Demonstration on Heroku
----------------------------------------
`kbowen-django-library <https://kbowen-django-library.herokuapp.com/>`_

Reporting Bugs
--------------

Visit the library `Issues page <https://github.com/kevinbowen777/library/issues>`_ on GitHub.
