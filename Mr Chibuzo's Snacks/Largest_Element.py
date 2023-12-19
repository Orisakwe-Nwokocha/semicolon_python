def largest_element(list_of_numbers):
    largest = list_of_numbers[0]
    for items in range(len(list_of_numbers)):
        if list_of_numbers[items] > largest:
            largest = list_of_numbers[items]

    return largest