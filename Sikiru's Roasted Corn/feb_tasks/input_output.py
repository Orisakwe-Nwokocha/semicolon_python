from tkinter import simpledialog, messagebox


class InputOutput:
    def __init__(self):
        self.__data = ""

    def get_string(self, prompt):
        self.__data = simpledialog.askstring("Enter anything", prompt)

    def print_string(self):
        return self.__data.upper()



