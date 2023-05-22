"""This module is in charge of testing inputconversion.py"""

import unittest
import grin
from grin.inputconversion import generator_to_token


class GrinTestCase(unittest.TestCase):
    """This class tests functions in inputconversion.py"""
    def test_generator_to_token(self):
        cmd = ['LET A 1']
        result = generator_to_token(cmd)
        # Asserts each token is a GrinToken
        for token in result[0]:
            self.assertEqual(type(token), grin.token.GrinToken)