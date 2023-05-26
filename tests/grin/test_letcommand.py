"""This module is in charge of testing letcommand.py"""

import unittest
from grin.inputconversion import generator_to_token
from grin.letcommand import let

class TestLetCommand(unittest.TestCase):
    """This class tests functions in labels.py"""
    def test_let(self):
        cmd = ['LET A 1']
        line = generator_to_token(cmd)
        var_dict, label_dict = let(line, {}, {}, 0)
        self.assertEqual(var_dict, {'A': 1})
        self.assertEqual(label_dict, {})
