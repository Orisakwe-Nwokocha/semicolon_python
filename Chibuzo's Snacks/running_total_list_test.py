from running_total_list import running_total

def test_running_total():
    assert running_total([1, 2, 3, 4, 5, -3]) == [1, 3, 6, 10, 15, 12]
