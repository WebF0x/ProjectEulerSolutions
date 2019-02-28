from src.euler_22 import load_names_file, to_alphabetical_order, get_alphabetical_value, get_names_scores


def test_load_names_from_file():
    test_file_path = 'test_data/p022_names.txt'
    names = load_names_file(test_file_path)
    assert names == ['DEF', 'ABC', 'GHI']


def test_to_alphabetical_order():
    names = ['DEF', 'ABC', 'GHI']
    assert to_alphabetical_order(names) == ['ABC', 'DEF', 'GHI']


def test_alphabetical_value():
    assert get_alphabetical_value('') == 0
    assert get_alphabetical_value('AA') == 2
    assert get_alphabetical_value('ABC') == 6
    assert get_alphabetical_value('DEF') == 15


def test_get_names_scores():
    names = ['A', 'B', 'C']
    names_scores = get_names_scores(names)
    assert names_scores[0] == 1
    assert names_scores[1] == 4
    assert names_scores[2] == 9
