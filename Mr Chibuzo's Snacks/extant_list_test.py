from extant_list import existing_element

def test_existing_element_true():
    assert existing_element([1, 2, True, 'c19', 3.5], 'c19') == True

def test_existing_element_false():
    assert existing_element([1, 2, True, 'c19', 3.5], 19) == False
