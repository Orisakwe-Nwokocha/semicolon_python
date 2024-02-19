def list_of_digits(args):
    if args < 0:
        args *= -1
    modded_args = str(args)
    new_list = []
    index = 0

    while index < len(modded_args):
        new_list.append(args % 10)
        args //= 10
        index += 1

    new_list.reverse()

    return new_list

a = -2342
b = str(a)

print(b)
print(len(b))