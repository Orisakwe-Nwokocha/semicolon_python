def running_total(args):
    new_list = []
    sum = 0
    for items in range(len(args)):
        new_list.append(args[items] + sum)
        sum += args[items]

    return new_list