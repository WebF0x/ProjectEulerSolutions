from math import factorial


def sum_of_digits(number):
    number_word = str(number)
    number_digits = [int(digit_char) for digit_char in number_word]
    return sum(number_digits)


def main():
    print(sum_of_digits(factorial(100)))


if __name__ == "__main__":
    main()
