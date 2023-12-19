from odd_positions_list import odd_positions

def test_odd_positions():
    assert odd_positions(['f', 2, 3, 'd', True]) == ['f', 3, True]
