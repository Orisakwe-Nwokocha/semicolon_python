def odd_positions(args):
    new_list = []
    counter = 0

    for items in args:
        if counter % 2 == 0:
            new_list.append(items)
        counter += 1

    return new_list

