from list_of_digits import list_of_digits

def test_list_of_digits():
    assert list_of_digits(2342) == [2, 3, 4, 2]

def test_list_of_digits_neg_num():
    assert list_of_digits(-545325) == [5, 4, 5, 3, 2, 5]
