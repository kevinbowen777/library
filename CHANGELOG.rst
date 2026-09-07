.. _`changelog`:

=========
Changelog
=========

``library`` issues are filed on `GitHub <https://github.com/kevinbowen777/library/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

library 0.3.6 (2026-09-06)
==========================

Contributor-facing changes
--------------------------

-  (`#609 <https://github.com/kevinbowen777/library/609>`_): Initial zizmor remediation. Pin GitHub actions to hashes.

-  (`#612 <https://github.com/kevinbowen777/library/612>`_): Update django-debug-toolbar to 7.1.1

-  (`#612 <https://github.com/kevinbowen777/library/612>`_): Update gunicorn to 26.1.0

-  (`#612 <https://github.com/kevinbowen777/library/612>`_): Update sqlparse to 0.6.0

-  (`#612 <https://github.com/kevinbowen777/library/612>`_): Update django-allauth to 65.19.1

-  (`#612 <https://github.com/kevinbowen777/library/612>`_): Update nox to 2026.8.17

library 0.3.5 (2026-08-17)
==========================

Improved documentation
----------------------

-  (`#587 <https://github.com/kevinbowen777/library/587>`_): Add towncrier 25.8.0.


New features
------------

-  (`#611 <https://github.com/kevinbowen777/library/611>`_): Upgrade to Django 6.0.8

library 0.3.4 (2026-07-29)
==========================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#605 <https://github.com/kevinbowen777/library/605>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#607 <https://github.com/kevinbowen777/library/607>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#601 <https://github.com/kevinbowen777/library/601>`_): Drop support for Python 3.11.


New features
------------

-  (`#569 <https://github.com/kevinbowen777/library/569>`_): Upgrade Django to 6.0.7.

library 0.3.3 (2025-05-04)
==========================

Contributor-facing changes
--------------------------

-  (`#515 <https://github.com/kevinbowen777/library/515>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#511 <https://github.com/kevinbowen777/library/511>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#515 <https://github.com/kevinbowen777/library/515>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#516 <https://github.com/kevinbowen777/library/516>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#519 <https://github.com/kevinbowen777/library/519>`_): Replace safety package with pip-audit.

library 0.3.2 (2025-01-17)
==========================

Contributor-facing changes
--------------------------

-  (`#453 <https://github.com/kevinbowen777/library/453>`_): Add support for Python 3.13

-  (`#495 <https://github.com/kevinbowen777/library/495>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#487 <https://github.com/kevinbowen777/library/487>`_): Upgrade Django to 5.1.4

library 0.3.0 (2023-12-30)
==========================

Contributor-facing changes
--------------------------

- : Upgrade Poetry to 1.7.1.

-  (`#196 <https://github.com/kevinbowen777/library/196>`_): Migrate to non-root Docker user & venv.

-  (`#364 <https://github.com/kevinbowen777/library/364>`_): Update Python to 3.12.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#362 <https://github.com/kevinbowen777/library/362>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#360 <https://github.com/kevinbowen777/library/360>`_): Upgrade to Django 5.0.

library 0.2.0 (2023-05-21)
==========================

Contributor-facing changes
--------------------------

-  (`#236 <https://github.com/kevinbowen777/library/236>`_): Install ruff. Drop flake8-* packages.

library 0.1.0 (2023-05-08)
==========================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#221 <https://github.com/kevinbowen777/library/221>`_): Upgrade PostgreSQL to 15.2

-  (`#231 <https://github.com/kevinbowen777/library/231>`_): Migrate from SQLite to PostgreSQL


Improved documentation
----------------------

- : Add Sphinx for documentation


New features
------------

-  (`#233 <https://github.com/kevinbowen777/library/233>`_): Upgrade to Django 4.2.

library 0.0.1 (2022-05-05)
==========================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Support Django 4.0.4

-  (`#9 <https://github.com/kevinbowen777/library/9>`_): Build Docker support for Heroku deployment.


Miscellaneous internal changes
------------------------------

- : Initial commit
