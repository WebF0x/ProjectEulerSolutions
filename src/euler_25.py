from memoized import memoized


@memoized
def get_fibonacci_number(n):
    if n == 1 or n == 2:
        return 1
    return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)


def get_index_of_first_fibonacci_number_with_n_digits(n):
    nb_digits = 0
    index = 0
    while nb_digits != n:
        index += 1
        nb_digits = len(str(get_fibonacci_number(index)))
    return index


def main():
    print(get_index_of_first_fibonacci_number_with_n_digits(1000))


if __name__ == '__main__':
    main()


