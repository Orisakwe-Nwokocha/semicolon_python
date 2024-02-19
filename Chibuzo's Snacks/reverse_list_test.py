from reverse_list import reverse_any_list

def test_reverse_any_list():
    my_array = [1, 2, True, 'c19', 3.5]
    assert reverse_any_list(my_array) == [3.5, 'c19', True, 2, 1]
