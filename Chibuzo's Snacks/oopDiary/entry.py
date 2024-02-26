from datetime import datetime


class Entry:
    def __init__(self, entry_id: int, title: str, body: str):
        self.__id = entry_id
        self.__title = title
        self.__body = body
        self.__date_created = datetime.now()

    def get_id(self) -> int:
        return self.__id

    def get_title(self) -> str:
        return self.__title

    def get_body(self) -> str:
        return self.__body

    def update_title(self, new_title: str):
        self.__title = new_title

    def update_body(self, new_body: str):
        self.__body = new_body

    def get_date_created(self) -> str:
        return self.__date_created.strftime("%d/%m/%Y %I:%M:%S %p").split(" ")[0]

    def __repr__(self):
        return (f"Entry[\n\tid ===> {self.__id}\n\tdate created ===> {self.get_date_created()}"
                f"\n\ttitle ===> {self.__title}\n\tbody ===> {self.__body}\n\t]")
