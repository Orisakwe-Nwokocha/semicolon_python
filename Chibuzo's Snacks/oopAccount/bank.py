from oopAccount.account import Account
from oopAccount.exceptions.invalid_pin_exception import InvalidPinException


class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []
        self.__lastAccountCreated = 0

    def register_customer(self, first_name, last_name, pin):
        name = first_name + " " + last_name
        number = self.generate_account_number()
        account: Account = Account(name, number, pin)
        self.__accounts.append(account)

        return account

    def generate_account_number(self):
        self.__lastAccountCreated += 1
        return self.__lastAccountCreated

    def find_account(self, account_number):
        for account in self.__accounts:
            if account.get_number() == account_number:
                return account

        raise ValueError("Account does not exist.")

    def check_balance(self, account_number, pin):
        account: Account = self.find_account(account_number)

        return account.check_balance(pin)

    def deposit(self, account_number, amount):
        account: Account = self.find_account(account_number)

        account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account: Account = self.find_account(account_number)

        account.withdraw(amount, pin)

    def transfer(self, sender_account_number, receiver_account_number, amount, pin):
        sender: Account = self.find_account(sender_account_number)
        receiver: Account = self.find_account(receiver_account_number)

        sender.withdraw(amount, pin)
        receiver.deposit(amount)

    def remove_account(self, account_number, pin):
        account: Account = self.find_account(account_number)
        if account.is_incorrect(pin):
            raise InvalidPinException("PIN provided is not valid.")
        
        self.__accounts.remove(account)
