from oopDiary.entry import Entry
from oopDiary.incorrect_password_error import IncorrectPasswordError


class Diary:
    def __init__(self, password):
        self.__is_locked = False
        self.__password = password
        self.__last_entry_created = 0
        self.__entries = []

    def is_locked(self) -> bool:
        return self.__is_locked

    def unlock_diary(self, password):
        self.validate(password)
        self.__is_locked = False

    def lock_diary(self):
        self.__is_locked = True

    def create_entry(self, title, body):
        self.__last_entry_created += 1
        new_entry = Entry(self.__last_entry_created, title, body)

        self.__entries.append(new_entry)

    def number_of_entries(self) -> int:
        return len(self.__entries)

    def find_entry_by_id(self, entry_id) -> Entry:
        for entry in self.__entries:
            if entry.get_id() == entry_id:
                return entry
        raise ValueError("Entry does not exist")

    def validate(self, password):
        if self.__password != password:
            raise IncorrectPasswordError("Password is incorrect")

    def delete_entry(self, entry_id):
        found_entry: Entry = self.find_entry_by_id(entry_id)
        self.__entries.remove(found_entry)

    def update_entry(self, entry_id, new_title, new_body):
        entry: Entry = self.find_entry_by_id(entry_id)

        entry.update_title(new_title)
        entry.update_body(new_body)

    def __repr__(self):
        return f"Diary[locked: {self.__is_locked}, entries: {self.__entries}\n\t]"
