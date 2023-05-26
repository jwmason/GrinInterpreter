"""This module is in charge of testing labels.py"""

import unittest
import grin
from grin.inputconversion import generator_to_token
from grin.labels import label_check, label_execute
import contextlib
import io

class TestLabels(unittest.TestCase):
    """This class tests functions in labels.py"""
    def test_label_check(self):
        """This function tests label check function"""
        cmd = ['test: PRINT "TEST"']
        line = generator_to_token(cmd)
        token = line[0][0]
        test_label_dict = label_check(token, line, {})
        for key, value in test_label_dict.items():
            self.assertEqual(type(value[0]), grin.token.GrinToken)

        cmd = ['PRINT "TEST"']
        line = generator_to_token(cmd)
        token = line[0][0]
        test_label_dict = label_check(token, line, {})
        self.assertEqual(test_label_dict, {})

    def test_label_execute(self):
        """This function tests the execution of a label line"""
        cmd = ['PRINT "HI"']
        result = generator_to_token(cmd)
        # Asserts each token is a GrinToken
        with contextlib.redirect_stdout(io.StringIO()) as output:
            label_execute(result[0], variable_dict = {}, label_dict = {})
        expected_output = 'HI\n'
        self.assertEqual(output.getvalue(), expected_output)