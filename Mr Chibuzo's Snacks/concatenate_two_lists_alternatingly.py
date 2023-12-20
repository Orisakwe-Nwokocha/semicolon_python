def concatenate_two_lists_alternatingly(args_first_list, args_second_list):
    new_list = []
    new_list.extend(args_first_list + args_second_list)

    count = 0
    counter = 0
    while count < len(args_first_list):
        new_list[counter] = args_first_list[count]
        count += 1
        counter += 2

    second_count = 0
    second_counter = 1

    while second_count < len(args_second_list):
        new_list[second_counter] = args_second_list[second_count]
        second_count += 1
        second_counter += 2

    return new_list