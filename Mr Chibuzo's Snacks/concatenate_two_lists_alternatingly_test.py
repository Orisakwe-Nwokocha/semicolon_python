from concatenate_two_lists_alternatingly import concatenate_two_lists_alternatingly

def test_concatenate_two_lists_alternatingly():
    letters = ['a', 'b', 'c', 4]
    numbers = [1, 2, 3]
    assert concatenate_two_lists_alternatingly(letters, numbers) == ['a', 1, 'b', 2, 'c', 3, 4]
