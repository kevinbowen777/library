Testing
=======

Running tests against this project can be done in several ways:

  1. Running ``python manage.py test``
  2. Using ``coverage``
  3. Running the ``nox`` test suite

A number of the tests can be executed via the ``run`` file. See the contents of
this file for how these tests can be run.

If you would like to create "test" or "dummy" users, see the :doc:`create_new_users` sections for examples.

Running the Tests
-----------------

Using ``coverage``
^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ coverage run -m pytest
   $ coverage report
   $ coverage html (this will generate html reports available in the ``htmlcov`` directory)
   $ this is a new line

Using the ``nox`` test suite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following sessions are available to run via ``nox``:

::

    - coverage-3.13 -> Generate coverage report.
    - coverage-3.12 -> Generate coverage report.
    - coverage-3.11 -> Generate coverage report.
    - coverage-3.10 -> Generate coverage report.
    - docs-3.13 -> Build the documentation.
    * lint-3.13 -> Lint using ruff.
    * lint-3.12 -> Lint using ruff.
    * lint-3.11 -> Lint using ruff.
    * lint-3.10 -> Lint using ruff.
    * pyright-3.10 -> Check types
    * pyright-3.11 -> Check types
    * pyright-3.12 -> Check types
    * pyright-3.13 -> Check types
    * safety-3.13 -> Scan dependencies for insecure packages.
    * safety-3.12 -> Scan dependencies for insecure packages.
    * safety-3.11 -> Scan dependencies for insecure packages.
    * safety-3.10 -> Scan dependencies for insecure packages.
    * tests-3.13 -> Run the test suite.
    * tests-3.12 -> Run the test suite.
    * tests-3.11 -> Run the test suite.
    * tests-3.10 -> Run the test suite.

    sessions marked with * are selected, sessions marked with - are skipped.

The ``lint``, ``safety``, and ``tests`` are enabled to be run with ``nox -s tests``. Generating documentation, (e.g. ``nox -s docs-3.13``) need to be run explicitly.

Below are some example of ``nox`` commands run locally:

.. code-block:: console

   $ nox --list-sessions
   $ nox
   $ nox -s coverage-3.13
   $ nox -s docs-3.11
   $ nox -rs lint-3.10  (Use the 'r' flag to reuse existing session)
   $ nox -s safety  (will run tests against all Python versions)
   $ nox -s tests

Below are examples of ``nox`` tests run against the Docker container:

.. code-block:: console

   $ docker compose exec web python manage.py test
   $ docker compose exec web nox --list-sessions
   $ docker compose exec web nox
   $ docker compose exec web nox -s coverage-3.12
   $ docker compose exec web nox -s docs-3.11
   $ docker compose exec web nox -rs lint-3.10  (Use the 'r' flag to reuse existing session)
   $ docker compose exec web nox -s safety  (will run tests against all Python versions)
   $ docker compose exec web nox -s tests
