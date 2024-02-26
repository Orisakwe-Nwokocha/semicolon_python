import unittest
from datetime import datetime

from oopDiary.diary import Diary
from oopDiary.incorrect_password_error import IncorrectPasswordError


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("correctPassword")

    def test_initial_state_diary_is_unlocked(self):
        self.assertFalse(self.diary.is_locked())

    def test_diaryIsLocked_unlockDiary(self):
        self.assertFalse(self.diary.is_locked())

        self.diary.unlock_diary("correctPassword")
        self.assertFalse(self.diary.is_locked())

    def test_diaryIsUnLocked_lockDiary(self):
        self.assertFalse(self.diary.is_locked())

        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_unlockDiaryWithIncorrectPassword_raisesIncorrectPasswordError(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

        with self.assertRaises(IncorrectPasswordError):
            self.diary.unlock_diary("incorrectPassword")

    def test_create_entry(self):
        self.diary.create_entry("title", "body")

        self.assertEqual(1, self.diary.number_of_entries())

    def test_create_entry_twice(self):
        self.diary.create_entry("title", "body")
        self.diary.create_entry("title2", "body2")

        self.assertEqual(2, self.diary.number_of_entries())

    def test_find_entry_by_id(self):
        self.diary.create_entry("title", "body")
        found_entry = self.diary.find_entry_by_id(1)

        self.assertEqual(1, found_entry.get_id())
        self.assertEqual(1, self.diary.number_of_entries())

    def test_delete_entry(self):
        self.diary.create_entry("title", "body")
        self.diary.create_entry("title2", "body2")
        self.diary.create_entry("title3", "body3")
        self.assertEqual(3, self.diary.number_of_entries())

        self.diary.delete_entry(2)
        self.assertEqual(2, self.diary.number_of_entries())

    def test_updateEntryTitle(self):
        self.diary.create_entry("title", "body")
        self.assertEqual(1, self.diary.number_of_entries())
        self.assertEqual("title", self.diary.find_entry_by_id(1).get_title())
        self.assertEqual("body", self.diary.find_entry_by_id(1).get_body())

        self.diary.update_entry(1, "newTitle", "body")

        self.assertEqual("newTitle", self.diary.find_entry_by_id(1).get_title())
        self.assertEqual("body", self.diary.find_entry_by_id(1).get_body())
        self.assertEqual(1, self.diary.number_of_entries())

    def test_updateEntryBody(self):
        self.diary.create_entry("title", "body")
        self.assertEqual(1, self.diary.number_of_entries())
        self.assertEqual("body", self.diary.find_entry_by_id(1).get_body())
        self.assertEqual("title", self.diary.find_entry_by_id(1).get_title())

        self.diary.update_entry(1, "title", "newBody")

        self.assertEqual("newBody", self.diary.find_entry_by_id(1).get_body())
        self.assertEqual("title", self.diary.find_entry_by_id(1).get_title())
        self.assertEqual(1, self.diary.number_of_entries())

    def test_update_entry_title_and_body(self):
        self.diary.create_entry("title", "body")
        self.assertEqual(1, self.diary.number_of_entries())
        self.assertEqual("title", self.diary.find_entry_by_id(1).get_title())
        self.assertEqual("body", self.diary.find_entry_by_id(1).get_body())

        self.diary.update_entry(1, "newTitle", "newBody")

        self.assertEqual(1, self.diary.number_of_entries())
        self.assertEqual("newTitle", self.diary.find_entry_by_id(1).get_title())
        self.assertEqual("newBody", self.diary.find_entry_by_id(1).get_body())

    def test_creation_date_for_entry(self):
        self.diary.create_entry("title", "body")
        found_entry = self.diary.find_entry_by_id(1)

        current_date_and_time = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p").split(" ")[0]
        self.assertEqual(current_date_and_time, found_entry.get_date_created().split(" ")[0])

    def test_print_diary(self):
        self.diary.create_entry("title1", "body1")
        self.diary.create_entry("title2", "body2")

        print()
        print(self.diary)

    def test_findNonExistingEntry_raisesValueError(self):
        self.assertRaises(ValueError, self.diary.find_entry_by_id, "nonExistingEntry")

