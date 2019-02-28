import string


def load_names_file(file_path):
    with open(file_path) as file:
        content = file.read()
        content_without_quotes = content.replace('"', '')
        return content_without_quotes.split(',')


def to_alphabetical_order(names):
    return sorted(names)


def get_alphabetical_value(name):
    letter_values = [string.ascii_lowercase.index(letter.lower()) + 1 for letter in name]
    return sum(letter_values)


def get_names_scores(names):
    return [get_alphabetical_value(name) * (index + 1) for index, name in enumerate(names)]


def main():
    file_path = 'resources/p022_names.txt'
    names = load_names_file(file_path)
    names_in_alphabetical_order = to_alphabetical_order(names)
    names_scores = get_names_scores(names_in_alphabetical_order)
    print(sum(names_scores))


if __name__ == "__main__":
    main()
