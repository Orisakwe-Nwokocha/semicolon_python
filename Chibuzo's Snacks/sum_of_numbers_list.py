def sum_of_numbers_for_loop(args_list):
    sum = 0
    for items in range(len(args_list)):
        sum += args_list[items]
    return sum


def sum_of_numbers_while_loop(args_list):
    sum = 0
    count = 0
    while count < len(args_list):
        sum += args_list[count]
        count += 1
    return sum


def sum_of_numbers_do_while_loop(args_list):
    sum = 0
    count = 0
    while True:
        sum += args_list[count]
        count += 1
        if count == len(args_list):
            break

    return sum