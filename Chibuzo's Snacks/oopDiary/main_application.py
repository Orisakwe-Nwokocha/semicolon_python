from tkinter import simpledialog, messagebox

from oopDiary.diaries import Diaries


class MainApplication:
    def __init__(self):
        self.__diary = None
        self.__diaries_shelf = Diaries()

    def start_app(self):
        self.__print_message("Welcome to C19 Diary Application")

        user_choice = messagebox.askyesno("Create Diary", "Do you want to create a new diary?")
        if user_choice:
            self.__create_diary()

        self.__go_to_main_menu()

    def __go_to_main_menu(self):
        main_menu = """         
        What do you want to do today?

        1. Create Diary
        2. Delete Diary
        3. Add Entry
        4. Lock Diary
        5. Unlock Diary
        6. Find Entry by ID
        7. Update Entry
        8. Delete Entry
        9. View All Entries
        10. Exit

        Select option:"""

        user_choice = self.__user_input(main_menu, "Main Menu")
        if user_choice:
            self.__manage_user_choice(user_choice)

    def __manage_user_choice(self, user_choice: str):
        if user_choice == "1":
            self.__create_diary()
        elif user_choice == "2":
            self.__delete_diary()
        elif user_choice == "3":
            self.__add_entry()
        elif user_choice == "4":
            self.__lock_diary()
        elif user_choice == "5":
            self.__unlock_diary()
        elif user_choice == "6":
            self.__find_entry_by_id()
        elif user_choice == "7":
            self.__update_entry()
        elif user_choice == "8":
            self.__delete_entry()
        elif user_choice == "9":
            self.__view_all_entries()
        elif user_choice == "10":
            self.__exit_app()
        else:
            self.__go_to_main_menu()

    def __create_diary(self):
        username = self.__user_input("Enter a username for the diary:", "Create Diary")
        password = self.__user_input("Enter a password for the diary:", "Create Diary")

        try:
            self.__diaries_shelf.add(username, password)
            self.__print_message("Diary has been created")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __delete_diary(self):
        username = self.__get_diary_username()
        password = self.__user_input("Enter the password of the diary:", "Delete Diary")

        try:
            self.__diaries_shelf.delete(username, password)
            self.__print_message("Diary has been deleted successfully")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __add_entry(self):
        username = self.__get_diary_username()
        self.__ensure_diary_is_unlocked(username)

        title = self.__user_input("Enter the title:", "Add Entry")
        body = self.__user_input("Enter the body:", "Add Entry")

        try:
            self.__diary.create_entry(title, body)
            self.__print_message("Entry has been created successfully")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __lock_diary(self):
        username = self.__get_diary_username()
        try:
            self.__check_lock_status(username)

            self.__diary.lock_diary()
            self.__print_message("Diary has been locked")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __unlock_diary(self):
        username = self.__get_diary_username()
        try:
            self.__check_unlock_status(username)

            password = self.__user_input("Enter password to unlock diary:", "Unlock Diary")
            self.__diary.unlock_diary(password)
            self.__print_message("Diary has been unlocked")
        except Exception as e:
            self.__print_message(str(e))
        finally:
            self.__go_to_main_menu()

    def __find_entry_by_id(self):
        username = self.__get_diary_username()
        self.__ensure_diary_is_unlocked(username)

        entry_id = self.__user_input("Enter ID of the entry you would like to find:", "Find Entry")
        try:
            found_entry = self.__diary.find_entry_by_id(int(entry_id))
            self.__print_message(found_entry)
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __update_entry(self):
        username = self.__get_diary_username()
        self.__ensure_diary_exists(username)
        self.__ensure_diary_is_unlocked(username)

        entry_id = self.__user_input("Enter ID of the entry you want to update:", "Update Entry")
        user_choice = self.__user_input("Enter 1 to update the title\nEnter 2 to update the body\n"
                                        "Enter 3 to update both:", "Update Entry")
        if user_choice:
            self.__manage_option(user_choice, int(entry_id))
        else:
            self.__go_to_main_menu()

    def __manage_option(self, user_choice: str, entry_id: int):
        if user_choice == "1":
            self.__update_entry_title(entry_id)
        elif user_choice == "2":
            self.__update_entry_body(entry_id)
        elif user_choice == "3":
            self.__update_entry_title_and_body(entry_id)
        else:
            self.__go_to_main_menu()

    def __update_entry_title(self, entry_id: int):
        try:
            body = self.__diary.find_entry_by_id(entry_id).get_body()
            new_title = self.__user_input("Enter the new title of the entry:", "Update Entry")
            self.__diary.update_entry(entry_id, new_title, body)

            self.__print_message("Diary has been updated")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __update_entry_body(self, entry_id: int):
        try:
            title = self.__diary.find_entry_by_id(entry_id).get_title()
            new_body = self.__user_input("Enter the new body of the entry:", "Update Entry")
            self.__diary.update_entry(entry_id, title, new_body)

            self.__print_message("Diary has been updated")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __update_entry_title_and_body(self, entry_id: int):
        try:
            new_title = self.__user_input("Enter the new title of the entry:", "Update Entry", )
            new_body = self.__user_input("Enter the new body of the entry:", "Update Entry", )
            self.__diary.update_entry(entry_id, new_title, new_body)

            self.__print_message("Diary has been updated")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __delete_entry(self):
        username = self.__get_diary_username()
        self.__ensure_diary_is_unlocked(username)

        entry_id = self.__user_input("Enter ID of the entry you want to delete:", "Delete Entry")
        try:
            self.__diary.delete_entry(int(entry_id))

            self.__print_message("Entry has been deleted successfully")
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __view_all_entries(self):
        username = self.__get_diary_username()
        self.__ensure_diary_is_unlocked(username)

        try:
            entries = self.__diary.get_entries()
            for entry in entries:
                self.__print_message(entry)
        except Exception as e:
            self.__print_message("Error: " + str(e))
        finally:
            self.__go_to_main_menu()

    def __exit_app(self):
        self.__print_message("Exiting...")
        self.__print_message("Thanks for using our app!!!")
        exit(0)

    def __get_diary_username(self) -> str:
        return self.__user_input("Enter the username of the diary:", "Diary Username")

    def __ensure_diary_exists(self, username: str):
        try:
            self.__diary = self.__diaries_shelf.find_by_username(username)
        except Exception as e:
            self.__print_message("Error: " + str(e))
            self.__go_to_main_menu()

    def __ensure_diary_is_unlocked(self, username: str):
        try:
            self.__diary = self.__diaries_shelf.find_by_username(username)

            if self.__diary.is_locked():
                raise ValueError("Diary is locked")
        except Exception as e:
            self.__print_message(str(e))
            self.__go_to_main_menu()

    def __check_lock_status(self, username: str):
        self.__ensure_diary_exists(username)

        if self.__diary.is_locked():
            raise ValueError("Diary is already locked")

    def __check_unlock_status(self, username: str):
        self.__ensure_diary_exists(username)

        if not self.__diary.is_locked():
            raise ValueError("Diary is already unlocked")

    @staticmethod
    def __print_message(message: str):
        messagebox.showinfo("Message", message)

    @staticmethod
    def __user_input(prompt: str, title: str) -> str:
        return simpledialog.askstring(title, prompt)


if __name__ == "__main__":
    app = MainApplication()
    app.start_app()
