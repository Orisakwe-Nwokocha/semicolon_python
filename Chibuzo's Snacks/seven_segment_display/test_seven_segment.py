import unittest

from seven_segment_display.exceptions.non_binary_error import NonBinaryNumberError
from seven_segment_display.exceptions.non_digit_error import NonDigitNumberError
from seven_segment_display.seven_segment import SevenSegmentDisplay


class TestSevenSegmentDisplay(unittest.TestCase):
    def setUp(self):
        self.display = SevenSegmentDisplay()

    def test_user_inputs_non_digit_number_raises_non_digit_number_error(self):
        self.assertRaises(NonDigitNumberError, self.display.display_segment, "1234s678")

    def test_user_inputs_non_binary_digit_number_raises_non_binary_number_error(self):
        self.assertRaises(NonBinaryNumberError, self.display.display_segment, "12345678")

    def test_user_inputs_more_than_8_digit_numbers_raises_value_error(self):
        self.assertRaises(ValueError, self.display.display_segment, "010011101")

    def test_user_inputs_less_than_8_digit_numbers_raises_value_error(self):
        self.assertRaises(ValueError, self.display.display_segment, "0100101")

    def test_given_11111100_board_is_off(self):
        self.display.display_segment("11111100")
        self.assertFalse(self.display.is_on())

    def test_given_11111101_board_is_on(self):
        self.display.display_segment("11111101")
        self.assertTrue(self.display.is_on())
        self.display.display_segment("11111100")
        self.assertFalse(self.display.is_on())

    def test_given_11111100_is_off_then_empty_string_is_displayed(self):
        self.assertEqual("", self.display.display_segment("11111100"))
        self.assertFalse(self.display.is_on())

    def test_given_11111101_board_is_on_when_displayed_then_hashtags_representing_0_is_displayed(self):
        actual = self.display.display_segment("11111101")
        self.assertTrue(self.display.is_on())
        expected = """# # # #
#     #
#     #       
#     #
#     #
# # # #
"""
        self.assertEqual(expected, actual)
