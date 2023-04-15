import pytest
from exercise_sheet0 import (add_numbers,
                             subtract_numbers,
                             multiply_numbers,
                             divide_numbers,
                             remainder,
                             exponentiate,
                             average,
                             gcd,
                             lcm,
                             celsius_to_fahrenheit)


def add_numbers_correct(a, b):
    return a + b


def subtract_numbers_correct(a, b):
    return a - b


def multiply_numbers_correct(a, b):
    return a * b


def divide_numbers_correct(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


def remainder_correct(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a % b


def exponentiate_correct(base, exponent):
    return base ** exponent


def average_correct(numbers):
    return sum(numbers) / len(numbers)


def gcd_correct(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm_correct(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)


def celsius_to_fahrenheit_correct(celsius):
    return (celsius * 9/5) + 32





###################################################
###################################################
#####################Tests#########################


test_data = [
    (3, 5),
    (-2, 7),
    (0, 0),
    (8, 2),
    (7, 3),
]

@pytest.mark.parametrize("a, b", test_data)
def test_add_numbers(a, b):
    assert add_numbers(a, b) == add_numbers_correct(a, b)

@pytest.mark.parametrize("a, b", test_data)
def test_subtract_numbers(a, b):
    assert subtract_numbers(a, b) == subtract_numbers_correct(a, b)

@pytest.mark.parametrize("a, b", test_data)
def test_multiply_numbers(a, b):
    assert multiply_numbers(a, b) == multiply_numbers_correct(a, b)

@pytest.mark.parametrize("a, b", test_data)
def test_divide_numbers(a, b):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            divide_numbers(a, b)
    else:
        assert divide_numbers(a, b) == divide_numbers_correct(a, b)

@pytest.mark.parametrize("a, b", test_data)
def test_remainder(a, b):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            remainder(a, b)
    else:
        assert remainder(a, b) == remainder_correct(a, b)

@pytest.mark.parametrize("base, exponent", test_data)
def test_exponentiate(base, exponent):
    assert exponentiate(base, exponent) == exponentiate_correct(base, exponent)

@pytest.mark.parametrize("numbers", [
    [1, 2, 3, 4, 5],
    [0, 0, 0],
    [10, -10],
])
def test_average(numbers):
    assert average(numbers) == average_correct(numbers)

@pytest.mark.parametrize("a, b", test_data)
def test_gcd(a, b):
    assert gcd(a, b) == gcd_correct(a, b)

@pytest.mark.parametrize("a, b", test_data)
def test_lcm(a, b):
    assert lcm(a, b) == lcm_correct(a, b)

@pytest.mark.parametrize("celsius", [0, 100, -40, 30, 50])
def test_celsius_to_fahrenheit(celsius):
    assert celsius_to_fahrenheit(celsius) == celsius_to_fahrenheit_correct(celsius)
