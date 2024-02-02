from class_task import *


class TestClassTask:

    def test_list_of_numbers(self):
        assert list_of_numbers() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_length_of_list(self):
        assert length_of_list() == 10

    def test_sum_of_numbers_at_even_positions(self):
        assert sum_of_numbers_at_even_positions() == 30

    def test_sum_of_numbers_at_odd_positions(self):
        assert sum_of_numbers_at_odd_positions() == 25

    def test_multiply_numbers_at_every_third_position(self):
        assert multiply_numbers_at_every_third_position() == 162

    def test_average_of_all_numbers_in_a_list(self):
        assert average_of_all_numbers_in_a_list() == 5.5

    def test_largest_number_in_the_list(self):
        assert largest_number_in_the_list() == 10

    def test_smallest_number_in_the_list(self):
        assert smallest_number_in_the_list() == 1

    def test_number_of_strings_in_a_list(self):
        given_strings = ['hello', 'world', 'anna', 'dayo', 'oyo', 'whds', '121']
        assert number_of_strings_in_a_list(given_strings) == ['anna', 'oyo', '121']
