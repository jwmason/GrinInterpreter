"""This module is in charge of testing gotogosubcommands.py"""

import unittest
import grin
import contextlib
import io
from grin.gotogosubcommands import find_target_line, target_conditional
from grin.inputconversion import generator_to_token


class TestGotoGosubCommands(unittest.TestCase):
    """This class tests functions in gotogosubcommands.py"""
    def test_find_target_line(self):
        """This tests find_target_line"""
        test_target = 1
        test_line = [['test', 1]]
        test_line_dict = {'A': 1}
        output = find_target_line(test_target, test_line, test_line_dict)
        expected_output = 1
        self.assertEqual(output, expected_output)

        test_target = 'A'
        test_line = [['test', 1]]
        test_line_dict = {'A': 1}
        output = find_target_line(test_target, test_line, test_line_dict)
        expected_output = 1
        self.assertEqual(output, expected_output)

        test_target = 'A'
        test_line = [['test', 1]]
        test_line_dict = {'B': 1}
        with self.assertRaises(Exception):
            find_target_line(test_target, test_line, test_line_dict)

        test_target = 1.1
        test_line = [['test', 1]]
        test_line_dict = {'A': 1}
        with self.assertRaises(Exception):
            find_target_line(test_target, test_line, test_line_dict)

    def test_target_conditional_no_if(self):
        line = generator_to_token(['GOTO 10'])
        variable_dict = {}
        line_dict = {'10': 2, '20': 3, '30': 4}
        list_len = 10
        current_line = 1
        expected_result = None

        actual_result = target_conditional(line, variable_dict, line_dict, list_len, current_line)

        self.assertEqual(actual_result, expected_result)

    def test_target_conditional_if_true(self):
        line = generator_to_token(['GOTO 10 IF A > B'])
        variable_dict = {'A': 5, 'B': 3}
        line_dict = {'10': 2, '20': 3, '30': 4}
        list_len = 10
        current_line = 1
        expected_result = None

        actual_result = target_conditional(line, variable_dict, line_dict, list_len, current_line)

        self.assertEqual(actual_result, expected_result)

    def test_target_conditional_if_false(self):
        line = generator_to_token(['GOTO 10 IF A > B'])
        variable_dict = {'A': 3, 'B': 5}
        line_dict = {'10': 2, '20': 3, '30': 4}
        list_len = 10
        current_line = 1
        expected_result = None

        actual_result = target_conditional(line, variable_dict, line_dict, list_len, current_line)

        self.assertEqual(actual_result, expected_result)

    def test_target_conditional_invalid_target(self):
        line = generator_to_token(['GOTO 50'])
        variable_dict = {}
        line_dict = {'10': 2, '20': 3, '30': 4}
        list_len = 10
        current_line = 1
        expected_result = None

        actual_result = target_conditional(line, variable_dict, line_dict, list_len, current_line)

        self.assertEqual(actual_result, expected_result)