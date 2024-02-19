from feb_tasks import task_one

import unittest


class TestFebTaskOne(unittest.TestCase):

    def test_create_sequential_integers_list(self):
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(expected_result, task_one.create_sequential_integers_list())

    def test_given_list_of_integers_duplicate_the_elements(self):
        sample_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        sample_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        expected_result = sample_list1 + sample_list2

        self.assertEqual(expected_result, task_one.duplicate_numbers_in_a_list())

    def test_given_list_of_duplicated_integers_remove_the_duplicates(self):
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        sample_list = task_one.duplicate_numbers_in_a_list()

        self.assertEqual(expected_result, task_one.remove_duplicated_numbers_in_a_list(sample_list))

    def test_given_list_of_integers_add_every_third_element(self):
        expected_result = 45
        sample_list = task_one.create_sequential_integers_list()

        self.assertEqual(expected_result, task_one.add_every_third_element_in_a_list(sample_list))

    def test_given_an_odd_length_list_of_integers_sum_first_middle_and_last_elements(self):
        expected_result = 24
        sample_list = task_one.create_sequential_integers_list()

        self.assertEqual(expected_result, task_one.sum_first_middle_and_last_elements(sample_list))

    def test_given_an_even_length_list_of_integers_sum_first_middle_and_last_elements(self):
        expected_result = 25.5
        sample_list = task_one.create_sequential_integers_list() + [16]
        print(sample_list)

        self.assertEqual(expected_result, task_one.sum_first_middle_and_last_elements(sample_list))
