"""This module contains util functions to generate the FizzBuzz sequence. These functions are used by :mod:~.`fizzbuzz_cli` and :mod:`~.fastapi_app`.
"""
from __future__ import annotations

from typing import Iterator


def classic_fizzbuzz(n: int) -> Iterator[str]:
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
        yield s if s else str(i)


def gen_text(gen: Iterator, sep: str):
    """Gives the content of ``gen`` as a generator of strings with suffix ``sep``"""
    return (f'{s}{sep}' for s in gen)


def as_text(gen: Iterator, sep: str):
    """Gives the content of ``gen`` as a text where each element is separated by ``sep``"""
    s = ''
    for x in gen_text(gen, sep):
        s += x
    return s


def classic_fizzbuzz_as_text(n: int, sep: str):
    """Gives classic FizzBuzz sequence as a text where each element is separated by ``sep``"""
    return as_text(classic_fizzbuzz(n), sep)


def classic_fizzbuzz_as_gen_text(n: int, sep: str):
    """Gives classic FizzBuzz sequence as a generator of strings with suffix ``sep``"""
    return gen_text(classic_fizzbuzz(n), sep)
