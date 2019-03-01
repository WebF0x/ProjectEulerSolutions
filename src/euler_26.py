def get_decimals_of_unit_fraction_with_denominator(denominator):
    index = 0
    dividend = 1
    remainder = dividend
    remainder_memo = {}
    decimals = []
    while True:
        if remainder in remainder_memo or remainder == 0:
            break
        remainder_memo.update({remainder: index})
        dividend *= 10
        new_decimal = dividend // denominator
        decimals.append(new_decimal)
        remainder = dividend % denominator
        dividend = remainder
        index += 1
    decimals_string = ''.join([str(decimal) for decimal in decimals])
    if remainder == 0:
        return decimals_string
    repeating_part_start = remainder_memo[remainder]
    repeating_part = decimals_string[repeating_part_start:]
    return decimals_string.replace(repeating_part, '(' + repeating_part + ')')


def get_denominator_containing_most_decimals(max_denominator):
    decimals_strings = [
        get_decimals_of_unit_fraction_with_denominator(denominator)
        for denominator in range(2, max_denominator + 1)
    ]

    def extract_repeating_decimals(decimals):
        if '(' not in decimals:
            return ''
        return decimals[decimals.find('(') + 1:decimals.find(')')]
    repeating_decimals = [extract_repeating_decimals(decimals) for decimals in decimals_strings]
    lengths_of_repeating_decimals = [len(repeating_decimal) for repeating_decimal in repeating_decimals]
    return lengths_of_repeating_decimals.index(max(lengths_of_repeating_decimals)) + 2


def main():
    print(get_denominator_containing_most_decimals(999))


if __name__ == '__main__':
    main()
