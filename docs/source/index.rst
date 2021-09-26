.. FizzBuzz Brainstorm documentation master file, created by
   sphinx-quickstart on Wed Sep 22 14:05:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FizzBuzz Brainstorm's documentation!
===============================================

`FizzBuzz <https://wiki.c2.com/?FizzBuzzTest>`_ is a simple test used in programming interviews. Pleasing the friends from `cuban.engineer <https://cuban.engineer/>`_, this repository is just a personal brainstorming on the subject. Project code is available in https://github.com/EStog/fizzbuzz.

To use any part of the project first run in project root directory:

.. code-block:: shell

   $> pip install -r ./requirements.txt


In case you need to generate offline HTML documentation just run in project root directory:

.. code-block:: shell

   $> pip install -r ./docs/requirements.txt
   $> ./build_docs.sh html

To see other available formats run ``build_docs.sh``:

In case you want to run the tests, execute in project root directory:

.. code-block:: console

   $> pip install -r ./tests/requirements.txt
   $> ./run_tests.sh

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   classic_fizzbuzz
   generalized_fizzbuzz
   API/modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
