import random
import unittest

from constants import CLASSIC_FIZZBUZZ_PREFIX, N_ARGS_NAME, SEP_ARGS_NAME, STREAM_PATH
from fastapi.testclient import TestClient
from fastapi_app import app
from fizzbuzz_lib import classic_fizzbuzz_as_text


class TestFastAPIApp(unittest.TestCase):

    def setUp(self) -> None:
        self._seps = [' ', ', ', '; ']
        random.seed()

    def test_classic_fizzbuzz(self):
        """Tests single response of classic fizzbuzz
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
