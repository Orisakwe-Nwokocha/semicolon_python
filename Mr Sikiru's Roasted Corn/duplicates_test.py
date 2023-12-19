from duplicates import check_duplicates

def test_check_duplicates_true():
    fruits = ['apple', 'orange', 'banana', 'apple']
    assert check_duplicates(fruits) == ['apple']

def test_check_duplicates_false():
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']
    assert check_duplicates(names) == "no duplicates"
