## library

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/library.svg)](https://github.com/kevinbowen777/library/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A lending library built using the Django web framework

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features
 - Application
     - Add, update, and delete authors and books
     - Borrow, renew, and return books
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
     - image carousel
 - Dev/testing
     - Basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, and 3.11
         - black
         - Sphinx documentaion generation
         - linting
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing)
         - pytest sessions with coverage

---

### Installation
 - `git clone https://github.com/kevinbowen777/library.git`
 - `cd library`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - Comment out the following lines in `accounts/models.py`:
        `library_members, created = Group.objects.get_or_create(name="Library Members")`
        `librarians, created = Group.objects.get_or_create(name="Librarians")`
     - `python manage.py migrate`
     - `python manage.py shell_plus`
         - Create the following groups in the shell:
            - `Group.objects.get_or_create(name="Library Members")`
            - `Group.objects.get_or_create(name="Librarians")`
     - Uncomment the lines previously indicated in `accounts/models.py`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker-compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---

### Application Demo
A live application demonstration hosted at Heroku
 - [library](https://kbowen-django-library.herokuapp.com/)

---

## Screenshots

Home page
![Home Page](https://github.com/kevinbowen777/library/blob/master/images/library_homepage_covers.png)

Catalog Index
![Catalog index](https://github.com/kevinbowen777/library/blob/master/images/library_index_staff.png)

Author list
![author_list](https://github.com/kevinbowen777/library/blob/master/images/library_authorlist_staff.png)

Book list
![Book List](https://github.com/kevinbowen777/library/blob/master/images/library_booklist_staff.png)

---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/library/issues) to view currently open bug reports or open a new issue.
