Classic FizzBuzz
================

The classic FizzBuzz problem `description <https://wiki.c2.com/?FizzBuzzTest>`_ is as follows::

    "Write a program that prints the numbers from 1 to 100.
    But for multiples of three print “Fizz” instead of the
    number and for the multiples of five print “Buzz”. For
    numbers which are multiples of both three and five print
    “FizzBuzz”."

The solution to the problem has been widely `discussed <https://wiki.c2.com/?FizzBuzzTest>`_.
One possible solution is the following:

.. code-block:: python

    for i in range(0,101):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        print(s) if len(s) else i


Changing the description
------------------------

To solve the problem a more flexible description may be considered::

      "Write a program that generates the numbers from 1 to n.
      But for multiples of three gives “Fizz” instead of the
      number and for the multiples of five gives “Buzz”. For
      numbers which are multiples of both three and five gives
      “FizzBuzz”."

This, in fact, leads to a more flexible solution. To print the results one just needs to use a generator (see :func:`~.classic_fizzbuzz`):

>>> from fizzbuzz_lib import classic_fizzbuzz
>>> for i in classic_fizzbuzz(10):
...     print(i)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz

This allows to store the solution in a container or to use it in a more lazy manner. For example:

>>> [s for s in classic_fizzbuzz(10) if s != 'Buzz']
['1', '2', 'Fizz', '4', 'Fizz', '7', '8', 'Fizz']

In :mod:`~.fizzbuzz_lib` you may find some other useful functions.

CLI script
----------

A CLI script [#fTyper]_ ``fizzbuzz_cli.py`` is available to execute this function from console [#fn]_:

.. code-block:: shell

    fizzbuzz $> ./fizzbuzz_cli.py 10
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz

See ``fizzbuzz_cli.py --help`` for other options.

Web services
------------

Web services [#fFastAPI]_ may also be used to generate the FizzBuzz sequence. Just execute `run_fastapi_server.sh` and then open in a browser http://localhost:8000/docs and a description of the available services will appear. You can also use http://localhost:8000/redoc to see the documentation in an alternative scheme.

The CLI script has also options to act as a client to consume the web services. See ``fizzbuzz_cli.py cfbw --help`` for more details.

.. rubric:: Footnotes

.. [#fTyper] The CLI is written in `Typer <https://typer.tiangolo.com>`_.

.. [#fn] For the sake of simplicity the output is showed after the command, but in fact the output is opened in a new console stream!

.. [#fFastAPI] Web services are written in `FastAPI <https://fastapi.tiangolo.com>`_.
