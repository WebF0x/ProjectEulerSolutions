from src.euler_21 import sum_of_proper_divisors, are_amicable_numbers, sum_of_amicable_numbers_under_n


def test_sum_of_proper_divisors():
    assert 0 == sum_of_proper_divisors(1)
    assert 1 == sum_of_proper_divisors(2)
    assert 1 == sum_of_proper_divisors(3)
    assert 3 == sum_of_proper_divisors(4)
    assert 1 == sum_of_proper_divisors(5)
    assert 6 == sum_of_proper_divisors(6)
    assert 1 == sum_of_proper_divisors(7)
    assert 284 == sum_of_proper_divisors(220)


def test_are_amicable_numbers():
    assert not are_amicable_numbers(1, 2)
    assert not are_amicable_numbers(3, 2)
    assert not are_amicable_numbers(6, 6)
    assert are_amicable_numbers(220, 284)
    assert are_amicable_numbers(284, 220)
    assert are_amicable_numbers(1184, 1210)
    assert are_amicable_numbers(1210, 1184)


def test_sum_of_amicable_numbers_under_n():
    assert 504 == sum_of_amicable_numbers_under_n(1000)
    assert 2898 == sum_of_amicable_numbers_under_n(2000)
