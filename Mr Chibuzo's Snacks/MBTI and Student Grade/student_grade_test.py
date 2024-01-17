from student_grade import *

sample_grades = [[4, 32], [89, 23], [45, 67], [23, 34], [12, 98]]
set_grades(sample_grades)


def test_get_total():
    assert get_total(grades[3]) == 57


def test_get_average():
    assert get_average(grades[0]) == 18.0


def test_get_position():
    assert get_position(grades[4]) == 3


def test_get_highest_score():
    assert get_highest_score(0) == 89


def test_get_lowest_score():
    assert get_lowest_score(1) == 23


def test_get_total_score():
    assert get_total_score(0) == 173


def test_no_of_passes():
    assert no_of_passes(1) == 2


def test_no_of_failures():
    assert no_of_failures(0) == 4

