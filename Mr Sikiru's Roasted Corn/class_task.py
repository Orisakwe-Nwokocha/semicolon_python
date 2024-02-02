def list_of_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return numbers


def length_of_list() -> int:
    length = 0

    for _ in list_of_numbers():
        length += 1

    return length


def sum_of_numbers_at_even_positions() -> int:
    total = 0

    for index in range(1, length_of_list(), 2):
        total += list_of_numbers()[index]

    return total


def sum_of_numbers_at_odd_positions() -> int:
    total = 0

    for index in range(0, length_of_list(), 2):
        total += list_of_numbers()[index]

    return total


def multiply_numbers_at_every_third_position() -> int:
    product = 1

    for index in range(2, length_of_list(), 3):
        product *= list_of_numbers()[index]

    return product


def average_of_all_numbers_in_a_list() -> float:
    return (sum_of_numbers_at_even_positions() + sum_of_numbers_at_odd_positions()) / length_of_list()


def largest_number_in_the_list() -> int:
    largest = list_of_numbers()[0]

    for number in list_of_numbers():
        if number > largest:
            largest = number

    return largest


def smallest_number_in_the_list() -> int:
    smallest = list_of_numbers()[0]

    for number in list_of_numbers():
        if number < smallest:
            smallest = number

    return smallest


def number_of_strings_in_a_list(strings: list):
    if len(strings) == 0:
        return []

    list_of_strings = []

    for string in strings:
        condition = len(string) >= 2 and string[0] == string[-1]
        if condition:
            list_of_strings.append(string)

    return list_of_strings
