from math import factorial

from src.euler_20 import sum_of_digits


def test_factorial():
    assert 1 == factorial(0)
    assert 1 == factorial(1)
    assert 2 == factorial(2)
    assert 6 == factorial(3)
    assert 24 == factorial(4)
    assert 120 == factorial(5)
    assert 720 == factorial(6)


def test_sum_of_digits():
    assert 6 == sum_of_digits(123)
    assert 13 == sum_of_digits(4324)
    assert 21 == sum_of_digits(678)
