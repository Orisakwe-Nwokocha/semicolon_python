from only_floats import only_floats

def test_only_floats_2():
	assert only_floats(12.1, 23.0) == 2

def test_only_floats_1():
	assert only_floats(12.1, 23) == 1

def test_only_floats_0():
	assert only_floats(12, 23) == 0

def test_only_floats_two_negative_numbers_2():
	assert only_floats(-12.1, -23.0) == 2

def test_only_floats_one_negative_one_positive_1():
	assert only_floats(-12.1, 23) == 1