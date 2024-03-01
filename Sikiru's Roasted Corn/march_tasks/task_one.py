def calculate(d: str):
    temp = list(map(lambda num: f"{((2 * 50 * int(num) / 30) ** 0.5):.0f}", d.split(",")))
    return "".join([str(element + ",") for element in temp])[:-1]


print(calculate("100,150,180"))
