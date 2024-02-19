from feb_tasks import task_two


def test_sum_collection():
    set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 9, 5, 5}
    assert 45 == task_two.sum_collection(set1)


def test_given_an_existing_element_when_removed_returns_the_element():
    set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 9, 5, 5}

    assert 8 == task_two.remove_item(set1, 8)


def test_given_a_non_existing_element_when_removed_returns_none():
    set1 = {1, 2, 3, 4, 5, 6, 8, 9, 2, 9, 5, 5}

    assert None == task_two.remove_item(set1, 7)


def test_given_two_sets_when_concatenated_returns_the_intersection():
    set1 = {1, 2, 3, 4, 5, 6}
    set2 = {2, 4, 7, 8, 9, 10}

    assert {2, 4} == task_two.find_intersection(set1, set2)

