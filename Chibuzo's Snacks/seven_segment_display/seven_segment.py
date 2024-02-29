from seven_segment_display.exceptions.non_binary_error import NonBinaryNumberError
from seven_segment_display.exceptions.non_digit_error import NonDigitNumberError


class SevenSegmentDisplay:
    def __init__(self):
        self.__isOn = False

    def display_segment(self, digits):
        self.__validate(digits)
        self.__change_status(digits)

        if not self.__isOn:
            return ""

        segment_key = digits[:7]
        segment_dict = {
            "1111110": "# # # #\n#     #\n#     #\n#     #\n# # # #",
            "0110000": "\t  #\n\t  #\n\t  #\n\t  #\n\t  #",
            "1101101": "# # # #\n      #\n# # # #\n#      \n# # # #",
            "1111001": "# # # #\n      #\n# # # #\n      #\n# # # #",
            "0110011": "#     #\n#     #\n# # # #\n      #\n      #",
            "1011011": "# # # #\n#      \n# # # #\n      #\n# # # #",
            "1011111": "# # # #\n#      \n# # # #\n#     #\n# # # #",
            "1110000": "# # # #\n      #\n      #\n      #\n      #",
            "1111111": "# # # #\n#     #\n# # # #\n#     #\n# # # #",
            "1111011": "# # # #\n#     #\n# # # #\n      #\n# # # #"
        }

        if segment_key in segment_dict:
            return segment_dict[segment_key] + "\n"
        else:
            return self.__display_segment_alphabet(digits)

    @staticmethod
    def __display_segment_alphabet(digits):
        output = ""

        output += "# # # #" if digits[0] == '1' else "       "
        output += "\n" + ("#    " if digits[5] == '1' else "     ")
        output += " #" if digits[1] == '1' else "  "
        output += "\n# # # #" if digits[6] == '1' else "       "
        output += "\n" + ("#  " if digits[4] == '1' else "   ")
        output += "   #" if digits[2] == '1' else "   "
        output += "\n# # # #" if digits[3] == '1' else "       "

        return output + "\n"

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
    digits_input = input("Enter binary number (8 digits long): ")
    print(display.display_segment(digits_input))
    print(display.display_segment("01100111"))
    print(display.display_segment("01100110"))
    print(display.display_segment("01100001"))
    print(display.display_segment("11011011"))
    print(display.display_segment("11101111"))
    print(display.display_segment("11101110"))
    print(display.display_segment("11001111"))
    print(display.display_segment("00011101"))
