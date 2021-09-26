Generalized FizzBuzz
====================

.. versionadded:: 0.2.0

FizzBuzz may be generalized to use an arbitrary amount of conditions with its respective replacements. Furthermore, the resultant sequence may be normalized in manner that each element shows a common trait [#f1]_.

:func:`~.general_fizzbuzz` is an alternative implementation of this generalized FizzBuzz.
For example, consider the following case. We have the numbers from 95 to 115, and we want to replace all numbers by a tuple with shape ``(number, string)``, where ``number`` is the current number and ``string`` is (checked in that order):

    - ``"Palindromic"`` if the number is `palindromic <https://en.wikipedia.org/wiki/Palindromic_number>`_,
    - ``"Even"`` if it has an even number of digits.

First let define a simple function to know if a number is palindromic:

.. testcode::

   def is_palindromic(n):
       n = str(n)
       return all(map(lambda x, y: x==y, n, reversed(n)))

.. testcode::
   :hide:

   assert is_palindromic(121)
   assert is_palindromic(1221)
   assert not is_palindromic(123421)

Let then define our mapping from conditions to replacements:

.. testcode::

   mapping = {is_palindromic: lambda x: (x, 'Palindromic'),
              (lambda n: len(str(n)) % 2 == 0): lambda x: (x, 'Even')}

Then, we use :func:`~.general_fizzbuzz` to obtain our list:

.. testcode::

   from fizzbuzz_lib import general_fizzbuzz

   it = general_fizzbuzz(iterable=range(95, 116), mapping=mapping,
                         default= lambda x: x, fusion=lambda ac, r: (ac[0], ac[1]+r[1]),
                         common= lambda x: x)
   print(list(it))

This would output:

.. testoutput::

   [(95, 'Even'), (96, 'Even'), (97, 'Even'), (98, 'Even'), (99, 'PalindromicEven'), 100, (101, 'Palindromic'), 102, 103, 104, 105, 106, 107, 108, 109, 110, (111, 'Palindromic'), 112, 113, 114, 115]

.. rubric:: Footnotes

.. [#f1] Of course, we may generalize even further to the point of seeing FizzBuzz as a `map <https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_ function, but we will not reach that point here because we will be discussing a widely known function and that will just take away all the fun |:wink:|.
