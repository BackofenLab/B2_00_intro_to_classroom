import pytest
from exercise_sheet0 import exercise_1, factorial
from random import randint


def check_none(*args):
    if None in args:
        print("You have not filled in all the fields!")
        raise ValueError


def r_factorial(x):
    if x == 1:
        return 1
    else:
        return x * r_factorial(x-1)


def test_exercise_01():
    a, b, c = exercise_1()
    check_none(a, b, c)
    if a is not False:
        print(f"a) should be False")
        raise ValueError
    if b is not True:
        print(f"b) should be True")
        raise ValueError
    if c is not False:
        print(f"c) should be False")
        raise ValueError


def test_factorial():
    for _ in range(3):
        val = randint(5, 20)
        st_value = factorial(val)
        correct_value = r_factorial(val)
        if st_value != correct_value:
            print(f"You got the wrong factorial value for the input value: {val}\n"
                  f"The correct value is {correct_value}\n"
                  f"You got {st_value}")
            raise ValueError
