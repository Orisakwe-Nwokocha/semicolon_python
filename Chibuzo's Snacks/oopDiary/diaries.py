from oopDiary.diary import Diary


class Diaries:
    def __init__(self):
        self.__diaries = []

    def size(self):
        return len(self.__diaries)

    def add(self, username: str, password: str):
        diary: Diary = Diary(username, password)
        self.__validate(diary)

        self.__diaries.append(diary)

    def find_by_username(self, username: str) -> Diary:
        for diary in self.__diaries:
            if diary.get_username() == username:
                return diary

        raise ValueError("Diary not found")

    def delete(self, username: str, password: str):
        found_diary: Diary = self.find_by_username(username)
        if not found_diary.verify_password(password):
            raise ValueError("Password is not valid")

        self.__diaries.remove(found_diary)

    def __validate(self, d):
        for diary in self.__diaries:
            if diary == d:
                raise ValueError("Username already exists")
