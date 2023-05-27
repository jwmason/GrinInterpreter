"""This module is in charge of testing labels.py"""

import unittest
import grin
from grin.inputconversion import generator_to_token
from grin.labels import label_check

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