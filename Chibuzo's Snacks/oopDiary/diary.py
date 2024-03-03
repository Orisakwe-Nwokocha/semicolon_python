from typing import List

from oopDiary.entry import Entry
from oopDiary.incorrect_password_error import IncorrectPasswordError


class Diary:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__is_locked = False
        self.__last_entry_created = 0
        self.__entries = []

    def is_locked(self) -> bool:
        return self.__is_locked

    def unlock_diary(self, password: str):
        self.__validate(password)
        self.__is_locked = False

    def lock_diary(self):
        self.__is_locked = True

    def create_entry(self, title: str, body: str):
        self.__last_entry_created += 1
        new_entry = Entry(self.__last_entry_created, title, body)

        self.__entries.append(new_entry)

    def number_of_entries(self) -> int:
        return len(self.__entries)

    def find_entry_by_id(self, entry_id: int) -> Entry:
        for entry in self.__entries:
            if entry.get_id() == entry_id:
                return entry
        raise ValueError("Entry does not exist")

    def __validate(self, password: str):
        if self.__password != password:
            raise IncorrectPasswordError("Password is incorrect")

    def delete_entry(self, entry_id: int):
        found_entry: Entry = self.find_entry_by_id(entry_id)
        self.__entries.remove(found_entry)

    def update_entry(self, entry_id: int, new_title: str, new_body: str):
        entry: Entry = self.find_entry_by_id(entry_id)

        entry.update_title(new_title)
        entry.update_body(new_body)

    def get_username(self) -> str:
        return self.__username

    def verify_password(self, password) -> bool:
        return self.__password == password

    def get_entries(self) -> List[Entry]:
        return self.__entries

    def __eq__(self, other):
        return self.__username == other.__username

    def __repr__(self):
        return f"Diary[locked: {self.__is_locked}, entries: {self.__entries}\n\t]"
