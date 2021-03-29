# TDD Test Driven Development  

We will use PyTest unittests  
Its widely used and is cheap  
  

### Best practises:  
make test cases as small and efficient as possible  
name the file test_unittest_thingtotest.py

### TDD Process:  
1. Read, understand, and process the feature or bug request.  
2. Translate the requirement by writing a unit test. If you have hot reloading set up, the unit test will run and fail as no code is implemented yet.  
3. Write and implement the code that fulfills the requirement. Run all tests and they should pass, if not repeat this step.  
4. Clean up your code by refactoring.  
5. Repeat.  


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