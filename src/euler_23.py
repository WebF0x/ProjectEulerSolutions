from src.euler_21 import sum_of_proper_divisors


def is_abundant(number):
    return sum_of_proper_divisors(number) > number


def get_abundant_numbers_inclusively_up_to(number):
    return [x for x in range(0, number + 1) if is_abundant(x)]


def is_sum_of_two_candidate_numbers(number, candidate_numbers):
    candidate_numbers_lesser_than_number = [x for x in candidate_numbers if x < number]
    for potential_candidate_number in candidate_numbers_lesser_than_number:
        potential_candidate_number_partner = number - potential_candidate_number
        if potential_candidate_number_partner in candidate_numbers_lesser_than_number:
            return True
    return False


def sum_of_all_positive_integers_that_are_sum_of_candidates(max_sum, candidate_numbers):
    sums_of_two_candidate_numbers = set()
    for index, candidate_number in enumerate(candidate_numbers):
        candidate_number_partners = candidate_numbers[index:]
        for candidate_number_partner in candidate_number_partners:
            sum_of_two_candidates = candidate_number + candidate_number_partner
            if sum_of_two_candidates <= max_sum:
                sums_of_two_candidate_numbers.add(sum_of_two_candidates)
    return sum(sums_of_two_candidate_numbers)


def sum_of_all_positive_integers_that_are_not_sum_of_candidates(max_number, candidate_numbers):
    sum_of_all_integers_up_to_max_number = get_sum_of_all_positive_numbers_inclusively_up_to(max_number)
    return (
            sum_of_all_integers_up_to_max_number -
            sum_of_all_positive_integers_that_are_sum_of_candidates(max_number, candidate_numbers)
    )


def get_sum_of_all_positive_numbers_inclusively_up_to(n):
    return int(n * (n + 1) / 2)


def main():
    max_number_that_is_not_sum_of_two_abundant_numbers = 28123
    print(
        'Calculating potential abundant numbers up to',
        max_number_that_is_not_sum_of_two_abundant_numbers
    )
    potential_abundant_numbers = get_abundant_numbers_inclusively_up_to(
        max_number_that_is_not_sum_of_two_abundant_numbers
    )
    print(
        'Found', len(potential_abundant_numbers), 'potential abundant numbers up to',
        max_number_that_is_not_sum_of_two_abundant_numbers
    )
    print('Potential abundant numbers:', potential_abundant_numbers)
    solution = sum_of_all_positive_integers_that_are_not_sum_of_candidates(
        max_number_that_is_not_sum_of_two_abundant_numbers,
        potential_abundant_numbers
    )
    print('Solution:', solution)


if __name__ == '__main__':
    main()
