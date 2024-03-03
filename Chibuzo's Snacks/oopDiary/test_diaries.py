import unittest
from oopDiary.diaries import Diaries
from oopDiary.diary import Diary


class TestDiaries(unittest.TestCase):

    def setUp(self):
        self.shelf = Diaries()

    def test_default_state_is_empty(self):
        self.assertEqual(0, self.shelf.size())

    def test_add_diary(self):
        self.shelf.add("username", "password")

        self.assertEqual(1, self.shelf.size())

    def test_add_diary_twice(self):
        self.shelf.add("username", "password")
        self.shelf.add("anotherUsername", "anotherPassword")

        self.assertEqual(2, self.shelf.size())

    def test_givenSameUsername_whenEquals_thenDiariesEqual(self):
        diary1: Diary = Diary("username", "password")
        diary2: Diary = Diary("username", "anotherPassword")

        self.assertEqual(diary1, diary2)

    def test_givenDifferentUsername_whenEquals_thenDiariesNotEqual(self):
        diary1: Diary = Diary("username", "password")
        diary2: Diary = Diary("differentUsername", "anotherPassword")

        self.assertNotEqual(diary1, diary2)

    def test_findByNonExistentUsername_raisesValueError(self):
        self.shelf.add("username", "password")
        self.assertEqual(1, self.shelf.size())

        self.assertRaises(ValueError, self.shelf.find_by_username, "anotherUsername")

    def test_add_diaryTwiceWithSameUsername_raisesValueError(self):
        self.shelf.add("username", "password")
        self.assertEqual(1, self.shelf.size())

        self.assertRaises(ValueError, self.shelf.add, "username", "correctPassword")
        self.assertEqual(1, self.shelf.size())

    def test_deleteDiary_shelfSizeIs0(self):
        self.shelf.add("username", "correctPassword")
        self.assertEqual(1, self.shelf.size())

        self.shelf.delete("username", "correctPassword")
        self.assertEqual(0, self.shelf.size())
