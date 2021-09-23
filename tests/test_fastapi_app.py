import random
import unittest

from fastapi.testclient import TestClient
from fizzbuzz_lib import classic_fizzbuzz_as_text
from fastapi_app import app, classic_fizzbuzz_prefix


class TestFastAPIApp(unittest.TestCase):

    def setUp(self) -> None:
        self._seps = [' ', ', ', '; ']
        random.seed()

    def test_get_plain_result_classic_fizzbuzz(self):
        """Tests single response of classic fizzbuzz"""
        with TestClient(app) as client:
            for i in range(100):
                with self.subTest(i=i):
                    sep = random.choice(self._seps)
                    r = client.get(f'/{classic_fizzbuzz_prefix}/',
                                            params={'n': i, 'sep': sep})
                    self.assertEqual(r.status_code, 200)
                    self.assertEqual(r.text, classic_fizzbuzz_as_text(i, sep))

    def test_get_stream_result_classic_fizzbuzz(self):
        """Tests stream response of classic fizzbuzz"""
        with TestClient(app) as client:
            for i in range(100):
                with self.subTest(i=i):
                    sep = random.choice(self._seps)
                    r = client.get(f'/{classic_fizzbuzz_prefix}/stream/',
                                            params={'n': i, 'sep': sep})
                    text = bytes()
                    for content in r.iter_lines():
                        text += content
                    self.assertEqual(r.status_code, 200)
                    self.assertEqual(str(text, r.encoding), classic_fizzbuzz_as_text(i, sep))
