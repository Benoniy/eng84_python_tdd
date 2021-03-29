# Create tests to check the code runs without error
from simple_calc import SimpleCalc
import unittest


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()  # Create an instance for use in testing

    def test_add(self):  # Must use "test" in the function name
        self.assertEqual(self.calc.add(2, 4), 6)  # see if the result of this method is 6

    def test_sub(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)  # see if the result of this method is 5

    def test_mult(self):
        self.assertEqual(self.calc.multiplication(6, 2), 12)  # see if the result of this method is 12

    def test_div(self):
        self.assertEqual(self.calc.division(9, 3), 3)  # see if the result of this method is 3


# python -m pytest to run all tests
