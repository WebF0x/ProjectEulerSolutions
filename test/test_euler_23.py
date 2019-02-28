from src.euler_23 import is_abundant, get_abundant_numbers_inclusively_up_to, \
    is_sum_of_two_candidate_numbers, sum_of_all_positive_integers_that_are_sum_of_candidates, \
    sum_of_all_positive_integers_that_are_not_sum_of_candidates, get_sum_of_all_positive_numbers_inclusively_up_to


def test_is_abundant_number():
    assert not is_abundant(0)
    assert not is_abundant(1)
    assert not is_abundant(11)
    assert is_abundant(12)


def test_get_abundant_numbers_inclusively_up_to():
    assert get_abundant_numbers_inclusively_up_to(11) == []
    assert get_abundant_numbers_inclusively_up_to(12) == [12]
    assert get_abundant_numbers_inclusively_up_to(35) == [12, 18, 20, 24, 30]


def test_is_sum_of_two_candidate_numbers():
    assert not is_sum_of_two_candidate_numbers(0, [3, 5])
    assert not is_sum_of_two_candidate_numbers(1, [3, 5])
    assert not is_sum_of_two_candidate_numbers(2, [3, 5])
    assert not is_sum_of_two_candidate_numbers(3, [3, 5])
    assert not is_sum_of_two_candidate_numbers(4, [3, 5])
    assert not is_sum_of_two_candidate_numbers(5, [3, 5])
    assert is_sum_of_two_candidate_numbers(6, [3, 5])
    assert not is_sum_of_two_candidate_numbers(7, [3, 5])
    assert is_sum_of_two_candidate_numbers(8, [3, 5])
    assert not is_sum_of_two_candidate_numbers(9, [3, 5])
    assert is_sum_of_two_candidate_numbers(10, [3, 5])


def test_sum_of_all_positive_integers_that_are_sum_of_candidates():
    assert type(sum_of_all_positive_integers_that_are_sum_of_candidates(6, [])) is int
    assert sum_of_all_positive_integers_that_are_sum_of_candidates(6, [0]) == 0
    assert sum_of_all_positive_integers_that_are_sum_of_candidates(6, [1]) == 2
    assert sum_of_all_positive_integers_that_are_sum_of_candidates(6, [2]) == 4
    assert sum_of_all_positive_integers_that_are_sum_of_candidates(6, [1, 2]) == 9
    assert sum_of_all_positive_integers_that_are_sum_of_candidates(6, [1, 2, 3]) == 20
    assert sum_of_all_positive_integers_that_are_sum_of_candidates(6, [1, 2, 3, 4]) == 20


def test_get_sum_of_all_positive_numbers_up_to():
    assert type(get_sum_of_all_positive_numbers_inclusively_up_to(1)) is int
    assert get_sum_of_all_positive_numbers_inclusively_up_to(1) == 1
    assert get_sum_of_all_positive_numbers_inclusively_up_to(2) == 3
    assert get_sum_of_all_positive_numbers_inclusively_up_to(3) == 6
    assert get_sum_of_all_positive_numbers_inclusively_up_to(4) == 10
    assert get_sum_of_all_positive_numbers_inclusively_up_to(5) == 15
    assert get_sum_of_all_positive_numbers_inclusively_up_to(6) == 21
    assert get_sum_of_all_positive_numbers_inclusively_up_to(100) == 5050


def test_sum_of_all_positive_integers_that_are_not_sum_of_candidates():
    assert type(sum_of_all_positive_integers_that_are_not_sum_of_candidates(6, [])) is int
    assert sum_of_all_positive_integers_that_are_not_sum_of_candidates(6, []) == 21
    assert sum_of_all_positive_integers_that_are_not_sum_of_candidates(6, [1]) == 19
    assert sum_of_all_positive_integers_that_are_not_sum_of_candidates(6, [1, 2]) == 12
    assert sum_of_all_positive_integers_that_are_not_sum_of_candidates(6, [1, 2, 3]) == 1
    assert sum_of_all_positive_integers_that_are_not_sum_of_candidates(6, [1, 2, 3, 4]) == 1
