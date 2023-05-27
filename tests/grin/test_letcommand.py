"""This module is in charge of testing letcommand.py"""

import unittest

import grin
from grin.inputconversion import generator_to_token
from grin.letcommand import let

class TestLetCommand(unittest.TestCase):
    """This class tests functions in labels.py"""
    def test_let_variable(self):
        line = ['LET A 1']
        line = generator_to_token(line)
        variable_dict = {}
        label_dict = {}
        current_line = 0
        expected_variable_dict = {'A': 1}
        expected_label_dict = {}

        actual_variable_dict, actual_label_dict = let(line, variable_dict, label_dict, current_line)

        self.assertEqual(actual_variable_dict, expected_variable_dict)
        self.assertEqual(actual_label_dict, expected_label_dict)

    def test_let_str_variable(self):
        line = ['LET A "JO"']
        line = generator_to_token(line)
        variable_dict = {}
        label_dict = {}
        current_line = 0
        expected_variable_dict = {'A': "JO"}
        expected_label_dict = {}

        actual_variable_dict, actual_label_dict = let(line, variable_dict, label_dict, current_line)

        self.assertEqual(actual_variable_dict, expected_variable_dict)
        self.assertEqual(actual_label_dict, expected_label_dict)

    def test_let_variable_with_existing_value(self):
        line = ['LET A B']
        line = generator_to_token(line)
        variable_dict = {'B': 2}
        label_dict = {}
        current_line = 0
        expected_variable_dict = {'A': 2, 'B': 2}
        expected_label_dict = {}

        actual_variable_dict, actual_label_dict = let(line, variable_dict, label_dict, current_line)

        self.assertEqual(actual_variable_dict, expected_variable_dict)
        self.assertEqual(actual_label_dict, expected_label_dict)

    def test_let_variable_with_label(self):
        line = ['LET A 5']
        line = generator_to_token(line)
        variable_dict = {}
        label_dict = {'5': 3}
        current_line = 0
        expected_variable_dict = {'A': 5}
        expected_label_dict = {'5': 3}

        actual_variable_dict, actual_label_dict = let(line, variable_dict, label_dict, current_line)

        self.assertEqual(actual_variable_dict, expected_variable_dict)
        self.assertEqual(actual_label_dict, expected_label_dict)

    def test_let_variable_with_label(self):
        line = ['test: LET A 5', 'LET B test']
        line = generator_to_token(line)
        variable_dict = {}
        label_dict = {'5': 3}
        current_line = 0
        expected_variable_dict = {':': 'LET'}
        expected_label_dict = {'5': 3}

        actual_variable_dict, actual_label_dict = let(line, variable_dict, label_dict, current_line)

        self.assertEqual(actual_variable_dict, expected_variable_dict)
        self.assertEqual(actual_label_dict, expected_label_dict)
