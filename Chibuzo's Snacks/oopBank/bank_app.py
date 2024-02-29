import time
from tkinter import simpledialog, messagebox

from oopBank.account import Account
from oopBank.bank import Bank
from oopBank.exceptions.invalid_pin_exception import InvalidPinException


class BankApp:
    def __init__(self):
        self.__first_bank = Bank("First Bank of Nigeria PLC")
        self.__other_banks = []

    def main(self):
        self.__add_other_banks()
        self.__start_app()

    def __start_app(self):
        choice = messagebox.askyesnocancel("Do you want to create a new account?")
        if choice is None:
            BankApp.__exit_app()
        elif choice:
            self.__register_customer()
        else:
            self.__login()

    def __add_other_banks(self):
        gt_bank = Bank("Guaranty Trust Bank of Nigeria PLC")
        access_bank = Bank("Access Bank of Nigeria PLC")

        self.__other_banks.append(gt_bank)
        self.__other_banks.append(access_bank)

        self.__other_banks[0].register_customer("Jane", "Doe", "0000")
        self.__other_banks[1].register_customer("FirstName", "LastName", "4321")

    def __register_customer(self):
        BankApp.__print_message("Welcome to First Bank.\nEnter your details to create an account")

        first_name = BankApp.__user_input("Enter first name:")
        last_name = BankApp.__user_input("Enter last name:")
        pin = BankApp.__user_input("Enter pin:")

        try:
            Account.validate_pin_format_and_length(pin)
        except InvalidPinException:
            BankApp.__print_message("Account creation was not successful")
            self.__register_customer()
        finally:
            account: Account = self.__first_bank.register_customer(first_name, last_name, pin)
            BankApp.__print_message("Account successfully created.")
            BankApp.__print_message("Your account number is " + str(account.get_number()))

            self.__login()

    def __login(self):
        BankApp.__print_message("Welcome to first mobile app!!!")
        account_number = self.__user_input("Enter your account number: ")

        account: Account = Account("", 1, "0000")
        try:
            account: Account = self.__first_bank.find_account(int(account_number))
        except ValueError as e:
            BankApp.__print_message(f"Error: {e}")
            self.__start_app()
        finally:
            pin = BankApp.__user_input("Enter your pin to login:")
            while account.is_incorrect(pin):
                BankApp.__print_message("Incorrect pin!!!:")
                self.__login()

            self.__go_to_main_menu(account)

    @staticmethod
    def __user_input(prompt) -> str:
        return simpledialog.askstring("Input", prompt)

    @staticmethod
    def __print_message(prompt):
        messagebox.showinfo("Message", prompt)

    @staticmethod
    def __exit_app():
        BankApp.__print_message("Thank you for banking with us\nExiting...")
        time.sleep(2)

        exit(0)

    def __go_to_main_menu(self, account: Account):
        main_menu = """What do you want to do today?
        
        1. Create a new account
        2. Deposit
        3. Withdraw
        4. Transfer
        5. Check Balance
        6. Close Account
        7. Log Out
        8. Exit App

        Select option:"""

        user_choice = BankApp.__user_input(main_menu)

        if user_choice == "1":
            self.__register_customer()
        elif user_choice == "2":
            self.__deposit(account)
        elif user_choice == "3":
            self.__withdraw(account)
        elif user_choice == "4":
            self.__transfer(account)
        elif user_choice == "5":
            self.__check_balance(account)
        elif user_choice == "6":
            self.__remove_account(account)
        elif user_choice == "7":
            self.__logout()
        elif user_choice == "8":
            self.__exit_app()
        else:
            self.__go_to_main_menu(account)

    def __deposit(self, account: Account):
        amount = BankApp.__user_input("Enter amount to deposit:")

        try:
            self.__first_bank.deposit(account.get_number(), int(amount))
            BankApp.__print_message("Amount successfully deposited.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__go_to_main_menu(account)

    def __remove_account(self, account: Account):
        pin = BankApp.__user_input("Enter account pin:")
        try:
            self.__first_bank.remove_account(account.get_number(), pin)
            BankApp.__print_message("Account successfully removed.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__exit_app()

    def __check_balance(self, account: Account):
        pin = BankApp.__user_input("Enter account pin:")
        try:
            balance = self.__first_bank.check_balance(account.get_number(), pin)
            BankApp.__print_message(f"{account.get_name()} balance: ₦{balance}")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__go_to_main_menu(account)

    def __transfer(self, account: Account):
        user_choice = BankApp.__user_input("""Enter 1 to transfer to first bank accounts
Enter 2 to transfer to other bank accounts""")

        if user_choice == "1":
            self.__intra_bank_transfer(account)
        elif user_choice == "2":
            self.__inter_bank_transfer(account)

        self.__go_to_main_menu(account)

    def __inter_bank_transfer(self, account: Account):
        for bank in self.__other_banks:
            BankApp.__print_message("*" * 5 + bank.get_name() + "*" * 5)

        choice = BankApp.__user_input("Select option (1 or 2):")

        if choice == "1":
            self.__transfer_to_gt_bank_accounts(account)
        elif choice == "2":
            self.__transfer_to_access_bank_accounts(account)

        self.__go_to_main_menu(account)

    def __transfer_to_access_bank_accounts(self, account: Account):
        receiver_account_number = BankApp.__user_input("Enter account number to credit:")
        amount = BankApp.__user_input("Enter amount to transfer:")
        pin = BankApp.__user_input("Enter account pin:")

        try:
            account.withdraw(int(amount), pin)
            self.__other_banks[-1].deposit(int(receiver_account_number), int(amount))
            BankApp.__print_message("Amount was successfully transferred.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__go_to_main_menu(account)

    def __transfer_to_gt_bank_accounts(self, account: Account):
        receiver_account_number = BankApp.__user_input("Enter account number to credit:")
        amount = BankApp.__user_input("Enter amount to transfer:")
        pin = BankApp.__user_input("Enter account pin:")

        try:
            account.withdraw(int(amount), pin)
            self.__other_banks[0].deposit(int(receiver_account_number), int(amount))
            BankApp.__print_message("Amount was successfully transferred.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__go_to_main_menu(account)

    def __intra_bank_transfer(self, account):
        receiver_account_number = BankApp.__user_input("Enter account number to credit:")
        amount = BankApp.__user_input("Enter amount to transfer:")
        pin = BankApp.__user_input("Enter account pin:")

        try:
            self.__first_bank.transfer(account.get_number(), int(receiver_account_number), int(amount), pin)
            BankApp.__print_message("Amount was successfully transferred.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__go_to_main_menu(account)

    def __withdraw(self, account: Account):
        amount = BankApp.__user_input("Enter amount to withdraw:")
        pin = BankApp.__user_input("Enter account pin:")

        try:
            self.__first_bank.withdraw(account.get_number(), int(amount), pin)
            BankApp.__print_message("Withdraw was successful.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__go_to_main_menu(account)

    def __logout(self):
        BankApp.__print_message("Logging out...")
        self.__login()


startApp = BankApp()
startApp.main()
