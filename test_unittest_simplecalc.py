# Create tests to check the code runs without error


from simple_calc import SimpleCalc
import unittest


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):  # Must use "test" in the function name
        self.assertEqual(self.calc.add(2, 4), 6)  # see if the result of this method is 6

