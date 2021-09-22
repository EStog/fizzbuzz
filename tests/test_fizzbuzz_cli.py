import subprocess

import unittest

class TestCLI(unittest.TestCase):

    def test_cli_classic_fizzbuzz_fail(self):
        """Tests CLI classic fizzbuzz fail when entering a wrong value"""
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.run(['python', 'ww'], check=True)
