"""Tests for :mod:`~.fizzbuzz_cli`
"""

import random
import unittest

import fastapi.testclient
import fastapi_app
import fizzbuzz_cli
import typer.testing
from fizzbuzz_cli import (CLASSIC_FIZZBUZZ_COMMAND,
                          CLASSIC_FIZZBUZZ_FROM_WEB_COMMAND, app)
from fizzbuzz_lib import classic_fizzbuzz_as_text


class TestCLI(unittest.TestCase):
    """Unittest class to test :mod:`~.fizzbuzz_cli`
    """

    def setUp(self) -> None:
        self._runner = typer.testing.CliRunner()
        self._seps = [' ', ', ', '; ']
        random.seed()
        fizzbuzz_cli.web_client = fastapi.testclient.TestClient(fastapi_app.app)

    def test_cli_classic_fizzbuzz_fail(self):
        """Checks that CLI classic-fizzbuzz command fails when entering a wrong value
        """
        r = self._runner.invoke(app, [CLASSIC_FIZZBUZZ_COMMAND, 'wwe'])
        self.assertNotEqual(r.exit_code, 0)

    def _options(self):
        for i in range(50):
            with self.subTest(i=i):
                sep = random.choice(self._seps)
                yield [str(i), '--sep', sep], classic_fizzbuzz_as_text(i, sep)+'\n'

    def _test_run(self, command, options, patron):
        r = self._runner.invoke(app, [command, *options])
        self.assertEqual(r.exit_code, 0)
        self.assertEqual(r.stdout, patron)

    def test_classic_fizzbuzz(self):
        """Tests classic-fizzbuzz command
        """
        for options, patron in self._options():
            self._test_run(CLASSIC_FIZZBUZZ_COMMAND, options, patron)

    def test_classic_fizzbuzz_web(self):
        """Tests classic-fizzbuzz-from-web command
        """
        for options, patron in self._options():
            self._test_run(CLASSIC_FIZZBUZZ_FROM_WEB_COMMAND,
                           [random.choice(['--stream', '--no-stream']), *options],
                           patron)