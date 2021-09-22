from __future__ import annotations

from typing import Generator


def classic_fizzbuzz(n: int) -> Generator[int | str, None, None]:
    """The classic FizzBuzz.

    The problem description is::

        "Write a program that generates the numbers from 1 to n.
        But for multiples of three gives “Fizz” instead of the
        number and for the multiples of five gives “Buzz”. For
        numbers which are multiples of both three and five gives
        “FizzBuzz”."

    This function gives a generator of ``n`` elements, each one of them complying with the previous description.

    For example:

    .. testsetup ::

       from fizzbuzz_lib import classic_fizzbuzz

    >>> list(classic_fizzbuzz(20))
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']
    >>> list(classic_fizzbuzz(0))
    []
    >>> list(classic_fizzbuzz(-1))
    []
    >>> try:
    ...     list(classic_fizzbuzz(object()))
    ... except TypeError:
    ...     pass # Right!
    ... else:
    ...     print('Wrong!')
    """

    for i in range(1, n+1):
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        if s == '':
            s += str(i)
        yield s if len(s) else i
