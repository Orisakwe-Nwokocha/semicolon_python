def calculate(d: str):
    temp = list(map(lambda num: f"{((2 * 50 * int(num) / 30) ** 0.5):.0f}", d.split(",")))

    # list comprehension
    return ",".join([str(element) for element in temp])

    # simple join method
    return ",".join(temp)


print(calculate("100,150,180"))
