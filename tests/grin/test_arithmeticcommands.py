"""This module is in charge of testing arithmeticcommands.py"""

import unittest
from grin.arithmeticcommands import add, subtract, multiply, divide


class TestArithmeticCommands(unittest.TestCase):
    """This class tests functions in arithmeticcommands.py"""
    def test_add(self):
        test_num1 = 1
        test_num2 = 2
        test_num3 = 1.0
        test_num4 = 2.0
        sum = add(test_num1, test_num2)
        sum2 = add(test_num3, test_num4)
        expected_sum = 1 + 2
        expected_sum2 = 3
        self.assertEqual(sum, expected_sum)
        self.assertEqual(sum2, expected_sum2)


    def test_subtract(self):
        test_num1 = 1
        test_num2 = 2
        test_num3 = 1.0
        test_num4 = 2.0
        difference = subtract(test_num1, test_num2)
        difference2 = subtract(test_num3, test_num4)
        expected_difference = 1 - 2
        expected_difference2 = -1
        self.assertEqual(difference, expected_difference)
        self.assertEqual(difference2, expected_difference2)

    def test_multiply(self):
        test_num1 = 1
        test_num2 = 2
        test_num3 = 1.0
        test_num4 = 2.0
        product = multiply(test_num1, test_num2)
        product2 = multiply(test_num3, test_num4)
        expected_product = 1 * 2
        expected_product2 = 2
        self.assertEqual(product, expected_product)
        self.assertEqual(product2, expected_product2)

    def test_quotient(self):
        test_num1 = 1
        test_num2 = 2
        test_num3 = 2.0
        test_num4 = 2.0
        quotient = divide(test_num1, test_num2)
        quotient2 = divide(test_num3, test_num4)
        expected_quotient = 1 / 2
        expected_quotient2 = 1
        self.assertEqual(quotient, expected_quotient)
        self.assertEqual(quotient2, expected_quotient2)