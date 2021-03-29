# TDD Test Driven Development  

### What is TTD and what are its benefits?
We will use PyTest unittests  
Its widely used and is cheap  


### Best practises:  
make test cases as small and efficient as possible  
name the file test_unittest_thingtotest.py

### TDD Process:  
1. Read, understand, and process the feature or bug request.  
   

2. Translate the requirement by writing a unit test. If you have hot reloading set up, the unit test will run and  
   fail as no code is implemented yet.  
   

3. Write and implement the code that fulfills the requirement. Run all tests, and they should pass, if not repeat  
   this step.  
   

4. Clean up your code by refactoring.  
   

5. Repeat.  


[Imgur](https://i.imgur.com/F5a2IxC.png)

### List of assertions in unit testing:

|Method                   |   Checks that          |New in|
|:---                     |:---                    |:---  |
|assertEqual(a, b)        |    a == b              |      |
|assertNotEqual(a, b)     |    a != b              |      |  
|assertTrue(x)            |    bool(x) is True     |      |  
|assertFalse(x)           |    bool(x) is False    |      |  
|assertIs(a, b)           |    a is b              |3.1   |
|assertIsNot(a, b)        |    a is not b          |3.1   |
|assertIsNone(x)          |    x is None           |3.1   |
|assertIsNotNone(x)       |    x is not None       |3.1   |
|assertIn(a, b)           |    a in b              |3.1   |
|assertNotIn(a, b)        |    a not in b          |3.1   |
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2   |
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2   | 


### Test code:  

```python
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
# python -m pytest -v to run all test verbose (super good)
```

### Code that gets tested: 
```python
class SimpleCalc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2
```
