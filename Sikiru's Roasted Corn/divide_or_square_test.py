from divide_or_square import divide_or_square

def test_divide_or_square_square():
    assert divide_or_square(25) == 5.0


def test_divide_or_square_divide():
    assert divide_or_square(21) == 1
