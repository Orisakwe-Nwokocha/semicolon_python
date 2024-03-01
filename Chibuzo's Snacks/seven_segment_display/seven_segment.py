from seven_segment_display.exceptions.non_binary_error import NonBinaryNumberError
from seven_segment_display.exceptions.non_digit_error import NonDigitNumberError


class SevenSegmentDisplay:
    def __init__(self):
        self.__isOn = False

    def display_segment(self, digits: str) -> str:
        self.__validate(digits)
        self.__change_status(digits)

        if not self.__isOn:
            return ""

        segment = self.__display_a(digits)
        segment += self.__display_f(digits)
        segment += self.__display_b(digits)
        segment += self.__display_extra(digits, 5, 1)
        segment += self.__display_g(digits)
        segment += self.__display_e(digits)
        segment += self.__display_c(digits)
        segment += self.__display_extra(digits, 4, 2)
        segment += self.__display_d(digits)

        return segment + "\n"

    @staticmethod
    def __display_a(digits: str) -> str:
        return "# # # #" if digits[0] == '1' else "       "

    @staticmethod
    def __display_b(digits: str) -> str:
        return " #" if digits[1] == '1' else "  "

    @staticmethod
    def __display_c(digits: str) -> str:
        return "   #" if digits[2] == '1' else "   "

    @staticmethod
    def __display_d(digits: str) -> str:
        return "\n# # # #" if digits[3] == '1' else "       "

    @staticmethod
    def __display_e(digits: str) -> str:
        return "\n" + ("#  " if digits[4] == '1' else "   ")

    @staticmethod
    def __display_f(digits: str) -> str:
        return "\n" + ("#    " if digits[5] == '1' else "     ")

    @staticmethod
    def __display_g(digits: str) -> str:
        return "\n# # # #" if digits[6] == '1' else "       "

    @staticmethod
    def __display_extra(digits: str, left: int, right: int) -> str:
        temp = ""
        if digits[left] == '1':
            temp += "\n" + "#"
        if digits[right] == '1':
            temp += "     #" if digits[left] == '1' else "\n      #"
        return temp

    def __change_status(self, digits):
        self.__isOn = digits[7] == '1'

    @staticmethod
    def __validate(digits):
        if not digits.isdigit():
            raise NonDigitNumberError("Binary number must be only digits")
        if not all(digit in '01' for digit in digits):
            raise NonBinaryNumberError("Binary number must consist of only 0s and 1s")
        if len(digits) != 8:
            raise ValueError("Binary number must be 8 digits long")

    def is_on(self):
        return self.__isOn


if __name__ == "__main__":
    display = SevenSegmentDisplay()
    # digits_input = input("Enter binary number (8 digits long): ")
    # print(display.display_segment(digits_input))
    print(display.display_segment("11111110"))
    print(display.display_segment("01100111"))
    print(display.display_segment("01100001"))
    print(display.display_segment("11011011"))
    print(display.display_segment("11101111"))
    print(display.display_segment("11101110"))
    print(display.display_segment("11001111"))
    print(display.display_segment("00011101"))
    print("I:\n", display.display_segment("00001101"))
