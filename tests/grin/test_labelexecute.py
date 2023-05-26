"""This module is in charge of testing labelexecute.py"""

import unittest
import grin
from grin.inputconversion import generator_to_token
from grin.labelexecute import label_execute
import contextlib
import io

class TestInputConversion(unittest.TestCase):
    """This class tests functions in inputconversion.py"""
    def test_generator_to_token(self):
        cmd = ['PRINT "HI"']
        result = generator_to_token(cmd)
        # Asserts each token is a GrinToken
        with contextlib.redirect_stdout(io.StringIO()) as output:
            label_execute(result[0], variable_dict = {}, label_dict = {})
        expected_output = 'HI\n'
        self.assertEqual(output.getvalue(), expected_output)