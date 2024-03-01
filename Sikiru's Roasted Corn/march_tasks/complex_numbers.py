class ComplexNumbers:
    def __init__(self, left, right):
        self.__left = left
        self.__right = right

    def __add__(self, other):
        return ComplexNumbers(self.__left + other.__left, self.__right + other.__right)

    def __iadd__(self, other):
        ComplexNumbers(self.__left + other.__left, self.__right + other.__right)
        return self

    def __sub__(self, other):
        return ComplexNumbers(self.__left - other.__left, self.__right - other.__right)

    def __eq__(self, other):
        return self.__left == other.__left and self.__right == other.__right

    def __gt__(self, other):
        return self.__left > other.__left and self.__right > other.__right

    def __repr__(self):
        return f"{self.__left}j {"+" if self.__right > 0 else "-"} {abs(self.__right)}i"


c1: ComplexNumbers = ComplexNumbers(2, 3)
c2: ComplexNumbers = ComplexNumbers(5, 5)
c3: ComplexNumbers = ComplexNumbers(2, 3)
print(c1)
print(c2)
c1 += c2
print(c1)
c1 -= c2
print(c1)
# print(c1 - c2)
# print(c1 == c3)
# print(c1 != c3)
# print("c1 > c2:", c1 > c2)
# print("c2 > c1:", c2 > c1)

