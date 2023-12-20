from concatenate_two_lists import concatenate_two_lists

def test_concatenate_two_lists():
    letters = ['a', 'b', 'c']
    numbers = [1, 2, 3]
    assert concatenate_two_lists(letters, numbers) == ['a', 'b', 'c', 1, 2, 3]
