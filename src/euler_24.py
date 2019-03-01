import itertools


def get_all_permutations_in_lexicographic_order(symbols):
    return [''.join(permutation) for permutation in itertools.permutations(sorted(symbols))]


def main():
    permutations = get_all_permutations_in_lexicographic_order(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print(permutations[999999])


if __name__ == '__main__':
    main()
