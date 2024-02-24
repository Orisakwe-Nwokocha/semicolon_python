import time
from tkinter import simpledialog, messagebox

from oopAccount.account import Account
from oopAccount.bank import Bank
from oopAccount.exceptions.invalid_pin_exception import InvalidPinException


class BankApp:
    def __init__(self):
        self.__first_bank = Bank("First Bank of Nigeria PLC")
        self.__other_banks = []

    def main(self):
        self.__add_other_banks()

    def __add_other_banks(self):
        gt_bank = Bank("Guaranty Trust Bank of Nigeria PLC")
        access_bank = Bank("Access Bank of Nigeria PLC")

        self.__other_banks.append(gt_bank)
        self.__other_banks.append(access_bank)

        self.__register_customer()

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

            self.__first_bank.register_customer("FirstName", "LastName", "1020")
            self.__other_banks[0].register_customer("Jane", "Doe", "0000")
            self.__other_banks[1].register_customer("FirstName", "LastName", "4321")

            self.__login(account)

    def __login(self, account: Account):
        BankApp.__print_message("Welcome to first mobile app!!!")
        pin = BankApp.__user_input("Enter your pin to login:")

        while account.is_incorrect(pin):
            BankApp.__print_message("Incorrect pin!!!\nPlease enter your pin to login:")
            pin = BankApp.__user_input("Enter your pin to login:")

        self.__go_to_main_menu(account)

    @staticmethod
    def __user_input(prompt):
        return simpledialog.askstring("Input", prompt)

    @staticmethod
    def __print_message(prompt):
        messagebox.showinfo("Message", prompt)

    @staticmethod
    def __exit_app():
        BankApp.__print_message("Exiting...")
        time.sleep(2.5)

        exit(0)

    def __go_to_main_menu(self, account: Account):
        main_menu = """What do you want to do today?

        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check Balance
        5. Close Account
        6. Exit

        Select option:"""

        user_choice = BankApp.__user_input(main_menu)

        if user_choice == "1":
            self.__deposit(account)
        elif user_choice == "2":
            withdraw(account)
        elif user_choice == "3":
            transfer(account)
        elif user_choice == "4":
            check_balance(account)
        elif user_choice == "5":
            remove_account(account)
        elif user_choice == "6":
            exit_app()
        else:
            go_to_main_menu(account)

    def __deposit(self, account: Account):
        amount = BankApp.__user_input("Enter amount to deposit:")

        try:
            self.__first_bank.deposit(account.get_number(), int(amount))
            BankApp.__print_message("Amount successfully deposited.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            self.__go_to_main_menu(account)

    def remove_account(self, account: Account):
        pin = BankApp.__user_input("Enter account pin:")
        try:
            first_bank.remove_account(account.get_number(), pin)
            print_message("Account successfully removed.")
        except Exception as e:
            BankApp.__print_message(str(e))
        finally:
            exit_app()

    def check_balance(account):
        pin = user_input("Enter account pin:")
        try:
            balance = first_bank.check_balance(account.get_number(), pin)
            print_message(f"{account.get_name()} balance: ₦{balance}")
        except Exception as e:
            print_message(str(e))
        finally:
            go_to_main_menu(account)

    def transfer(account):
        user_choice = user_input("""Enter 1 to transfer to first bank accounts
        Enter 2 to transfer to other bank accounts""")

        if user_choice == "1":
            intra_bank_transfer(account)
        elif user_choice == "2":
            inter_bank_transfer(account)
        else:
            go_to_main_menu(account)

    def inter_bank_transfer(account):
        for bank in other_banks:
            print_message("*" * 5 + bank.name + "*" * 5)

        choice = user_input("Select option (1 or 2):")
        if choice == "1":
            transfer_to_gt_bank_accounts(account)
        elif choice == "2":
            transfer_to_access_bank_accounts(account)

        go_to_main_menu(account)

    def transfer_to_access_bank_accounts(account):
        receiver_account_number = user_input("Enter account number to credit:")
        amount = user_input("Enter amount to transfer:")
        pin = user_input("Enter account pin:")

        try:
            account.withdraw(int(amount), pin)
            other_banks[-1].deposit(int(receiver_account_number), int(amount))
            print_message("Amount was successfully transferred.")
        except Exception as e:
            print_message(str(e))
        finally:
            go_to_main_menu(account)

    def transfer_to_gt_bank_accounts(account):
        receiver_account_number = user_input("Enter account number to credit:")
        amount = user_input("Enter amount to transfer:")
        pin = user_input("Enter account pin:")

        try:
            account.withdraw(int(amount), pin)
            other_banks[0].deposit(int(receiver_account_number), int(amount))
            print_message("Amount was successfully transferred.")
        except Exception as e:
            print_message(str(e))
        finally:
            go_to_main_menu(account)

    def intra_bank_transfer(account):
        receiver_account_number = user_input("Enter account number to credit:")
        amount = user_input("Enter amount to transfer:")
        pin = user_input("Enter account pin:")

        try:
            first_bank.transfer(account.get_number(), int(receiver_account_number), int(amount), pin)
            print_message("Amount was successfully transferred.")
        except Exception as e:
            print_message(str(e))
        finally:
            go_to_main_menu(account)

    def withdraw(account):
        amount = user_input("Enter amount to withdraw:")
        pin = user_input("Enter account pin:")

        try:
            first_bank.withdraw(account.get_number(), int(amount), pin)
            print_message("Withdraw was successful.")
        except Exception as e:
            print_message(str(e))
        finally:
            go_to_main_menu(account)



