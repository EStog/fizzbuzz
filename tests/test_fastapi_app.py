"""Tests for :mod:`~.fastapi_app`
"""

import random
import unittest

from fastapi.testclient import TestClient
from fastapi_app import app
from fastapi_app.constants import (CLASSIC_FIZZBUZZ_PREFIX, N_ARGS_NAME,
                                   SEP_ARGS_NAME, STREAM_PATH)
from fizzbuzz_lib import classic_fizzbuzz_as_text


class TestFastAPIApp(unittest.TestCase):
    """Unittest class to test :mod:`~.fastapi_app`"""

    def setUp(self) -> None:
        self._seps = [' ', ', ', '; ']
        random.seed()

    def test_classic_fizzbuzz(self):
        """Tests classic FizzBuzz web services
        """
        with TestClient(app) as client:
            for i in range(100):
                with self.subTest(i=i):
                    sep = random.choice(self._seps)
                    stream = random.choice([STREAM_PATH, ''])
                    r = client.get(f'/{CLASSIC_FIZZBUZZ_PREFIX}/{stream}',
                                   params={N_ARGS_NAME: i, SEP_ARGS_NAME: sep})
                    self.assertEqual(r.status_code, 200)
                    self.assertEqual(r.text, classic_fizzbuzz_as_text(i, sep))
