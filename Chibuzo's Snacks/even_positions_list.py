def even_positions(args):
    counter = 1
    new_list = []

    for items in args:
        if counter % 2 == 0:
            new_list.append(items)
        counter += 1

    return new_list