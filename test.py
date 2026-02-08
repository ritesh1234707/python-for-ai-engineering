# from calculator_test import square

# def main(): 
#     test_square()

# def test_square(): 
#     if square(2) != 4: 
#         print(" 2 squared was not 4")
#     if square(3) != 9: 
#         print(" 3 squared was not 9")
#     if square

# if __name__ == "__main__": 
#     main()

''' So in here we are writign more lines of code to 
test a programe than the original program. '''

''' So to fix it there is a function called "assert" 
in python. '''

# from calculator_test import square

# def main(): 
#     test_square()

# def test_square(): 
#     try:
#         assert square(2) == 4
#     except AssertionError: 
#         print("2 squared was not 4")
#     try: 
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared is not 9")
#     try: 
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared is not 4")
#     try: 
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared is not 9")
#     try: 
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared is not 0")

# if __name__ == "__main__": 
#     main()

''' so what assertion does it it tell that it will be always true
so if something will be broken in the main code file it
will throw AsserTionError'''

''' Now we'll use try'''

''' But this is not ideal cause in the main code file we 
only have few lines of code but in the test file 
we have way more than that, whose gonna write more than 
30 lines of code just to test 2 lines of code form main 
file.'''

''' We can use pytest to make things eaisier.'''

# from calculator_test import square

# def test_square(): 
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0


import pytest

from calculator_test import square
# from calculator_test import main

def test_positive(): 
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# def test_main():
#     assert main("cat")

def test_str(): 
    with pytest.raises(TypeError): 
        square("cat") 
    