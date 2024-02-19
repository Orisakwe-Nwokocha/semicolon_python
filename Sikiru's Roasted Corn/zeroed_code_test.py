from zeroed_code import zeroed_code

def test_zeroed_code():
    a_list = [4,5,6,7,8,9]
    assert zeroed_code(a_list) == [0,5,6,7,8,0]