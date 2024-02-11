# my_set = set()
#
# for counter in range(10):
#     num = int(input("Enter a number: "))
#     my_set.add(num)
#
# print(my_set)


def sum_collection(numbers: set) -> int:
    return sum(numbers)


def remove_item(numbers: set, number: int) -> int | None:
    if number in numbers:
        numbers.remove(number)
        print("\n", numbers)
        return number

    return None


def find_intersection(set1: set, set2: set) -> set:
    return set1.intersection(set2)
