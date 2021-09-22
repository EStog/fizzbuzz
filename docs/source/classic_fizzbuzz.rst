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

I changed the description to the following::

      "Write a program that generates the numbers from 1 to n.
      But for multiples of three gives “Fizz” instead of the
      number and for the multiples of five gives “Buzz”. For
      numbers which are multiples of both three and five gives
      “FizzBuzz”."

This gives a more flexible solution. To print the results one just needs to use the generator:

>>> from fizzbuzz import classic_fizzbuzz
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

This allows to store the solution in a container. For example, a list:

>>> a = list(classic_fizzbuzz(10))
>>> a
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']

Other advantages will be discussed soon in other sections.
