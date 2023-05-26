"""This module is in charge of testing gotogosubcommands.py"""

import unittest
import grin
import contextlib
import io
from grin.gotogosubcommands import find_target_line, goto, gosub


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