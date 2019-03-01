from src.euler_24 import get_all_permutations_in_lexicographic_order


def test_get_all_permutations_in_lexicographic_order():
    assert get_all_permutations_in_lexicographic_order(['0', '1', '2']) == ['012', '021', '102', '120', '201', '210']
    assert get_all_permutations_in_lexicographic_order(['2', '1', '0']) == ['012', '021', '102', '120', '201', '210']


def test_get_all_permutations_in_lexicographic_order_for_huge_permutations():
    permutations_from_0_to_9 = get_all_permutations_in_lexicographic_order(
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    )
    assert len(permutations_from_0_to_9) == 3628800
    assert permutations_from_0_to_9[0] == '0123456789'
