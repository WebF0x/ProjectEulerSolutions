from src.euler_25 import get_index_of_first_fibonacci_number_with_n_digits, get_fibonacci_number


def test_get_index_of_first_fibonacci_number_with_n_digits():
    assert get_index_of_first_fibonacci_number_with_n_digits(1) == 1
    assert get_index_of_first_fibonacci_number_with_n_digits(2) == 7
    assert get_index_of_first_fibonacci_number_with_n_digits(3) == 12


def test_get_fibonacci_number():
    assert get_fibonacci_number(1) == 1
    assert get_fibonacci_number(2) == 1
    assert get_fibonacci_number(3) == 2
    assert get_fibonacci_number(4) == 3
    assert get_fibonacci_number(5) == 5
    assert get_fibonacci_number(6) == 8
    assert get_fibonacci_number(50) == 12586269025
