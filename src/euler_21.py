def sum_of_proper_divisors(n):
    proper_divisors = [x for x in range(1, n) if n % x == 0]
    return sum(proper_divisors)


def are_amicable_numbers(a, b):
    if a == b:
        return False
    return sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a


def sum_of_amicable_numbers_under_n(n):
    amicable_numbers_under_n = set()
    for x in range(1, n):
        d_of_x = sum_of_proper_divisors(x)
        if are_amicable_numbers(x, d_of_x):
            amicable_numbers_under_n.add(x)
    return sum(amicable_numbers_under_n)


def main():
    print(sum_of_amicable_numbers_under_n(10000))


if __name__ == "__main__":
    main()


