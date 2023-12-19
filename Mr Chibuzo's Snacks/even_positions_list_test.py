from even_positions_list import even_positions

def test_even_positions():
    assert even_positions(['f', 2, 3, 'd', True]) == [2, 'd']
