from src.euler_26 import get_decimals_of_unit_fraction_with_denominator, get_denominator_containing_most_decimals


def test_get_decimals_of_unit_fraction_with_denominator_without_repeating_pattern():
    assert get_decimals_of_unit_fraction_with_denominator(2) == '5'
    assert get_decimals_of_unit_fraction_with_denominator(4) == '25'
    assert get_decimals_of_unit_fraction_with_denominator(5) == '2'
    assert get_decimals_of_unit_fraction_with_denominator(8) == '125'
    assert get_decimals_of_unit_fraction_with_denominator(10) == '1'


def test_get_decimals_of_unit_fraction_with_denominator_with_repeating_pattern():
    assert get_decimals_of_unit_fraction_with_denominator(3) == '(3)'
    assert get_decimals_of_unit_fraction_with_denominator(6) == '1(6)'
    assert get_decimals_of_unit_fraction_with_denominator(7) == '(142857)'
    assert get_decimals_of_unit_fraction_with_denominator(9) == '(1)'


def test_get_denominator_containing_most_decimals():
    assert get_denominator_containing_most_decimals(2) == 2
    assert get_denominator_containing_most_decimals(3) == 3
    assert get_denominator_containing_most_decimals(4) == 3
    assert get_denominator_containing_most_decimals(6) == 3
    assert get_denominator_containing_most_decimals(7) == 7
    assert get_denominator_containing_most_decimals(8) == 7
