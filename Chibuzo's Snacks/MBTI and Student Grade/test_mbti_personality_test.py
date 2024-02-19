from mbti_personality_test import get_mbti_questions


def test_get_mbti_questions():
    assert get_mbti_questions(8) == ("A. seek many tasks, public activities, interaction with others			"
                                     "B. seek private, solitary activities with quiet to concentrate")
