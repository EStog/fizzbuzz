"""This module contains util functions to generate the FizzBuzz sequence. These functions are used by :mod:~.`fizzbuzz_cli` and :mod:`~.fastapi_app`.
"""
from __future__ import annotations
from functools import reduce

from typing import Callable, Iterator, TypeVar
from collections.abc import Mapping, Iterable

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


_E = TypeVar('_E')
_RE = TypeVar('_RE')
_AC= TypeVar('_AC')
_R = TypeVar('_R')

def general_fizzbuzz(iterable: Iterable[_E],
                     mapping: Mapping[Callable[[_E], bool], Callable[[_E], _RE]],
                     default: Callable[[_E], _AC],
                     fusion: Callable[[_AC, _RE], _AC],
                     common: Callable[[_AC], _R]) -> Iterator[_R]:
    """general_fizzbuzz(iterable: Iterable[_E], \
                     mapping: Mapping[Callable[[_E], bool], Callable[[_E], _RE]], \
                     default: Callable[[_E], _AC], \
                     fusion: Callable[[_AC, _RE], _AC], \
                     common: Callable[[_AC], _R]) -> Iterator[_R]

    .. versionadded:: 0.2.0

    This function is to solve a parameterized version of the FizzBuzz problem.
    Instead of receiving just the stop of the sequence, this function receives an ``iterable``, a ``mapping`` from conditions to replacements functions, a ``default`` function that gives a replacement value for the element in question if it does not fulfill any condition, a ``fusion`` function that, for each element, merges in an accumulative manner all the applicable replacements into one, and a ``common`` transformation that is applied to each resultant replacement from the ``fusion`` phase.

    For example:

    .. testsetup ::

       from fizzbuzz_lib import classic_fizzbuzz, classic_fizzbuzz_as_text, general_fizzbuzz

    >>> mod3 = lambda e: e % 3 == 0
    >>> mod5 = lambda e: e % 5 == 0
    >>> mapping={mod3: lambda e: 'Fizz', mod5: lambda e: 'Buzz'}
    >>> fusion = lambda ac, r: ac+r
    >>> assert list(classic_fizzbuzz(100)) == list(general_fizzbuzz(
    ...                                                iterable=range(1, 101),
    ...                                                mapping=mapping,
    ...                                                default=str, fusion=fusion,
    ...                                                common=lambda r: r          ))

    >>> assert classic_fizzbuzz_as_text(100, ', ') == ''.join(general_fizzbuzz(
    ...                                                           iterable=range(1, 101),
    ...                                                           mapping=mapping,
    ...                                                           default=str, fusion=fusion,
    ...                                                           common=lambda r: f'{r}, '   ) )

    >>> list(  general_fizzbuzz(  iterable=range(55, 61),
    ...                           mapping={ mod3: lambda e: 'Fuzzy',
    ...                                     mod5: lambda e: 'Buzzy'  },
    ...                           default=lambda x: 'Normal',
    ...                           fusion=fusion,
    ...                           common=lambda r: f'({r})'              )  )
    ['(Buzzy)', '(Normal)', '(Fuzzy)', '(Normal)', '(Normal)', '(FuzzyBuzzy)']

    >>> list(  general_fizzbuzz(  iterable=range(55, 61),
    ...                           mapping={ mod3: lambda e: (e, 'Fuzzy'),
    ...                                     mod5: lambda e: (e, 'Buzzy')  },
    ...                           default=lambda x: 'Normal',
    ...                           fusion=lambda ac, r: (ac[0], ac[1]+r[1]),
    ...                           common=lambda r: r                          )  )
    [(55, 'Buzzy'), 'Normal', (57, 'Fuzzy'), 'Normal', 'Normal', (60, 'FuzzyBuzzy')]

    .. caution::

       Take into account that this function does not validates if two conditions in the mapping are equivalent.


    """
    for e in iterable:
        it = (cond for cond in mapping if cond(e))
        try:
            ac = mapping[next(it)](e)
        except StopIteration:
            ac = default(e)
        else:
            ac = reduce(lambda ac, cond: fusion(ac, mapping[cond](e)), it, ac)
        yield common(ac)
