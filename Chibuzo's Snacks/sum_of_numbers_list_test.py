from sum_of_numbers_list import sum_of_numbers_for_loop, sum_of_numbers_while_loop, sum_of_numbers_do_while_loop


def test_sum_of_numbers_for_loop():
    numbers = [10, 20, 30, 40, 50]
    assert sum_of_numbers_for_loop(numbers) == 150


def test_sum_of_numbers_while_loop():
    numbers = [5, -15, 25, -35, 45]
    assert sum_of_numbers_for_loop(numbers) == 25


def test_sum_of_numbers_do_while_loop():
    numbers = [30, 25, 20, 15, 10, 5, 0]
    assert sum_of_numbers_do_while_loop(numbers) == 105