"""This module is in charge of testing relationaloperationcommands.py"""

import unittest
from grin.relationaloperationcommands import relational_operation


class TestRelationalOperationCommands(unittest.TestCase):
    """This class tests functions in relationaloperationcommands.py"""
    def test_relational_operation(self):
        """This function tests relational operation function"""
        # True tests
        true_test1 = relational_operation(2, 1, '>')
        true_test2 = relational_operation(2, 2, '>=')
        true_test3 = relational_operation(1, 2, '<')
        true_test4 = relational_operation(2, 2, '<=')
        true_test5 = relational_operation(2, 2, '=')
        true_test6 = relational_operation(1, 2, '<>')

        self.assertEqual(true_test1, True)
        self.assertEqual(true_test2, True)
        self.assertEqual(true_test3, True)
        self.assertEqual(true_test4, True)
        self.assertEqual(true_test5, True)
        self.assertEqual(true_test6, True)

        # False tests
        false_test1 = relational_operation(2, 1, '<')
        false_test2 = relational_operation(2, 3, '>=')
        false_test3 = relational_operation(1, 2, '>')
        false_test4 = relational_operation(3, 2, '<=')
        false_test5 = relational_operation(2, 3, '=')
        false_test6 = relational_operation(2, 2, '<>')

        self.assertEqual(false_test1, False)
        self.assertEqual(false_test2, False)
        self.assertEqual(false_test3, False)
        self.assertEqual(false_test4, False)
        self.assertEqual(false_test5, False)
        self.assertEqual(false_test6, False)

        # Additional tests for code coverage
        self.assertEqual(relational_operation(2, 2, ''), False)
        self.assertEqual(relational_operation(2, 2, None), False)