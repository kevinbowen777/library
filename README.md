## library  - A lending library built using the Django web framework

---
## Features
 - Add, update, and delete authors and books
 - Borrow, renew, and return books
 - Email verification for registration, password recovery
 - Support for Social logon authentication (OAuth) (e.g. via GitHub)

### Installation
 - `git clone https://github.com/kevinbowen777/library.git`
 - `cd library`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Live Demo on Heroku:
 - [library](https://kbowen-django-library.herokuapp.com/)
 
## Screenshots

Home page
![Home
Page](https://github.com/kevinbowen777/library/blob/master/images/library_homepage_covers.png)

Catalog Index
![Catalog index](https://github.com/kevinbowen777/library/blob/master/images/library_index_staff.png)

Author list
![author_list](https://github.com/kevinbowen777/library/blob/master/images/library_authorlist_staff.png)

Book list
![Book List](https://github.com/kevinbowen777/library/blob/master/images/library_booklist_staff.png)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/library/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/library/issues)
      to view currently open bug reports or open a new issue.
