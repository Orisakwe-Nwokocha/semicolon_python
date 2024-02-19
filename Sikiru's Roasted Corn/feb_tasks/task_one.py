from typing import List


def create_sequential_integers_list() -> List:
    return list(range(1, 16))


def duplicate_numbers_in_a_list() -> List:
    list1 = create_sequential_integers_list()
    for number in create_sequential_integers_list():
        list1.append(number)

    return list1


def remove_duplicated_numbers_in_a_list(numbers: list) -> List:
    list1 = []
    for number in numbers:
        if number not in list1:
            list1.append(number)

    return list1


def add_every_third_element_in_a_list(sample_list) -> int:
    return sum(sample_list[2::3])


def sum_first_middle_and_last_elements(sample_list) -> int | float:
    total = sample_list[0] + sample_list[-1]

    index = len(sample_list) // 2

    if len(sample_list) % 2 == 0:
        index = (sample_list[index] + sample_list[index - 1]) / 2
        return total + index

    return total + sample_list[index]
