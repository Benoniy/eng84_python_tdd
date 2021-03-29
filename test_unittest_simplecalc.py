# Create tests to check the code runs without error


from simple_calc import SimpleCalc
import unittest


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):  # Must use "test" in the function name


